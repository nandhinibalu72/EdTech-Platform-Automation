# Project1: GUVI Test Automation Framework

## Architecture
- **Pages**: `BasePage`, `HomePage`, `LoginPage`
- **Tests**: `test_home.py`, `test_login.py`
- **Locators**: All element locators segregated for maintainability
- **Utilities**: Shared methods and helpers

## Features
- Page Object Model (POM) implementation
- Explicit Waits and Exception Handling
- Allure Reports for test results
- Supports multi-browser execution

## Usage
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run the test suite:
    ```
    pytest
    ```
3. Generate Allure Report:
    ```
    pytest --alluredir=allure-results
    allure serve allure-results
    ```

##  Reports
Check the latest test reports here:
[Google Drive Test Reports](https://drive.google.com/drive/folders/11RQdXxryye4Xh0fKh0AxM7sI0ouOs9Dl?usp=drive_link)

---
