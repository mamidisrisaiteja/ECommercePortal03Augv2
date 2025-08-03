# ECommerce Portal - Test Automation Framework

A comprehensive Python Playwright Pytest Cucumber BDD framework using Page Object Model design pattern for automated testing of the ECommerce Portal.

## 🏗️ Framework Structure

```
ECommercePortal_03Augv2/
├── config.yaml                 # Configuration file with base URLs
├── conftest.py                 # Pytest fixtures and configuration
├── pyproject.toml             # Pytest configuration
├── requirements.txt           # Python dependencies
├── pages/                     # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py          # Base page with common methods
│   ├── login_page.py         # Login page object
│   └── products_page.py      # Products page object
├── features/                  # Gherkin feature files
│   └── authentication.feature # Authentication scenarios
├── step_definitions/          # BDD step implementations
│   ├── __init__.py
│   └── test_authentication_steps.py
├── tests/                     # Test runners
│   ├── __init__.py
│   └── run_tests.py          # Test execution script
├── utils/                     # Utility modules
│   ├── __init__.py
│   └── config_manager.py     # Configuration management
├── reports/                   # Test reports and artifacts
│   ├── html/                 # HTML reports
│   ├── screenshots/          # Failure screenshots
│   └── videos/               # Test execution videos
└── TestData/
    └── TestCaseDocument.xlsx # Test case specifications
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- VS Code with Python extension

### Installation

1. **Activate Virtual Environment** (already configured):
   ```powershell
   # Virtual environment is already set up in .venv/
   ```

2. **Install Dependencies**:
   ```powershell
   & "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" -m pip install -r requirements.txt
   ```

3. **Install Playwright Browsers**:
   ```powershell
   & "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" -m playwright install
   ```

## 🧪 Running Tests

### Using Test Runner
```powershell
# Run authentication tests
& "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" tests/run_tests.py auth

# Run smoke tests
& "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" tests/run_tests.py smoke

# Run all tests
& "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" tests/run_tests.py all

# Run tests by tag
& "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" tests/run_tests.py tag:auth
```

### Using Pytest Directly
```powershell
# Run specific test file
& "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" -m pytest step_definitions/test_authentication_steps.py -v

# Run with specific marker
& "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" -m pytest -m auth -v

# Run with HTML report
& "C:/Users/AN574BV/OneDrive - EY/Desktop/Sai Teja/Professional/TestAI/realTimeProject/ECommercePortal_03Augv2/.venv/Scripts/python.exe" -m pytest --html=reports/html/report.html --self-contained-html -v
```

## 🏷️ Test Tags

- `@auth` - Authentication module tests
- `@inventory` - Inventory/Products module tests  
- `@cart` - Shopping cart module tests
- `@smoke` - Smoke tests for critical functionality

## 📊 Test Reports

After running tests, reports are generated in:
- **HTML Reports**: `reports/html/`
- **Screenshots**: `reports/screenshots/` (on test failures)
- **Videos**: `reports/videos/` (test execution recordings)

## 🔧 Configuration

### config.yaml
```yaml
login_page_base_url: "https://www.saucedemo.com/"
```

### Test Data
Test scenarios are defined in `TestData/TestCaseDocument.xlsx` with the following structure:
- Test Case Id (e.g., TC_AUTH_01)
- Module (e.g., Authentication Module)
- Description
- Detailed Steps (Gherkin format)
- Expected Result

## 🎯 Test Case Coverage

### TC_AUTH_01 - Login with Valid Credentials
- **Module**: Authentication
- **Tags**: @auth, @smoke
- **Description**: Verify user can login with valid credentials
- **Steps**:
  1. Navigate to login page
  2. Enter username: "standard_user"
  3. Enter password: "secret_sauce"
  4. Click login button
  5. Verify "Products" text is displayed

## 🔄 Adding New Tests

### 1. Create Feature File
Add new `.feature` files in the `features/` directory using Gherkin syntax:

```gherkin
@inventory @smoke
Feature: Product Management
  Scenario: View available products
    Given user is logged in
    When user navigates to products page
    Then user should see list of products
```

### 2. Create Step Definitions
Add corresponding step definitions in `step_definitions/`:

```python
from pytest_bdd import given, when, then, scenarios

scenarios('../features/inventory.feature')

@given('user is logged in')
def user_is_logged_in(browser_context):
    # Implementation
    pass
```

### 3. Create Page Objects
Add page objects in `pages/` directory following the POM pattern:

```python
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Define locators and methods
```

## 🛠️ Framework Features

- ✅ **Page Object Model**: Modular and maintainable page objects
- ✅ **BDD with Gherkin**: Human-readable test scenarios
- ✅ **Playwright Integration**: Modern browser automation
- ✅ **HTML Reporting**: Comprehensive test reports with screenshots
- ✅ **Tag-based Execution**: Run specific test suites
- ✅ **Screenshot on Failure**: Automatic failure documentation
- ✅ **Video Recording**: Test execution recordings
- ✅ **Configuration Management**: Centralized config handling
- ✅ **Parallel Execution**: Support for parallel test runs
- ✅ **Cross-browser Support**: Chromium, Firefox, WebKit

## 🤝 Contributing

1. Add new test cases to `TestData/TestCaseDocument.xlsx`
2. Create corresponding feature files in `features/`
3. Implement step definitions in `step_definitions/`
4. Add page objects in `pages/` if needed
5. Update this README with new test information

## 📝 Best Practices

- Use descriptive test names and scenarios
- Keep page objects focused and cohesive
- Add appropriate tags to new tests
- Write reusable step definitions
- Update configuration for environment-specific settings
- Review test reports after each run
