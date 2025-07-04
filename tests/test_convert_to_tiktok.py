from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.convert_to_tiktok_page import ConvertToTikTokPage
import time

def test_convert_clip_to_tiktok():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://eklipse.gg/")
    print("🟢 Browser launched and navigated to https://eklipse.gg/")

    try:
        BasePage(driver).accept_cookies_if_present()

        LandingPage(driver).click_sign_in()
        login = LoginPage(driver)
        assert login.is_welcome_text_visible()
        login.login("averio.matsu@gmail.com", "Testing12")

        home = HomePage(driver)
        home.wait_for_home()
        home.handle_skip_popup()
        print("✅ Logged in and skipped popup")

        convert = ConvertToTikTokPage(driver)
        convert.go_to_edited_clips()
        assert convert.is_edited_clips_heading_visible()

        convert.dismiss_desktop_notification_popup()
        convert.close_onboarding_popup_if_present()

        convert.click_convert_to_tiktok()
        assert convert.is_add_clip_text_visible()
        print("✅ 'Add Clip to Start' screen is visible.")

        twitch_clip_url = "https://clips.twitch.tv/AthleticEnjoyableBatteryDeIlluminati-zF_UJug9VzVrpdJp?tt_content=url&tt_medium=clips_api"
        convert.paste_clip_url(twitch_clip_url)
        print("✅ Pasted Twitch clip URL.")

        convert.click_get_clip()

        for _ in range(5):
            convert.click_button_by_text("Continue")
            time.sleep(1)

        convert.click_button_by_text("Export")
        assert convert.is_export_confirmation_visible()
        print("🎉 TEST CASE PASSED: Export confirmation modal is visible.")

        convert.click_confirm_export()
        print("🎉 TEST CASE PASSED: Export confirmed successfully.")

        assert convert.is_export_success_visible()
        print("🎉 TEST CASE PASSED: Export success confirmed with 'Thank you' message.")

        convert.click_got_it()

        convert.click_back_to_edited_clips()

        # 🔄 Refresh page to ensure UI is ready
        driver.refresh()
        time.sleep(3)

        assert convert.is_converted_clip_title_visible("TECTONE TRUE")
        print("✅ TEST CASE PASSED: Converted clip title 'TECTONE TRUE' is visible.")

        convert.click_more_options_for_clip("TECTONE TRUE")
        print("✅ Successfully clicked 3-dot menu for the clip.")

        assert convert.is_delete_option_visible(), "❌ Delete option not visible after clicking 3-dot menu."
        print("✅ Delete option is visible.")

        convert.click_delete_option()
        convert.confirm_delete_clip()
        assert convert.is_clip_deleted_successfully()
        print("🧹 Clip deleted successfully and confirmed with 'Continue'.")

    finally:
        driver.quit()
        print("🧹 Browser closed.")
