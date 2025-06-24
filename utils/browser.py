import pytest
from selenium import webdriver


def get_driver(browser_name: str = "chrome"):
    """Initialize the WebDriver based on browser_name."""
    if browser_name == "chrome":
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                               options=options)

    elif browser_name == "firefox":
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager
        return webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
