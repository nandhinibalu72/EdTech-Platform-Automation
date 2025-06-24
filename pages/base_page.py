from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page class for common methods across pages."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Wait for element to be clickable and click."""
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def send_keys(self, locator, text):
        """Wait for element and send text."""
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def is_visible(self, locator) -> bool:
        """Check if element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_title(self) -> str:
        """Get the page title."""
        return self.driver.title
