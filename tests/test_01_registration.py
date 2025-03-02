import pytest
from utilities.data_generator import generate_unique_email, get_password
from utilities.file_handler import save_credentials
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage

# @pytest.mark.dependency()
@pytest.mark.register
@pytest.mark.usefixtures('setup', 'config')
def test_user_registration(setup, config):
    driver = setup
    home_page = HomePage(driver)
    my_account_page = MyAccountPage(driver)

    driver.get(config.get_url())
    home_page.navigate_to_my_account()

    # Generate unique email and password
    email = generate_unique_email()
    password = get_password()

    # Register a new user and save credentials
    my_account_page.register(email, password)
    save_credentials(email, password)
    print(email, password)

    # Validate greeting message after registration
    username = email.split('@')[0]
    expected_greeting_message = f"Hello {username} (not {username}? Sign out)"
    actual_greeting_message = my_account_page.get_greeting_text()
    print(actual_greeting_message)

    assert expected_greeting_message == actual_greeting_message, f"Expected '{expected_greeting_message}', but got '{actual_greeting_message}'"
    my_account_page.sign_out()
    print("User Registration test passed successfully ")





















