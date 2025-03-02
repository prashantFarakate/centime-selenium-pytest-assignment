import pytest
from pytest_dependency import depends
from pages.my_account_page import MyAccountPage
from pages.home_page import HomePage
from utilities.file_handler import get_address_details, get_expected_saved_address, load_credentials
from utilities.data_generator import generate_unique_email, get_password

@pytest.mark.dependency()
@pytest.mark.address
@pytest.mark.usefixtures('setup', 'config')
def test_add_address(setup, config):
    driver = setup
    home_page = HomePage(driver)
    my_account_page = MyAccountPage(driver)

    # Step 1: Navigate to My Account page
    driver.get(config.get_url())
    home_page.navigate_to_my_account()

    # Step 2: Register a new user
    email = generate_unique_email()
    password = get_password()
    # credentials = load_credentials()                        # Using existing user credentials
    # email = credentials['email']
    # password = credentials['password']
    my_account_page.register(email, password)

    my_account_page.click_address_link()
    my_account_page.edit_billing_address()

    # Step 3: Add billing address details
    my_account_page.add_address_details(get_address_details())

    print("Add Address details test passed Successfully")


@pytest.mark.dependency(depends=["test_add_address"])
@pytest.mark.address
@pytest.mark.usefixtures('setup')
def test_saved_address(setup):
    driver = setup
    my_account_page = MyAccountPage(driver)

    # Step 1: Navigate to Address section and get saved address
    my_account_page.click_address_link()
    saved_address = my_account_page.get_saved_address()
    expected_saved_address = get_expected_saved_address()

    print(saved_address)
    print(expected_saved_address)

    # Step 2: Verify saved address matches expected details
    assert saved_address == expected_saved_address
















