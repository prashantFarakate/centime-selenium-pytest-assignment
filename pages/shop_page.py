import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class ShopPage(BasePage):
    # Locators
    PRODUCTS_LIST = (By.XPATH, "//ul[@class='products masonry-done']/li")
    PRODUCT_NAME = (By.TAG_NAME, "h3")
    ADD_TO_BASKET_LINK = (By.XPATH, ".//a[text()='Add to basket']")
    CART_ICON_LINK = (By.XPATH, "//a[@title='View your shopping cart']")
    CART_ITEMS_COUNT = (By.XPATH, "//span[@class='cartcontents']")
    VIEW_BASKET = (By.XPATH, "//a[@title='View Basket']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def get_product_list(self):
        return self.get_elements(self.PRODUCTS_LIST)

    def get_product_name(self, product_element):
        return product_element.find_element(*self.PRODUCT_NAME).text

    def get_product_names(self, product_elements):
        product_names = []
        for product_element in product_elements:
            product_names.append(product_element.find_element(*self.PRODUCT_NAME).text)
        return product_names

    def add_to_basket(self, product_element):
        ActionChains(self.driver).move_to_element(product_element).perform()
        add_button = product_element.find_element(*self.ADD_TO_BASKET_LINK)
        add_button.click()
        return self

    def is_view_basket_visible(self):
        return self.is_element_visible(self.VIEW_BASKET)

    def wait_for_cart_icon_to_update(self):
        # self.is_element_visible(self.CART_ICON_LINK)
        self.wait.until(EC.visibility_of_element_located(self.CART_ICON_LINK))
        time.sleep(2)

    def get_added_items_count(self):
        self.is_element_visible(self.CART_ITEMS_COUNT)
        text = self.get_element(self.CART_ITEMS_COUNT).text
        return int(text.split()[0])

    def navigate_to_cart(self):
        self.get_element(self.CART_ICON_LINK).click()
        # self.wait.until(EC.visibility_of_element_located(self.CART_ICON_LINK)).click()
        # self.get_element(self.CART_ICON_LINK).click()







