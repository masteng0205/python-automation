from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
import time

class StreamsPage(BasePage):
    CLIP_ITEM = (By.CSS_SELECTOR, ".stream-item")
    PAGE_HEADING = (By.XPATH, "//h1[text()='Generate Stream Highlights']")
    COOKIE_ACCEPT = (By.XPATH, "//button[contains(text(), 'Accept') and contains(@onclick, 'acceptCookie')]")
    UNDERSTAND_BUTTON = (By.XPATH, "//button[contains(text(), 'Understand')]")
    NOTIFICATION_NOT_NOW = (By.XPATH, "//div[@class='request-notification-snackbar']//div[@class='div-action' and text()='Not Now']")
    TALKING_VIDEO_TAB = (By.XPATH, "//li[contains(@class, 'tab-list-item') and text()='Talking Video']")
    CLIP_YOUTUBE_HEADER = (By.XPATH, "//h4[text()='Clip a YouTube Video']")
    YOUTUBE_LINK_INPUT = (By.XPATH, "//input[@type='url' and @placeholder='Insert Youtube video link']")
    GET_CLIP_BUTTON = (By.CSS_SELECTOR, "button.btn-get-video-info")
    CLIP_TITLE = (By.XPATH, "//h4[text()='SEHARUSNYA MEREKA TIDAK BERKEMAH DISINI.... Road of Fear']")
    LANGUAGE_DROPDOWN = (By.CSS_SELECTOR, "select.ek-dropdown-list")
    CATEGORY_DROPDOWN = (By.XPATH, "//select[@class='ek-dropdown-list form-control' and not(contains(@class, 'text-capitalize'))]")
    CLIP_NOW_BUTTON = (By.XPATH, "//button[contains(@class, 'ek-primary-button') and text()='Clip Now']")
    UNDERSTOOD_BUTTON = (By.XPATH, "//button[contains(@class, 'ek-primary-button') and text()='Understood']")
    NOT_ENOUGH_CREDITS_HEADING = (By.XPATH, "//h2[text()='Oops, Not Enough Credits!']")

    def is_clip_library_heading_visible(self):
        return self.is_visible(self.PAGE_HEADING)

    def is_clip_displayed(self):
        return self.is_visible(self.CLIP_ITEM)

    def click_first_clip(self):
        clips = self.driver.find_elements(*self.CLIP_ITEM)
        if clips:
            clips[0].click()
            return True
        return False

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

    def click_talking_video_tab(self):
        self.click(self.TALKING_VIDEO_TAB)
        print("✅ Clicked 'Talking Video' tab")

    def is_youtube_clip_heading_visible(self):
        return self.is_visible(self.CLIP_YOUTUBE_HEADER)

    def enter_youtube_video_link(self, url: str):
        self.type(self.YOUTUBE_LINK_INPUT, url)
        print(f"✅ Entered YouTube link: {url}")

    def click_get_clip_button(self):
        self.click(self.GET_CLIP_BUTTON)
        print("✅ Clicked 'Get Clip' button")

    def is_clip_title_visible(self):
        return self.is_visible(self.CLIP_TITLE)

    def select_language(self, lang_value="en"):
        dropdown_element = self.find_element(self.LANGUAGE_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_value(lang_value)  # e.g., "en" for English
        print(f"✅ Language '{lang_value}' selected from dropdown")

    def select_category(self, category_value="Video Podcasts"):
        dropdown_element = self.find_element(self.CATEGORY_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(category_value)
        print(f"✅ Category '{category_value}' selected from dropdown")

    def click_clip_now(self):
        self.click(self.CLIP_NOW_BUTTON)
        print("✅ Clicked 'Clip Now' button")

    def click_understood_popup(self):
        self.click(self.UNDERSTOOD_BUTTON)
        print("✅ Clicked 'Understood' on confirmation popup")

    def is_not_enough_credits_popup_visible(self):
        return self.is_visible(self.NOT_ENOUGH_CREDITS_HEADING)
