from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.streams_page import StreamsPage

def test_open_clip_library():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://eklipse.gg/")
    print("🟢 Browser launched and navigated to https://eklipse.gg/")

    try:
        # Login
        LandingPage(driver).click_sign_in()
        login = LoginPage(driver)
        assert login.is_welcome_text_visible()
        login.login("averio.matsu@gmail.com", "Testing12")

        # Wait for home page
        home = HomePage(driver)
        home.wait_for_home()
        home.handle_skip_popup()
        print("✅ Logged in and skipped popup")

        # Click Clip Library (Streams)
        home.click_clip_library()
        print("✅ Navigated to Clip Library")

        # Assert the page heading
        streams = StreamsPage(driver)
        assert streams.is_clip_library_heading_visible(), "❌ 'Generate Stream Highlights' heading not found"
        print("✅ 'Generate Stream Highlights' heading is visible")

        # Accept cookie
        BasePage(driver).accept_cookies_if_present()

        # Dismiss desktop notification popup
        streams.dismiss_desktop_notification_popup()
        streams.close_onboarding_popup_if_present()

        # Click "Talking Video" tab
        streams.click_talking_video_tab()

        # Assert the 'Clip a YouTube Video' heading is visible
        assert streams.is_youtube_clip_heading_visible(), "❌ 'Clip a YouTube Video' heading not found"
        print("✅ 'Clip a YouTube Video' heading is visible")

        # Enter YouTube link
        youtube_url = "https://www.youtube.com/watch?v=bXBn7v8OxPw"
        streams.enter_youtube_video_link(youtube_url)

        # Click Get Clip
        streams.click_get_clip_button()

        # Assert the clip title appears
        assert streams.is_clip_title_visible(), "❌ Clip title not visible after clicking 'Get Clip'"
        print("✅ Clip title 'SEHARUSNYA MEREKA TIDAK BERKEMAH DISINI.... Road of Fear' is visible")

        # Select language from dropdown
        streams.select_language("en")

        # Select category
        streams.select_category("Video Podcasts")

        # Click 'Clip Now' to submit
        streams.click_clip_now()

        # Click 'Understood' on confirmation popup
        streams.click_understood_popup()

        # Assert 'Not Enough Credits' popup appears
        assert streams.is_not_enough_credits_popup_visible(), "❌ 'Not Enough Credits' popup did not appear"
        print("✅ 'Oops, Not Enough Credits!' popup is visible")

    finally:
        driver.quit()
        print("🧹 Browser closed.")
