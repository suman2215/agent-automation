# OrangeHRM Login Functionality Tests

This project contains automated tests for OrangeHRM login functionality using Playwright with Python.

## Setup

1. Install dependencies:
   ```
   pip install pytest pytest-playwright playwright
   ```

2. Install browser drivers:
   ```
   playwright install
   ```

## Running Tests

To run the tests:
```
pytest tests/AGENT-3/test_orangehrm_login.py -v
```

## Test Details

The test verifies the login functionality of OrangeHRM:
- It tests both valid and invalid credentials.
- For valid credentials, it verifies successful login and dashboard access.
- For invalid credentials, it verifies the proper error message is displayed.

Credentials are retrieved from MongoDB Atlas `users.credentials` collection.
