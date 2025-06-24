import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from test_data.credentials import VALID_CREDENTIALS, INVALID_CREDENTIALS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Login Page")
def test_valid_login(driver):
    """Test-Case-6: Verify login with valid credentials."""
    driver.get("https://www.guvi.in/sign-in/")
    login = LoginPage(driver)
    login.login(VALID_CREDENTIALS["email"], VALID_CREDENTIALS["password"])
    WebDriverWait(driver, 15).until(EC.url_contains("courses"))
    assert "courses" in driver.current_url


@allure.feature("Login Page")
def test_invalid_login(driver):
    """Test-Case-7: Verify error for invalid login."""
    driver.get("https://www.guvi.in/sign-in/")
    login = LoginPage(driver)
    login.login(INVALID_CREDENTIALS["email"], INVALID_CREDENTIALS["password"])
    error_message = login.get_error_message()
    assert "Incorrect Email or Password" in error_message


@allure.feature("Login Page")
def test_logout(driver):
    """Test-Case-10: Validate logout functionality."""
    driver.get("https://www.guvi.in/sign-in/")
    login = LoginPage(driver)
    login.login(VALID_CREDENTIALS["email"], VALID_CREDENTIALS["password"])
    WebDriverWait(driver, 15).until(EC.url_contains("courses"))
    assert "courses" in driver.current_url

    # Add actual logout method in HomePage, e.g., click_user_menu() and click_logout()
    home = HomePage(driver)
    home.logout()  # Implement this method
    WebDriverWait(driver, 15).until(EC.url_contains("guvi"))
    assert "guvi" in driver.current_url
