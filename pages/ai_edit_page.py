from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
import time

class AIEditPage(BasePage):
    PAGE_HEADING = (By.XPATH, "//h2[text()='AI Edit']")
    COOKIE_ACCEPT = (By.XPATH, "//button[contains(text(), 'Accept') and contains(@onclick, 'acceptCookie')]")
    UNDERSTAND_BUTTON = (By.XPATH, "//button[contains(text(), 'Understand')]")
    NOTIFICATION_NOT_NOW = (By.XPATH, "//div[@class='request-notification-snackbar']//div[@class='div-action' and text()='Not Now']")
    CREATE_AI_EDIT_BUTTON = (By.XPATH, "//div[contains(@class,'btn-ai') and contains(., 'Create AI Edit')]")
    START_AI_EDIT_BUTTON = (By.XPATH, "//button[contains(@class, 'ek-primary-button') and text()='Start AI Edit']")
    BROWSE_CLIP_LIBRARY_ENTRY = (By.XPATH, "//div[@class='action']//div[contains(@class,'title') and text()='Browse Clip Library']")
    BROWSE_CLIP_LIBRARY_MODAL_TITLE = (By.XPATH, "//h5[@class='modal-choice-title' and text()='Browse Clips for AI Edit']")
    VICTORY_CLIP = (
        By.XPATH,
        "//div[contains(@class,'item-container')]//div[@class='title' and text()='Victory round - 2x']/ancestor::div[contains(@class, 'item-container')]"
    )
    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'ek-primary-button') and normalize-space(text())='Confirm']"
    )
    AI_EDIT_STUDIO_LOADING_TEXT = (
        By.XPATH,
        "//div[contains(@class, 'loading-text') and normalize-space(text())='Loading AI Edit Studio']"
    )
    GENERATE_AI_EDIT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'ek-primary-button') and contains(@class, 'btn-confirm') and text()='Generate AI Edit']"
    )
    GENERATING_AI_EDIT_TEXT = (
        By.XPATH,
        "//button[contains(@class, 'generate-ai-edit')]//span[contains(text(), 'Generating AI Edit')]"
    )
    VICTORY_RESULT_TITLE = (
        By.XPATH,
        "//div[contains(@class,'list-item')]//div[@class='title' and text()='Victory round - 2x']"
    )

    def accept_cookie_popup_if_present(self):
        try:
            accept_btn = self.wait.until(EC.element_to_be_clickable(self.COOKIE_ACCEPT))
            accept_btn.click()
            print("✅ Accepted cookies.")
        except Exception:
            print("ℹ️ Cookie popup not found.")

    def close_onboarding_popup_if_present(self):
        try:
            popup_button = self.wait.until(EC.element_to_be_clickable(self.UNDERSTAND_BUTTON))
            popup_button.click()
            print("✅ Closed onboarding popup with 'Understand' button.")
        except Exception:
            print("ℹ️ No onboarding popup appeared.")

    def dismiss_desktop_notification_popup(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.NOTIFICATION_NOT_NOW)).click()
            print("✅ Dismissed desktop notification popup via 'Not Now'.")
            time.sleep(0.5)
        except Exception:
            print("ℹ️ No desktop notification popup appeared.")

    def is_ai_edit_heading_visible(self):
        return self.is_visible(self.PAGE_HEADING)

    def click_create_ai_edit(self):
        try:
            create_btn = self.wait.until(
                EC.element_to_be_clickable(self.CREATE_AI_EDIT_BUTTON)
            )
            print("🧪 Found Create AI Edit button, attempting click...")
            self.driver.execute_script("arguments[0].click();", create_btn)
        except Exception as e:
            print("❌ Could not click 'Create AI Edit':", e)
            self.driver.save_screenshot("click_failed_debug.png")
            with open("page_source_on_failure.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise

    def is_ai_edit_modal_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//h3[contains(text(), 'AI Edit')]")
            ))
            return True
        except:
            return False

    def click_start_ai_edit_button(self):
        self.click(self.START_AI_EDIT_BUTTON)
        print("✅ Clicked 'Start AI Edit' button in the popup")

    def click_browse_clip_library_entry(self):
        try:
            entry = self.wait.until(EC.element_to_be_clickable(self.BROWSE_CLIP_LIBRARY_ENTRY))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", entry)
            time.sleep(0.3)
            self.driver.execute_script("arguments[0].click();", entry)
            print("✅ Clicked 'Browse Clip Library' entry.")
        except Exception as e:
            print(f"❌ Failed to click 'Browse Clip Library': {e}")

    def is_browse_clip_modal_visible(self):
        return self.is_visible(self.BROWSE_CLIP_LIBRARY_MODAL_TITLE)

    def click_victory_round_clip(self, timeout=15):
        try:
            print("⏳ Waiting for 'Victory round - 2x' clip to be clickable...")
            clip = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.VICTORY_CLIP)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", clip)
            time.sleep(0.5)
            clip.click()
            print("✅ Clicked 'Victory round - 2x' clip.")
        except Exception as e:
            print(f"❌ Failed to click 'Victory round - 2x' clip: {e}")

    def click_confirm_button(self):
        try:
            confirm_btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
            self.scroll_into_view(confirm_btn)
            confirm_btn.click()
            print("✅ Clicked 'Confirm' button")
        except Exception as e:
            print(f"❌ Failed to click 'Confirm' button: {e}")

    def is_ai_edit_studio_loading_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.AI_EDIT_STUDIO_LOADING_TEXT))
        except Exception as e:
            print(f"❌ 'Loading AI Edit Studio' not visible: {e}")
            return False

    def wait_and_click_generate_ai_edit(self, timeout=20):
        try:
            print(f"⏳ Waiting up to {timeout} seconds for 'Generate AI Edit' button...")
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.GENERATE_AI_EDIT_BUTTON)
            )
            self.scroll_into_view(button)
            self.driver.execute_script("arguments[0].click();", button)
            print("✅ Clicked 'Generate AI Edit' button.")
        except Exception as e:
            print(f"❌ Failed to click 'Generate AI Edit': {e}")

    def is_generating_ai_edit_visible(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.GENERATING_AI_EDIT_TEXT)
            )
            print("✅ 'Generating AI Edit' text is visible.")
            return True
        except Exception as e:
            print(f"❌ 'Generating AI Edit' text not found within {timeout} seconds: {e}")
            return False

    def is_victory_result_visible(self, timeout=15):
        try:
            time.sleep(5)  # Delay before checking
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.VICTORY_RESULT_TITLE)
            )
            print("✅ 'Victory round - 2x' result is visible in the AI Edit list.")
            return True
        except Exception as e:
            print(f"❌ 'Victory round - 2x' result not found: {e}")
            return False
