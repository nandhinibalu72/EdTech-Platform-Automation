import pytest
from utils.browser import get_driver


@pytest.fixture(scope="function")
def driver(request):
    """Initialize and yield WebDriver, then teardown after test."""
    browser_name = request.config.getoption("--browser") or "chrome"
    driver = get_driver(browser_name)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    """Add option for selecting browser."""
    parser.addoption("--browser", action="store", default="chrome", help="Browser name.")
