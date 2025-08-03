"""Pytest configuration and fixtures"""
import pytest
import os
from playwright.sync_api import sync_playwright
from datetime import datetime


@pytest.fixture(scope="session")
def playwright_instance():
    """Create a Playwright instance for the test session"""
    with sync_playwright() as p:
        yield p


def pytest_addoption(parser):
    """Add command line options for pytest"""
    parser.addoption(
        "--test-browser",
        action="store",
        default="chromium",
        help="Browser to run tests on: chromium, firefox, webkit"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def browser(playwright_instance, request):
    """Create a browser instance for the test session"""
    # Get browser type from command line argument or environment variable
    browser_name = request.config.getoption("--test-browser") or os.getenv("BROWSER", "chromium")
    browser_name = browser_name.lower()
    
    # Get headless option from command line or environment
    headless_option = request.config.getoption("--headless")
    is_ci = os.getenv("CI", "false").lower() == "true" or os.getenv("GITHUB_ACTIONS", "false").lower() == "true"
    
    # Browser launch options
    launch_options = {
        "headless": headless_option or is_ci,  # Headless if specified or in CI
    }
    
    # Browser-specific configurations for CI stability
    if is_ci:
        if browser_name == "firefox":
            launch_options.update({
                "args": [
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-background-timer-throttling",
                    "--disable-backgrounding-occluded-windows",
                    "--disable-renderer-backgrounding",
                    "--disable-web-security",
                    "--disable-features=TranslateUI",
                    "--disable-component-extensions-with-background-pages",
                    "--no-first-run",
                    "--disable-default-apps"
                ],
                "timeout": 60000,  # 60 seconds timeout
                "handle_sigterm": False,
                "handle_sigint": False
            })
        elif browser_name == "webkit":
            launch_options.update({
                "args": [
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-web-security"
                ],
                "timeout": 60000,  # 60 seconds timeout
                "handle_sigterm": False,
                "handle_sigint": False
            })
        else:  # chromium
            launch_options.update({
                "args": [
                    "--no-sandbox", 
                    "--disable-dev-shm-usage",
                    "--disable-gpu",
                    "--disable-web-security",
                    "--disable-features=VizDisplayCompositor"
                ]
            })
    else:
        # Local development options
        launch_options["args"] = ["--start-maximized"]
        launch_options["slow_mo"] = 500
    
    # Launch the appropriate browser
    if browser_name == "firefox":
        browser = playwright_instance.firefox.launch(**launch_options)
    elif browser_name == "webkit":
        browser = playwright_instance.webkit.launch(**launch_options)
    else:  # default to chromium
        browser = playwright_instance.chromium.launch(**launch_options)
    
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def browser_context(browser):
    """Create a new browser context for each test"""
    # Check if we're in CI environment
    is_ci = os.getenv("CI", "false").lower() == "true" or os.getenv("GITHUB_ACTIONS", "false").lower() == "true"
    
    # Context options
    context_options = {
        "viewport": {'width': 1920, 'height': 1080},
        "ignore_https_errors": True,  # Ignore SSL errors
        "java_script_enabled": True,
        "accept_downloads": True,
        "has_touch": False,
        "is_mobile": False,
        "locale": "en-US",
        "timezone_id": "America/New_York"
    }
    
    # Add video recording only if not in CI to avoid storage issues
    if not is_ci:
        context_options.update({
            "record_video_dir": "reports/videos/",
            "record_video_size": {'width': 1920, 'height': 1080}
        })
    
    try:
        context = browser.new_context(**context_options)
        
        # Set longer timeouts for more stability
        context.set_default_timeout(30000)  # 30 seconds
        context.set_default_navigation_timeout(45000)  # 45 seconds
        
        page = context.new_page()
        
        # Additional page configurations for stability
        page.set_viewport_size({"width": 1920, "height": 1080})
        
        # Create context dictionary to share between steps
        test_context = {
            'page': page,
            'context': context,
            'browser': browser
        }
        
        yield test_context
        
    except Exception as e:
        print(f"Error creating browser context: {e}")
        raise
    finally:
        # Cleanup with proper error handling
        try:
            if 'page' in locals() and page:
                page.close()
        except Exception:
            pass
        try:
            if 'context' in locals() and context:
                context.close()
        except Exception:
            pass


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment before running tests"""
    # Create necessary directories
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/videos", exist_ok=True)
    os.makedirs("reports/html", exist_ok=True)
    
    print("Test environment setup completed")


@pytest.fixture(autouse=True)
def test_metadata(request):
    """Add metadata to each test"""
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Add test metadata
    request.node.test_timestamp = timestamp
    request.node.test_start_time = datetime.now()
    
    yield
    
    # Calculate test duration
    end_time = datetime.now()
    duration = end_time - request.node.test_start_time
    request.node.test_duration = duration.total_seconds()


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line("markers", "auth: Authentication module tests")
    config.addinivalue_line("markers", "inventory: Inventory module tests")
    config.addinivalue_line("markers", "cart: Shopping cart module tests")
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "TC_AUTH_01: Test case for login with valid credentials")
    config.addinivalue_line("markers", "inventory_view: View product inventory")
    config.addinivalue_line("markers", "add_to_cart: Add products to cart")


def pytest_html_report_title(report):
    """Customize HTML report title"""
    report.title = "ECommerce Portal - Test Automation Report"


def pytest_html_results_summary(prefix, summary, postfix):
    """Customize HTML report summary"""
    prefix.extend([
        "<h2>Test Environment Information</h2>",
        "<table>",
        "<tr><td>Application URL</td><td>https://www.saucedemo.com/</td></tr>",
        "<tr><td>Browser</td><td>Chromium</td></tr>",
        "<tr><td>Test Framework</td><td>Pytest + Playwright + BDD</td></tr>",
        "</table>"
    ])


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots on test failure"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Get the browser context from the test
        if hasattr(item, 'funcargs') and 'browser_context' in item.funcargs:
            context = item.funcargs['browser_context']
            page = context.get('page')
            if page:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"failed_{item.name}_{timestamp}.png"
                screenshot_path = f"reports/screenshots/{screenshot_name}"
                page.screenshot(path=screenshot_path)
                
                # Add screenshot to HTML report
                if hasattr(rep, 'extra'):
                    try:
                        from pytest_html import extras
                        rep.extra.append(extras.image(screenshot_path))
                    except ImportError:
                        pass
