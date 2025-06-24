from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn") 
    ERROR_MSG=(By.XPATH,"//*[@id='passwordGroup']/div")
 # ERROR_MSG = (By.CSS_SELECTOR, ".error-msg")