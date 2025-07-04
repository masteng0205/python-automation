from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    HOME_ELEMENT = (By.XPATH, "//*[contains(text(), 'Home')]")
    SKIP_BUTTON = (By.XPATH, "//button[contains(text(), 'Skip for now')]")
    CLIP_LIBRARY_MENU = (By.XPATH, "//a[@href='/video-library/streams']")
    AI_EDIT_MENU = (By.XPATH, "//a[@href='/edited-clip/ai-edit']")

    def wait_for_home(self):
        self.wait_for_url("/home")
        self.is_visible(self.HOME_ELEMENT)

    def handle_skip_popup(self):
        try:
            skip_button = self.wait.until(
                EC.presence_of_element_located(self.SKIP_BUTTON)
            )
            self.scroll_into_view(skip_button)
            self.js_click(skip_button)
            print("✅ Clicked 'Skip for now'.")
        except Exception as e:
            print(f"ℹ️ 'Skip for now' popup not shown: {e}")

    def click_clip_library(self):
        self.click(self.CLIP_LIBRARY_MENU)

    def click_ai_edit_menu(self):
        self.click(self.AI_EDIT_MENU)
        print("✅ Clicked 'Edits' (AI Edit) menu")
