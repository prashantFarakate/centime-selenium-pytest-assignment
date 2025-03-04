import pytest
from pages.home_page import HomePage
from pages.shop_page import ShopPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures('setup', 'config')
class TestCart:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup, config):
        self.driver = setup
        self.config = config
        self.home_page = HomePage(self.driver)
        self.shop_page = ShopPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def add_products(self, product_wishlist):
        # Reusable function to add multiple products to the cart
        self.driver.get(self.config.get_url())
        self.home_page.navigate_to_shop()

        # Get list of available products on the shop page
        product_elements = self.shop_page.get_product_list()
        product_names = self.shop_page.get_product_names(product_elements)

        # Add products from wishlist to the cart
        added_count = sum(
            1 for name, element in zip(product_names, product_elements)
            if name in product_wishlist and self.shop_page.add_to_basket(element)
        )

        assert self.shop_page.is_view_basket_visible(), "View Basket is not visible"
        return added_count

    def verify_cart_items(self, expected_products):
        # Reusable function to verify cart items
        cart_items = self.cart_page.get_cart_items()
        assert len(cart_items) == len(expected_products), "Cart Item count mismatched"

        # Validate product details in the cart
        for item in cart_items:
            details = self.cart_page.get_product_details(item)
            assert details['name'] in expected_products, f"Unexpected product: {details['name']}"
            assert details['quantity'] == '1', f"Incorrect quantity for {details['name']}"

    def test_add_single_product(self):
        product_wishlist = ["Selenium Ruby"]
        products_added = self.add_products(product_wishlist)

        # Ensure cart icon updates with correct count
        self.shop_page.wait_for_cart_icon_to_update()
        assert self.shop_page.get_added_items_count() == products_added, "Mismatch in added items"

        # Navigate to cart and verify added product
        self.shop_page.navigate_to_cart()
        self.verify_cart_items(product_wishlist)

        print("Add Single Product Test Passed Successfully")

    def test_add_multiple_products(self):
        product_wishlist = ["Selenium Ruby", "Functional Programming in JS", "Mastering JavaScript"]
        products_added = self.add_products(product_wishlist)

        # Verify cart icon updates with correct count
        self.shop_page.wait_for_cart_icon_to_update()
        assert self.shop_page.get_added_items_count() == products_added, "Mismatch in added items"

        # Navigate to cart and verify all products are present
        self.shop_page.navigate_to_cart()
        self.verify_cart_items(product_wishlist)

        print("Add Multiple Products Test Passed Successfully")

    def test_delete_single_product_from_cart(self):
        # Test case to add a single product and then delete it from the cart
        product_wishlist = ["Selenium Ruby"]
        products_added = self.add_products(product_wishlist)

        self.shop_page.wait_for_cart_icon_to_update()
        assert self.shop_page.get_added_items_count() == products_added, "Mismatch in added items"

        self.shop_page.navigate_to_cart()
        self.verify_cart_items(product_wishlist)

        # Removing the product from the cart
        cart_items = self.cart_page.get_cart_items()
        for item in cart_items:
            self.cart_page.remove_product(item)

        # Verify cart is empty after deletion
        assert self.cart_page.is_cart_empty(), "Cart is not empty after deleting products"

        print("Delete Single Product Test Passed Successfully")

    def test_delete_multiple_products(self):
        #Add multiple products and delete them one by one from the cart
        product_wishlist = ["Selenium Ruby", "Functional Programming in JS", "Mastering JavaScript"]
        self.add_products(product_wishlist)

        self.shop_page.navigate_to_cart()
        cart_items = self.cart_page.get_cart_items()
        assert len(cart_items) == len(product_wishlist), "Mismatch in cart items before deletion"

        # Remove all products one by one
        while True:
            cart_items = self.cart_page.get_cart_items()
            if not cart_items:
                break
            self.cart_page.remove_product(cart_items[0])
            print("Cart Items removed successfully")

        assert self.cart_page.is_cart_empty(), "Cart is not empty after deleting all products"

        print("Delete Multiple Products Test Passed Successfully")
