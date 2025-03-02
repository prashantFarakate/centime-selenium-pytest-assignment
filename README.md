# centime-selenium-pytest-assignment
Centime Assignment: Selenium and Pytest web automation framework for an e-commerce application.

## Automated Test Suite - E-Commerce Web Application

### Overview:
This repository contains an automated test suite for an e-commerce web application using Selenium and Pytest. The test suite includes functional test cases for user registration, login, cart management, and address management.

### Features
- Page Object Model implementation
- Data-driven testing
- Configurations
- HTML report generation
- Utilities for handling common operations

### Prerequisites
- Ensure you have the following installed on your system before running the tests:
- Python (3.12)
- Chrome WebDriver 
- Required Python dependencies (listed in requirements.txt)

### Installation
1. Clone the repository

git clone https://github.com/prashantFarakate/centime-selenium-pytest-assignment

2. Create a virtual environment

python -m venv venv 
On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

### Test Execution
- Run all tests: pytest -v
- Run specific test cases: pytest -m register
pytest -m login
pytest -m cart
pytest -m address

## Test Cases
### 1. User Registration (test_user_registration)
- Registers a new user with a unique email.
- Verifies the greeting message.
- Saves credentials for later use.
- Logs out after registration.

### 2. User Login (test_login)
- Logs in using registered credentials.
- Verifies greeting message after login.
- Logs out and checks login page appearance.

### 3. Add to Cart (test_add_to_cart)
- Adds multiple items to the cart.
- Checks if correct items and quantities are displayed.

### 4. Remove from Cart (test_remove_from_cart)
- Removes all items from the cart.
- Confirms the cart is empty.

### 5. Add Address (test_add_address)
- Registers a user  
- navigates to the address section.
- Adds billing address details.
- Save address

### 6. Verify Saved Address (test_saved_address)
- Verify address get saved
- Checks if saved address matches expected details.

### Reporting
- The framework generates HTML reports after test execution when using the --html flag.
- Find report at reports/report.html