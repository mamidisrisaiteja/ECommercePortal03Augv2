"""Login Page Object Model"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object following Page Object Model pattern"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Locators
        self.username_input = "[data-test='username']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-button']"
        self.error_message = "[data-test='error']"
        self.products_header = ".title"
    
    def navigate_to_login_page(self, base_url: str):
        """Navigate to login page"""
        self.navigate_to(base_url)
    
    def enter_username(self, username: str):
        """Enter username in the username field"""
        self.fill_text(self.username_input, username)
    
    def enter_password(self, password: str):
        """Enter password in the password field"""
        self.fill_text(self.password_input, password)
    
    def click_login_button(self):
        """Click the login button"""
        self.click_element(self.login_button)
    
    def login(self, username: str, password: str):
        """Complete login flow with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self) -> str:
        """Get error message text if present"""
        if self.is_element_visible(self.error_message):
            return self.get_text(self.error_message)
        return ""
    
    def verify_login_successful(self):
        """Verify login was successful by checking products page"""
        self.verify_text_present("Products")
    
    def verify_products_text(self):
        """Verify Products text is displayed"""
        self.verify_element_text(self.products_header, "Products")
    
    def is_login_page_loaded(self) -> bool:
        """Check if login page is loaded"""
        return self.is_element_visible(self.username_input) and \
               self.is_element_visible(self.password_input) and \
               self.is_element_visible(self.login_button)
