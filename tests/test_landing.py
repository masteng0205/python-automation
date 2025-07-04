from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.landing_page import LandingPage

def test_click_sign_in():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://eklipse.gg/")
    print("🟢 Browser launched and navigated to https://eklipse.gg/")

    try:
        landing = LandingPage(driver)
        landing.click_sign_in()
        print("✅ Clicked on 'Sign In' link.")

        assert "login" in driver.current_url.lower() or "signin" in driver.page_source.lower()
        print("🎉 TEST CASE PASSED: Redirected to login page after clicking 'Sign In'.")

    finally:
        driver.quit()
        print("🧹 Browser closed.")
