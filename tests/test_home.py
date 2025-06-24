import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Home Page")
def test_valid_url_load(driver):
    """Test-Case-1: Verify that https://www.guvi.in loads successfully."""
    driver.get("https://www.guvi.in/")
    assert "GUVI" in driver.title


@allure.feature("Home Page")
def test_homepage_title(driver):
    """Test-Case-2: Verify the title of the webpage."""
    driver.get("https://www.guvi.in/")
    assert driver.title == "GUVI | Learn to code in your native language"


@allure.feature("Home Page")
def test_login_button_visibility_and_click(driver):
    """Test-Case-3: Verify visibility and clickability of the Login button."""
    home = HomePage(driver)
    driver.get("https://www.guvi.in/")
    assert home.is_element_visible(home.LOGIN_BUTTON)
    home.click_login()
    assert "sign-in" in driver.current_url


@allure.feature("Home Page")
def test_signup_button_redirection(driver):
    """Test-Case-4 & 5: Verify Sign-Up button visibility and navigation."""
    home = HomePage(driver)
    driver.get("https://www.guvi.in/")
    assert home.is_element_visible(home.SIGNUP_BUTTON)
    home.click_signup()
    assert driver.current_url == "https://www.guvi.in/register/"


@allure.feature("Home Page")
def test_main_menu_items(driver):
    """Test-Case-8: Validate menu items like 'Courses', 'LIVE Classes', and 'Practice' are visible."""
    home = HomePage(driver)
    driver.get("https://www.guvi.in/")
    assert home.get_elements([home.NAV_COURSES, home.NAV_LIVE_CLASSES, home.NAV_PRACTICE])


@allure.feature("Home Page")
def test_dobby_assistant_visible(driver):
    """Test-Case-9: Validate that the Dobby Assistant is present on the page."""
    home = HomePage(driver)
    driver.get("https://www.guvi.in/")
    assert home.is_element_visible(home.DOBBY_ASSISTANT)