import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ShopPage(BasePage):
    PRODUCTS_LIST = (By.XPATH, "//ul[@class='products masonry-done']/li")
    PRODUCT_NAME = (By.TAG_NAME, "h3")
    ADD_TO_BASKET = (By.XPATH, ".//a[text()='Add to basket']")
    CART_ICON = (By.XPATH, "//a[@title='View your shopping cart']")
    CART_ITEMS_COUNT = (By.XPATH, "//span[@class='cartcontents']")
    VIEW_BASKET = (By.XPATH, "//a[@title='View Basket']")

    def get_product_list(self):
        return self.get_elements(self.PRODUCTS_LIST)

    def get_product_names(self, product_elements):
        return [element.find_element(*self.PRODUCT_NAME).text for element in product_elements]

    def add_to_basket(self, product_element):
        ActionChains(self.driver).move_to_element(product_element).perform()
        product_element.find_element(*self.ADD_TO_BASKET).click()
        return self.is_view_basket_visible()

    def is_view_basket_visible(self):
        return self.is_element_visible(self.VIEW_BASKET)

    def wait_for_cart_icon_to_update(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ICON))
        time.sleep(2)
        # self.wait_for_element_text_change(self.CART_ITEMS_COUNT)

    def get_added_items_count(self):
        text = self.get_element(self.CART_ITEMS_COUNT).text
        return int(text.split()[0]) if text else 0

    def navigate_to_cart(self):
        self.get_element(self.CART_ICON).click()


