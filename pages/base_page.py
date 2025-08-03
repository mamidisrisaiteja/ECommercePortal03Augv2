"""Base Page class for Page Object Model"""
from playwright.sync_api import Page, expect
from abc import ABC, abstractmethod


class BasePage(ABC):
    """Base page class that all page objects should inherit from"""
    
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 30000  # 30 seconds default timeout
    
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
    
    def click_element(self, selector: str):
        """Click an element with wait"""
        self.page.wait_for_selector(selector, timeout=self.timeout)
        self.page.click(selector)
    
    def fill_text(self, selector: str, text: str):
        """Fill text in an input field"""
        self.page.wait_for_selector(selector, timeout=self.timeout)
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        self.page.wait_for_selector(selector, timeout=self.timeout)
        return self.page.text_content(selector)
    
    def is_element_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        try:
            self.page.wait_for_selector(selector, timeout=5000)
            return self.page.is_visible(selector)
        except:
            return False
    
    def wait_for_element(self, selector: str, timeout: int = None):
        """Wait for element to be visible"""
        wait_timeout = timeout or self.timeout
        self.page.wait_for_selector(selector, timeout=wait_timeout)
    
    def verify_text_present(self, text: str):
        """Verify text is present on the page"""
        expect(self.page.locator(f"text={text}")).to_be_visible()
    
    def verify_element_text(self, selector: str, expected_text: str):
        """Verify element contains expected text"""
        expect(self.page.locator(selector)).to_contain_text(expected_text)
    
    def take_screenshot(self, filename: str):
        """Take a screenshot"""
        self.page.screenshot(path=f"reports/screenshots/{filename}")
