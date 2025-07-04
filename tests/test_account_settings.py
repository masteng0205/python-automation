from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_settings_page import AccountSettingsPage

def test_navigate_to_account_settings():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://eklipse.gg/")
    print("🟢 Browser launched and navigated to https://eklipse.gg/")

    try:
        # Login flow
        LandingPage(driver).click_sign_in()
        login = LoginPage(driver)
        assert login.is_welcome_text_visible()
        login.login("averio.matsu@gmail.com", "Testing12")

        home = HomePage(driver)
        home.wait_for_home()
        home.handle_skip_popup()
        print("✅ Logged in and skipped intro popup")

        # Navigate to Account Settings
        settings = AccountSettingsPage(driver)
        settings.open_account_settings()

        # Assert the Account Settings page heading is visible
        assert settings.is_account_settings_page_displayed()
        print("🎉 TEST CASE PASSED: Account Settings page heading is visible.")

    finally:
        driver.quit()
        print("🧹 Browser closed.")
