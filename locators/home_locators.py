from selenium.webdriver.common.by import By

class HomeLocators:
    LOGIN_BUTTON = (By.ID, "login-btn") #login button
    SIGNUP_BUTTON = (By.XPATH, "/html/body/main/div[1]/div/div[5]/div/div[2]/a")#sign-up button
    DOBBY_ASSISTANT = (By.XPATH, "//div[@id='chateleon-sub-container-0']") #dobboy bot
    NAV_COURSES = (By.XPATH, "/html/body/main/div[1]/div/div[4]/a")#courses menu
    NAV_LIVE_CLASSES = (By.ID, "liveclasseslink") #live classes menu
    NAV_PRACTICE = (By.ID, "practiceslink") #Practice menu
    LOGOUT_DROPDOWN=(By.ID,"dropdown_container")
    LOGOUT_BUTTON = (By.XPATH, "//ul[@id='drop_contents']/li[4]")