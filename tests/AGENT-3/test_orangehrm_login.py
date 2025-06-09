import base64
import pytest
from playwright.sync_api import expect, Page

# Credentials from MongoDB Atlas users.credentials collection
# Username: Admin, Password: YWRtaW4xMjM (base64 encoded)
# Username: Admin, Password: d3JvbmdwYXNzd29yZA (base64 encoded)

def decode_base64(encoded_str):
    """Decode a base64 string."""
    # Add padding if necessary
    padding = len(encoded_str) % 4
    if padding:
        encoded_str += "=" * (4 - padding)
    return base64.b64decode(encoded_str).decode('utf-8')

# First password decodes to 'admin123', second to 'wrongpassword'
TEST_CREDENTIALS = [
    {"username": "Admin", "password": decode_base64("YWRtaW4xMjM="), "valid": True},
    {"username": "Admin", "password": decode_base64("d3JvbmdwYXNzd29yZA=="), "valid": False}
]

@pytest.fixture(scope="function", params=TEST_CREDENTIALS)
def login_credential(request):
    """Fixture to provide credentials for tests."""
    return request.param

def test_orangehrm_login(page: Page, login_credential):
    """
    Test OrangeHRM Login Functionality
    
    Steps to Reproduce:
    1. Go to https://opensource-demo.orangehrmlive.com/
    2. Login using credentials from MongoDB Atlas
    3. Verify successful login or error message
    """
    # Go to the login page
    page.goto("https://opensource-demo.orangehrmlive.com/")
    
    # Fill in the username and password fields
    page.fill('input[name="username"]', login_credential["username"])
    page.fill('input[type="password"]', login_credential["password"])
    
    # Click login button
    page.click('button[type="submit"]')
    
    if login_credential["valid"]:
        # For valid credentials, verify successful login by checking that the dashboard is displayed
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        dashboard_header = page.locator('.oxd-topbar-header-title')
        expect(dashboard_header).to_be_visible()
        expect(dashboard_header).to_contain_text("Dashboard")
    else:
        # For invalid credentials, verify error message
        error_message = page.locator('.oxd-alert-content-text')
        expect(error_message).to_be_visible()
        expect(error_message).to_contain_text("Invalid credentials")
