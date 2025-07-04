from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AccountSettingsPage(BasePage):
    USER_ICON = (By.CLASS_NAME, "ic-user")
    ACCOUNT_SETTINGS_BUTTON = (
        By.XPATH,
        "//button[@role='menuitem' and .//span[normalize-space()='Account Settings']]"
    )
    ACCOUNT_SETTINGS_HEADING = (By.XPATH, "//h2[normalize-space()='Account Setting']")

    def open_account_settings(self):
        # Click profile icon
        self.click(self.USER_ICON)
        print("✅ Clicked user profile icon.")

        # Click account settings button
        self.wait.until(EC.presence_of_element_located(self.ACCOUNT_SETTINGS_BUTTON))
        self.click(self.ACCOUNT_SETTINGS_BUTTON)
        print("✅ Clicked 'Account Settings' button.")

    def is_account_settings_page_displayed(self):
        return self.is_visible(self.ACCOUNT_SETTINGS_HEADING)
