from .base_page import BasePage
from locators.home_locators import HomeLocators as HL
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """Home page object for Guvi site."""

    # Locators needed for tests
    LOGIN_BUTTON = HL.LOGIN_BUTTON                # From HL
    SIGNUP_BUTTON = HL.SIGNUP_BUTTON              # From HL
    NAV_COURSES = HL.NAV_COURSES                  # From HL
    NAV_LIVE_CLASSES = HL.NAV_LIVE_CLASSES        # From HL
    NAV_PRACTICE = HL.NAV_PRACTICE                # From HL
    DOBBY_ASSISTANT = HL.DOBBY_ASSISTANT          # From HL
    LOGOUT_DROPDOWN = HL.LOGOUT_DROPDOWN
    LOGOUT_BUTTON = HL.LOGOUT_BUTTON 

    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)

    def click_signup(self):
        """Click the signup button."""
        self.click(self.SIGNUP_BUTTON)

    def is_element_visible(self, locator) -> bool:
        """Check if an element is visible."""
        return self.is_visible(locator)

    def get_elements(self, locators) -> bool:
        """Check if all locators are visible."""
        return all(self.is_element_visible(locator) for locator in locators)

    def logout(self):
        """Perform logout."""
        self.click(self.LOGOUT_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)