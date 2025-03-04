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
```bash 
git clone https://github.com/prashantFarakate/centime-selenium-pytest-assignment
```

2. Create a virtual environment
```bash 
python -m venv venv 
venv\Scripts\activate
```
3. Install dependencies
```bash 
pip install -r requirements.txt
```

### Test Execution
- Run all tests: 
```bash 
pytest -v
```
- Run specific test cases: pytest -m register
```bash 
pytest -m register
pytest -m login
pytest -m cart
pytest -m address
```

## Test Cases
Refer **test_cases.xlsx** for detailed testcases
### 1. User Registration (test_user_registration)
- Registers a new user with a unique email.
- Verifies the greeting message.
- Saves credentials for later use.
- Logs out after registration.

### 2. User Login (test_login, test_invalid_login)
- Logs in using registered credentials.
- Verifies greeting message after login.
- Logs out and checks login page appearance.
- Login with Invalid credential and check error message

### 3. Add to Cart (test_add_single_product, test_add_multiple_products)
- Add single item to the cart.
- Adds multiple items to the cart.
- Checks if correct items and quantities are displayed.

### 4. Remove from Cart (test_delete_single_product_from_cart, test_delete_multiple_products)
- Remove single item from the cart.
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
- The framework generates HTML reports after test execution, using the --html flag.
```bash 
pytest -v -s --html=reports/reports.html
```
- Find report at reports/report.html