from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.XPATH, "//*[contains(text(), 'Sign In')]")
    WELCOME_TEXT = (By.XPATH, "//*[contains(text(), 'Welcome back!')]")

    def is_welcome_text_visible(self):
        return self.is_visible(self.WELCOME_TEXT)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SIGN_IN_BUTTON)
