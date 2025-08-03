"""Products Page Object Model"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Products page object following Page Object Model pattern"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Locators
        self.products_header = ".title"
        self.products_container = ".inventory_container"
        self.product_items = ".inventory_item"
        self.add_to_cart_buttons = "[data-test*='add-to-cart']"
        self.shopping_cart_badge = ".shopping_cart_badge"
        self.shopping_cart_link = ".shopping_cart_link"
        self.menu_button = "#react-burger-menu-btn"
        self.logout_link = "#logout_sidebar_link"
    
    def verify_products_page_loaded(self):
        """Verify products page is loaded"""
        self.wait_for_element(self.products_header)
        self.verify_element_text(self.products_header, "Products")
    
    def get_products_count(self) -> int:
        """Get count of products displayed"""
        return len(self.page.locator(self.product_items).all())
    
    def add_product_to_cart(self, product_name: str):
        """Add a specific product to cart by name"""
        product_selector = f"[data-test='add-to-cart-{product_name.lower().replace(' ', '-')}']"
        self.click_element(product_selector)
    
    def get_cart_items_count(self) -> int:
        """Get number of items in cart"""
        if self.is_element_visible(self.shopping_cart_badge):
            badge_text = self.get_text(self.shopping_cart_badge)
            return int(badge_text) if badge_text.isdigit() else 0
        return 0
    
    def go_to_cart(self):
        """Navigate to shopping cart"""
        self.click_element(self.shopping_cart_link)
    
    def logout(self):
        """Logout from the application"""
        self.click_element(self.menu_button)
        self.wait_for_element(self.logout_link)
        self.click_element(self.logout_link)
