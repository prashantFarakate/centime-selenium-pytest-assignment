from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    CART_ITEM = (By.XPATH, "//tbody/tr[@class='cart_item']")
    PRODUCT_NAME_HEADER = (By.XPATH, "//th[@class='product_name']")
    PRODUCT_QUANTITY_HEADER= (By.XPATH, "//th[@class='product-quantity']")

    REMOVE_PRODUCT = (By.XPATH, ".//td[@class='product-remove']/a[@class='remove']")
    PRODUCT_NAME = (By.XPATH, ".//td[@class='product-name']//a")
    PRODUCT_PRICE = (By.XPATH, ".//td[@class='product-price']/span")
    PRODUCT_QUANTITY = (By.XPATH, ".//td[contains(@class, 'product-quantity')]//input[@type='number']")
    PRODUCT_TOTAL = (By.XPATH, ".//td[@class='product-subtotal']/span")

    EMPTY_CART_MESSAGE = (By.XPATH, "//p[@class='cart-empty']")


    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_item(self):
        return self.get_element(self.CART_ITEM)

    def get_cart_items(self):
        return self.get_elements(self.CART_ITEM)

    def get_product_details(self, cart_item):
        name = cart_item.find_element(*self.PRODUCT_NAME).text
        price = cart_item.find_element(*self.PRODUCT_PRICE).text
        quantity = cart_item.find_element(*self.PRODUCT_QUANTITY).get_attribute("value")
        total = cart_item.find_element(*self.PRODUCT_TOTAL).text

        return {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': total
        }

    def remove_product(self, cart_item):
        remove_button = cart_item.find_element(*self.REMOVE_PRODUCT)
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_PRODUCT)).click()
        self.wait.until(EC.staleness_of(cart_item))

    def is_cart_empty(self):
        return self.get_element(self.EMPTY_CART_MESSAGE).text.strip()









