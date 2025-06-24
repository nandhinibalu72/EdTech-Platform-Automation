from .base_page import BasePage
from locators.login_locators import LoginLocators as LL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    EMAIL_INPUT=LL.EMAIL_INPUT
    PASSWORD_INPUT=LL.PASSWORD_INPUT
    LOGIN_BUTTON=LL.LOGIN_BUTTON
    ERROR_MSG=LL.ERROR_MSG
    def login(self, email, password):
        """Perform login."""
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Get error message text."""
        elem = self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG))
        return elem.text
