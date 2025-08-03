"""Step definitions for inventory features"""
import pytest
from pytest_bdd import given, when, then, scenarios
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_manager import config

# Load scenarios from feature files
scenarios('../features/inventory.feature')


# Shared authentication steps
@given('user is on Login Page')
def user_is_on_login_page(browser_context):
    """Navigate to login page"""
    page = browser_context['page']
    login_page = LoginPage(page)
    base_url = config.get_login_page_url()
    login_page.navigate_to_login_page(base_url)
    assert login_page.is_login_page_loaded(), "Login page is not loaded properly"
    browser_context['login_page'] = login_page


@when('user enters user name as "standard_user" and password as "secret_sauce"')
def user_enters_credentials_standard_user(browser_context):
    """Enter standard user credentials"""
    login_page = browser_context['login_page']
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")


@when('click Login Button')
def click_login_button(browser_context):
    """Click the login button"""
    login_page = browser_context['login_page']
    login_page.click_login_button()
    
    # Initialize products page for next steps
    page = browser_context['page']
    products_page = ProductsPage(page)
    browser_context['products_page'] = products_page


@then('verify page has text "Products"')
def verify_page_has_text_products(browser_context):
    """Verify page contains Products text"""
    products_page = browser_context['products_page']
    products_page.verify_products_page_loaded()


# Inventory specific steps
@given('user is on products page')
def user_is_on_products_page(browser_context):
    """Verify user is on products page"""
    products_page = browser_context.get('products_page')
    if not products_page:
        page = browser_context['page']
        products_page = ProductsPage(page)
        browser_context['products_page'] = products_page
    
    products_page.verify_products_page_loaded()


@when('user views the product list')
def user_views_product_list(browser_context):
    """User views the product list"""
    products_page = browser_context['products_page']
    products_count = products_page.get_products_count()
    browser_context['products_count'] = products_count


@then('user should see multiple products available')
def user_should_see_multiple_products(browser_context):
    """Verify multiple products are available"""
    products_count = browser_context.get('products_count', 0)
    assert products_count > 1, f"Expected multiple products, but found {products_count}"


@when('user adds "sauce-labs-backpack" to cart')
def user_adds_product_to_cart(browser_context):
    """Add specific product to cart"""
    products_page = browser_context['products_page']
    products_page.add_product_to_cart("sauce-labs-backpack")


@then('cart should show 1 item')
def cart_should_show_items(browser_context):
    """Verify cart shows expected number of items"""
    products_page = browser_context['products_page']
    cart_count = products_page.get_cart_items_count()
    assert cart_count == 1, f"Expected 1 item in cart, but found {cart_count}"
