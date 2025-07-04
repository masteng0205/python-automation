from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class ConvertToTikTokPage(BasePage):
    EDIT_TAB = (By.XPATH, "//a[@class='sidebar-link' and @href='/edited-clip/ai-edit']")
    EDITED_CLIPS = (By.XPATH, "//a[@class='sidebar-submenu-link' and @href='/edited-clip/edited-by-you']")
    EDITED_CLIPS_HEADING = (By.XPATH, "//h2[normalize-space()='Edited Clips']")
    CONVERT_BUTTON = (By.XPATH, "//button[contains(text(), 'Convert to TikTok')]")
    ADD_CLIP_TEXT = (By.XPATH, "//p[normalize-space()='Add Clip to Start']")
    CLIP_INPUT = (By.XPATH, "//input[@placeholder='Paste Twitch or Kick clips URL here']")
    UNDERSTAND_BUTTON = (By.XPATH, "//button[contains(text(), 'Understand')]")
    COOKIE_ACCEPT = (By.XPATH, "//button[contains(text(), 'Accept') and contains(@onclick, 'acceptCookie')]")
    NOTIFICATION_NOT_NOW = (By.XPATH, "//div[@class='request-notification-snackbar']//div[@class='div-action' and text()='Not Now']")
    GET_CLIP_BUTTON = (By.CLASS_NAME, "css-ar65o0")
    CONTINUE_BUTTON = (By.XPATH, "//button[.='Continue']")
    CONFIRMATION_HEADING = (By.XPATH, "//div[normalize-space()='Are you sure you want to export?']")
    CONFIRM_EXPORT_BUTTON = (By.XPATH, "//button[normalize-space()='Confirm Export']")
    EXPORT_SUCCESS_HEADING = (By.XPATH, "//div[normalize-space()='Thank you']")
    GOT_IT_BUTTON = (By.XPATH, "//button[normalize-space()='Got it!']")
    CONVERSION_STATUS_HEADING = (By.XPATH, "//div[contains(@class, 'box-header--title') and contains(text(), 'Convert to TikTok / Shorts / Reels Status')]")
    BACK_TO_EDITED_CLIPS_BTN = (By.XPATH, "//a[contains(@class, 'btn-primary') and contains(text(), 'Back to Convert to TikTok')]")
    CONVERTED_TITLE = (By.XPATH, "//div[@class='title' and contains(text(), 'TECTONE TRUE')]")
    MORE_OPTIONS_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-link') and .//i[contains(@class, 'nic-more-tools')]]")
    DELETE_OPTION = (By.XPATH, "//a[starts-with(@id, 'delete-') and text()='Delete']")
    DELETE_CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'swal2-confirm') and text()='Yes']")
    DELETE_SUCCESS_CONTINUE_BUTTON = (By.XPATH, "//button[contains(@class, 'swal2-confirm') and text()='Continue']")

    def go_to_edited_clips(self):
        self.click(self.EDIT_TAB)
        print("✅ Clicked 'Edits' tab.")

        self.click(self.EDITED_CLIPS)
        print("✅ Clicked 'Edited Clips' submenu.")

        self.close_onboarding_popup_if_present()
        self.accept_cookie_popup_if_present()

    def is_edited_clips_heading_visible(self):
        return self.is_visible(self.EDITED_CLIPS_HEADING)

    def click_convert_to_tiktok(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))
        self.click(self.CONVERT_BUTTON)
        print("✅ Clicked 'Convert to TikTok / Shorts / Reels' button.")

    def close_onboarding_popup_if_present(self):
        try:
            popup_button = self.wait.until(EC.element_to_be_clickable(self.UNDERSTAND_BUTTON))
            popup_button.click()
            print("✅ Closed onboarding popup with 'Understand' button.")
        except Exception:
            print("ℹ️ No onboarding popup appeared.")

    def accept_cookie_popup_if_present(self):
        try:
            accept_btn = self.wait.until(EC.element_to_be_clickable(self.COOKIE_ACCEPT))
            accept_btn.click()
            print("✅ Accepted cookies.")
        except Exception:
            print("ℹ️ Cookie popup not found.")

    def is_add_clip_text_visible(self):
        return self.is_visible(self.ADD_CLIP_TEXT)

    def paste_clip_url(self, clip_url):
        self.type(self.CLIP_INPUT, clip_url)
        print(f"✅ Pasted Twitch clip URL: {clip_url}")

    def dismiss_desktop_notification_popup(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.NOTIFICATION_NOT_NOW)).click()
            print("✅ Dismissed desktop notification popup via 'Not Now'.")
            time.sleep(0.5)
        except Exception:
            print("ℹ️ No desktop notification popup appeared.")

    def click_get_clip(self):
        get_clip_btn = self.wait.until(EC.element_to_be_clickable(self.GET_CLIP_BUTTON))
        get_clip_btn.click()
        print("✅ Clicked 'Get Clip' button.")
        time.sleep(10)

    def click_continue_button(self):
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_btn.click()
        print("✅ Clicked 'Continue' button.")

    def click_button_by_text(self, button_text):
        button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//button[normalize-space()='{button_text}']")
        ))
        button.click()
        print(f"✅ Clicked '{button_text}' button.")

    def is_export_confirmation_visible(self):
        try:
            return self.is_visible(self.CONFIRMATION_HEADING)
        except Exception:
            return False

    def click_confirm_export(self):
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_EXPORT_BUTTON))
        confirm_btn.click()
        print("✅ Clicked 'Confirm Export' button.")

    def is_export_success_visible(self):
        try:
            return self.is_visible(self.EXPORT_SUCCESS_HEADING)
        except Exception:
            return False

    def click_got_it(self):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "MuiBackdrop-root")))
            buttons = self.driver.find_elements(*self.GOT_IT_BUTTON)
            print(f"🔍 Found {len(buttons)} 'Got it!' button(s).")
            for btn in buttons:
                if btn.is_displayed() and btn.is_enabled():
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                    time.sleep(0.5)
                    self.driver.execute_script("arguments[0].click();", btn)
                    print("✅ Clicked visible 'Got it!' button using JavaScript.")
                    return
            print("❌ No visible and enabled 'Got it!' button was found to click.")
        except Exception as e:
            print(f"❌ Exception while trying to click 'Got it!': {e}")

    def is_conversion_status_visible(self):
        return self.is_visible(self.CONVERSION_STATUS_HEADING)

    def click_back_to_edited_clips(self):
        self.click(self.BACK_TO_EDITED_CLIPS_BTN)
        print("🔙 Clicked 'Back to Convert to TikTok / Shorts / Reels'.")

    def is_converted_clip_title_visible(self, title_text):
        locator = (By.XPATH, f"//div[@class='title' and contains(normalize-space(), '{title_text}')]")
        return self.is_visible(locator)

    def click_more_options_for_clip(self, title_text="TECTONE TRUE"):
        print(f"🔍 Looking for clip card with title '{title_text}'...")
        try:
            containers = self.driver.find_elements(By.CLASS_NAME, "list-item")
            for container in containers:
                title_element = container.find_element(By.CLASS_NAME, "title")
                if title_text in title_element.text:
                    print("✅ Found matching clip container.")
                    try:
                        more_btn = container.find_element(By.XPATH, ".//button[contains(@class, 'btn-link') and .//i[contains(@class, 'nic-more-tools')]]")
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", more_btn)
                        time.sleep(0.5)
                        self.wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[contains(@class, 'btn-link') and .//i[contains(@class, 'nic-more-tools')]]")))
                        more_btn.click()
                        print("✅ Clicked 3-dot 'more options' button.")
                        return
                    except Exception as click_error:
                        print(f"❌ Could not click 3-dot menu: {click_error}")
            print(f"❌ No matching clip container with title: {title_text}")
        except Exception as e:
            print(f"❌ Exception while searching for clip containers: {e}")

    def is_delete_option_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DELETE_OPTION))
            return True
        except:
            return False

    def click_delete_option(self):
        try:
            delete_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_OPTION))
            delete_btn.click()
            print("🗑️ Clicked 'Delete' option.")
        except Exception as e:
            print(f"❌ Failed to click 'Delete' option: {e}")

    def confirm_delete_clip(self):
        try:
                confirm_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_CONFIRM_BUTTON))
                confirm_btn.click()
                print("✅ Clicked 'Yes' to confirm deletion.")
        except Exception as e:
                print(f"❌ Failed to confirm deletion: {e}")

    def is_clip_deleted_successfully(self):
        try:
            continue_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_SUCCESS_CONTINUE_BUTTON))
            continue_btn.click()
            print("✅ Clicked 'Continue' after successful deletion.")
            return True
        except Exception as e:
            print(f"❌ Clip deletion success message not handled: {e}")
            return False