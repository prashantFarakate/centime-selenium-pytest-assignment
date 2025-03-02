import json

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage(BasePage):
    # Locators
    REG_EMAIL_ID_INPUT = (By.ID, "reg_email")
    REG_PASSWORD_INPUT = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.NAME, "register")

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")

    GREETING_TEXT = (By.XPATH, "//p[contains(text(),'Hello')]")
    WELCOME_USERNAME = (By.XPATH, "//p//strong")
    SIGN_OUT = (By.XPATH, "//a[text()='Sign out']")

    ADDRESS_LINK = (By.XPATH, "//a[text()='Addresses']")
    EDIT_BILLING_ADDRESS = (By.XPATH, "//h3[contains(text(), 'Billing Address')]/../a[@class='edit']")
    EDIT_SHIPPING_ADDRESS = (By.XPATH, "//h3[contains(text(), 'Shipping Address')]/../a[@class='edit']")
    FIRST_NAME = (By.ID, "billing_first_name")
    LAST_NAME = (By.ID, "billing_last_name")
    COMPANY_NAME = (By.ID, "billing_company")
    BILLING_EMAIL = (By.ID, "billing_email")
    BILLING_PHONE = (By.ID, "billing_phone")

    SELECT_CITY_DROPDOWN = (By.XPATH, "//span[@id='select2-chosen-1']")
    COUNTRY_DROPDOWN = (By.ID, "billing_country")
    # COUNTRY_SEARCH_ARROW = (By.ID, "select2-arrow")
    # ENTER_COUNTRY_NAME = (By.XPATH, "//input[@class='select2-input']")
    STATE_DROPDOWN = (By.ID, "billing_state")

    BILLING_ADDRESS_1 = (By.ID, "billing_address_1")
    BILLING_ADDRESS_2 = (By.ID, "billing_address_2")
    BILLING_CITY = (By.ID, "billing_city")
    BILLING_POSTCODE = (By.ID, "billing_postcode")
    SAVE_ADDRESS_BUTTON = (By.XPATH, "//input[@class='button']")

    SAVED_ADDRESS = (By.XPATH, "//div[header/h3[text()='Billing Address']]/address")

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def enter_username(self, username):
        self.get_element(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.get_element(self.LOGIN_BUTTON).click()

    def register(self, email, password):
        self.input_text(self.REG_EMAIL_ID_INPUT, email)
        self.input_text(self.REG_PASSWORD_INPUT, password)
        self.click(self.REGISTER_BUTTON)

    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_greeting_text(self):
        return self.get_element(self.GREETING_TEXT).text

    def confirm_reg_username(self):
        return self.get_element(self.WELCOME_USERNAME).text

    def sign_out(self):
        self.click(self.SIGN_OUT)

    def click_address_link(self):
        self.click(self.ADDRESS_LINK)

    def edit_billing_address(self):
        self.click(self.EDIT_BILLING_ADDRESS)

    def save_address(self):
        self.click(self.SAVE_ADDRESS_BUTTON)

    def add_address_details(self, address_details):
        self.input_text(self.FIRST_NAME, address_details.get("first_name", ""))
        self.input_text(self.LAST_NAME, address_details.get("last_name", ""))
        self.input_text(self.COMPANY_NAME, address_details.get("company_name", ""))
        self.input_text(self.BILLING_PHONE, address_details.get("billing_phone", ""))

        self.input_text(self.BILLING_ADDRESS_1, address_details.get("billing_address_1", ""))
        self.input_text(self.BILLING_ADDRESS_2, address_details.get("billing_address_2", ""))
        self.input_text(self.BILLING_CITY, address_details.get("billing_city", ""))
        self.input_text(self.BILLING_POSTCODE, address_details.get("billing_postcode", ""))

        if "country_name" in address_details and "country_code" in address_details:
            self.select_country_option(address_details["country_name"], address_details["country_code"])

        if "state" in address_details and "state_code" in address_details:
            self.select_state(address_details["state"], address_details["state_code"])

        self.save_address()

    # def get_saved_address(self):
    #     return self.get_element(self.SAVED_ADDRESS).text

    def get_saved_address(self):
        address_text = self.get_element(self.SAVED_ADDRESS).text

        # Split by newlines to get individual parts
        parts = address_text.split('\n')

        # Parse into a dictionary that matches expected JSON structure
        parsed_address = {}

        if len(parts) >= 1:
            parsed_address["company_name"] = parts[0]
        if len(parts) >= 2:
            parsed_address["name"] = parts[1]
        if len(parts) >= 3:
            parsed_address["address_1"] = parts[2]
        if len(parts) >= 4:
            parsed_address["address_2"] = parts[3]
        if len(parts) >= 5:
            parsed_address["city"] = parts[4]
        if len(parts) >= 6:
            parsed_address["state"] = parts[5]

        return parsed_address

    def enter_first_name(self, first_name):
        self.input_text(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.input_text(self.LAST_NAME, last_name)

    def enter_company_name(self, company_name):
        self.input_text(self.COMPANY_NAME, company_name)

    def enter_phone(self, phone):
        self.input_text(self.BILLING_PHONE, phone)

    def select_country(self):
        self.click(self.SELECT_CITY_DROPDOWN)

    def select_country_option(self, country_name, country_code):
        script = f"jQuery('#billing_country').val('{country_code}').trigger('change');"
        self.driver.execute_script(script)
        self.wait.until(EC.text_to_be_present_in_element((By.ID, "select2-chosen-1"), country_name))

    def enter_address_1(self, address_1):
        self.input_text(self.BILLING_ADDRESS_1, address_1)

    def enter_address_2(self, address_2):
        self.input_text(self.BILLING_ADDRESS_2, address_2)

    def enter_city(self, city):
        self.input_text(self.BILLING_CITY, city)

    def select_state(self, state, state_code):
        script = f"jQuery('#billing_state').val('{state_code}').trigger('change');"
        self.driver.execute_script(script)
        self.wait.until(EC.text_to_be_present_in_element((By.ID, "select2-chosen-2"), state))

    def enter_postcode(self, postcode):
        self.input_text(self.BILLING_POSTCODE, postcode)


