from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.XPATH, "//tbody/tr[@class='cart_item']")
    PRODUCT_NAME = (By.XPATH, ".//td[@class='product-name']//a")
    PRODUCT_QUANTITY = (By.XPATH, ".//td[contains(@class, 'product-quantity')]//input[@type='number']")
    REMOVE_PRODUCT = (By.XPATH, ".//td[@class='product-remove']/a[@class='remove']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[@class='cart-empty']")

    def get_cart_items(self):
        return self.get_elements(self.CART_ITEM)

    def get_product_details(self, cart_item):
        return {
            'name': cart_item.find_element(*self.PRODUCT_NAME).text,
            'quantity': cart_item.find_element(*self.PRODUCT_QUANTITY).get_attribute("value"),
        }

    def remove_product(self, cart_item):
        cart_item.find_element(*self.REMOVE_PRODUCT).click()
        self.wait.until(lambda _: cart_item not in self.get_cart_items())

    def is_cart_empty(self):
        return self.is_element_visible(self.EMPTY_CART_MESSAGE)
