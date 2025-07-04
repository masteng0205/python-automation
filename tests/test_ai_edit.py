from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.ai_edit_page import AIEditPage

def test_open_ai_edit_page():
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

        # Wait for home page
        home = HomePage(driver)
        home.wait_for_home()
        home.handle_skip_popup()
        print("✅ Logged in and skipped popup")

        # Click 'Edits' (AI Edit) menu
        home.click_ai_edit_menu()

        ai_edit = AIEditPage(driver)
        ai_edit.dismiss_desktop_notification_popup()
        ai_edit.accept_cookie_popup_if_present()
        ai_edit.close_onboarding_popup_if_present()

        assert ai_edit.is_ai_edit_heading_visible(), "❌ AI Edit heading not found"
        print("✅ AI Edit page loaded successfully")

        print("Page title:", driver.title)
        print("Current URL:", driver.current_url)
        print("Page heading:", driver.find_element(By.TAG_NAME, "h2").text)
        driver.save_screenshot("ai_edit_debug_before_click.png")

        # Click 'Create AI Edit' button
        ai_edit.click_create_ai_edit()

        # Assert modal appears
        assert ai_edit.is_ai_edit_modal_visible(), "❌ AI Edit modal did not appear after clicking 'Create AI Edit'"
        print("✅ AI Edit modal appeared")

        # Click 'Start AI Edit' in the popup modal
        ai_edit.click_start_ai_edit_button()

        # Click 'Browse Clip Library' entry
        ai_edit.click_browse_clip_library_entry()

        # Assert modal is visible
        assert ai_edit.is_browse_clip_modal_visible(), "❌ 'Browse Clips for AI Edit' modal not visible"
        print("✅ 'Browse Clips for AI Edit' modal appeared successfully")

        # Click Video Container under 1 minutes
        ai_edit.click_victory_round_clip()

        # Click Confirm button
        ai_edit.click_confirm_button()

        # Assert Loading Statement
        assert ai_edit.is_ai_edit_studio_loading_visible(), "❌ 'Loading AI Edit Studio' did not appear"
        print("⏳ 'Loading AI Edit Studio' appeared successfully")

        # Click Generate AI Edit button
        ai_edit.wait_and_click_generate_ai_edit()

        # Assert Generating AI Edit Loading
        assert ai_edit.is_generating_ai_edit_visible(), "❌ 'Generating AI Edit' text not visible in time"

        # Click 'Edits' (AI Edit) menu
        home.click_ai_edit_menu()

        # Assert the title is same what we choose
        assert ai_edit.is_victory_result_visible(), "❌ 'Victory round - 2x' result not visible in the list"

    finally:
        # input("⏸️ Test finished — press Enter to close the browser manually...")
        print("🧹 Test completed (browser left open for inspection)")
