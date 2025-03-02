import pytest
from pytest_dependency import depends
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.shop_page import ShopPage

@pytest.mark.cart
@pytest.mark.dependency()
@pytest.mark.usefixtures('setup', 'config')
def test_add_to_cart(setup, config):
    """
       Test adding multiple products to the cart.

       This test:
       1. Navigates to the shop page
       2. Adds specific products to the cart
       3. Verifies that all products are added correctly
       4. Checks product names, quantities, and total cart count
    """

    # Test Date - Products to add
    product_wishlist = ["Selenium Ruby", "Functional Programming in JS", "Mastering JavaScript"]

    driver = setup
    home_page = HomePage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)

    # Step 1: Navigate to the website and shop page
    driver.get(config.get_url())
    home_page.navigate_to_shop()

    # Step 2: Get all products from the shop page
    product_elements = shop_page.get_product_list()
    product_names = shop_page.get_product_names(product_elements)

    # Step 3: Add each product from wishlist to the cart
    products_to_add = 0
    for product_name, product_element in zip(product_names, product_elements):
        if product_name in product_wishlist:
            # print(product_name, 'Yes')
            shop_page.add_to_basket(product_element)
            assert shop_page.is_view_basket_visible(), "View Basket is not visible"
            print(f"Products '{product_name}' added to the Cart successfully")
            products_to_add += 1
    # time.sleep(2)

    # Step 4: Verify cart icon updates with correct count
    shop_page.wait_for_cart_icon_to_update()
    assert shop_page.get_added_items_count() == products_to_add, "Item count is not matching with added Items"

    # Step 5: Navigate to cart page
    shop_page.navigate_to_cart()

    # Step 5: Verify total number of items in cart
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == products_to_add == len(product_wishlist), "Cart Item count mismatched"

    # Step 7: Verify each product's details in cart
    for item in cart_items:
        item_details = cart_page.get_product_details(item)
        assert item_details['name'] in product_wishlist, "Cart contains unexpected product"
        assert item_details['quantity'] == '1', f"Unexpected quantity for {item_details['name']}"

    print("Add to Cart Test passed Successfully")


@pytest.mark.cart
@pytest.mark.dependency(depends=['test_add_to_cart'])
@pytest.mark.usefixtures('setup')
def test_remove_from_cart(setup):

    driver = setup
    cart_page = CartPage(driver)

    # Step 1: Verify we have items to remove first
    cart_items = cart_page.get_cart_items()
    assert cart_items, "No items in cart to remove - dependency on test_add_to_cart may have failed"

    # Step 2: Remove all items one by one
    while True:
        cart_items = cart_page.get_cart_items()
        if not cart_items:
            break
        cart_page.remove_product(cart_items[0])
        print("Cart Items removed successfully")

    # Step 3: Verify if Cart is empty
    assert cart_page.is_cart_empty() == "Your basket is currently empty.", "Empty Cart message is not displayed"

    print("Remove item from Cart Test passed successfully ")







