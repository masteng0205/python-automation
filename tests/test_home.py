from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_full_login_flow_and_skip_popup():
    # Setup WebDriver
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://eklipse.gg/")

    try:
        print("🟢 Browser launched and navigated to https://eklipse.gg/")

        # Page Object Instantiation
        landing = LandingPage(driver)
        login = LoginPage(driver)
        home = HomePage(driver)

        # Landing Page: click Sign In
        landing.click_sign_in()
        print("✅ Clicked on 'Sign In' link.")

        # Login Page: check Welcome text and login
        assert login.is_welcome_text_visible()
        print("✅ 'Welcome back!' text is visible.")

        login.login("averio.matsu@gmail.com", "Testing12")
        print("✅ Login form submitted.")

        # Home Page: wait for redirect and check elements
        home.wait_for_home()
        assert "home" in driver.current_url.lower()
        print("✅ Redirected to home page.")

        # Handle "Skip for now" popup if present
        home.handle_skip_popup()
        print("✅ Skip popup handled (if present).")

        print("🎉 TEST CASE PASSED: Full login flow and popup handling completed successfully.")

    finally:
        driver.quit()
        print("🧹 Browser closed.")
