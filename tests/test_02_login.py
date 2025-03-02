import pytest
from pytest_dependency import depends
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage
from utilities.file_handler import load_credentials

# @pytest.mark.dependency(depends=['test_user_registration'])
@pytest.mark.login
@pytest.mark.usefixtures('setup', 'config')
def test_login(setup, config):
    driver = setup
    home_page = HomePage(driver)
    my_account_page = MyAccountPage(driver)

    credentials = load_credentials()
    email = credentials['email']
    password = credentials['password']

    # Step 1: Navigate to My Account
    driver.get(config.get_url())
    home_page.navigate_to_my_account()

    # Step 2: Enter user details
    my_account_page.enter_username(email)
    my_account_page.enter_password(password)
    my_account_page.click_login()

    # Step 3: Verify user Login
    username = email.split('@')[0]
    expected_greeting_message = f"Hello {username} (not {username}? Sign out)"
    actual_greeting_message = my_account_page.get_greeting_text()
    print(actual_greeting_message)
    assert expected_greeting_message == actual_greeting_message, f"Expected '{expected_greeting_message}', but got '{actual_greeting_message}'"
    print("User Login test passed successfully")

    # Step 4: Verify Logout
    my_account_page.sign_out()
    assert my_account_page.get_login_header() == "Login", "Login header value mismatched"
    print("User Logout test passed successfully")