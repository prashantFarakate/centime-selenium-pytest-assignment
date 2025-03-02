from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    SHOP_LINK = (By.XPATH, "//a[text()='Shop']")
    MY_ACCOUNT = (By.XPATH, "//a[text()='My Account']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Method
    def navigate_to_shop(self):
        self.get_element(self.SHOP_LINK).click()

    def navigate_to_my_account(self):
        self.get_element(self.MY_ACCOUNT).click()






