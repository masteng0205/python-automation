from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LandingPage(BasePage):
    SIGN_IN_LINK = (By.PARTIAL_LINK_TEXT, "Sign In")

    def click_sign_in(self):
        self.click(self.SIGN_IN_LINK)
