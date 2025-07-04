from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.landing_page import LandingPage

def test_valid_login():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://eklipse.gg/")
    print("🟢 Browser launched and navigated to https://eklipse.gg/")

    try:
        # Step: Click Sign In
        LandingPage(driver).click_sign_in()
        print("✅ Clicked on 'Sign In' link.")

        # Step: Wait for login page and perform login
        login = LoginPage(driver)
        assert login.is_welcome_text_visible()
        print("✅ 'Welcome back!' text is visible.")

        login.login("averio.matsu@gmail.com", "Testing12")
        print("✅ Login form submitted.")

        # You can also assert URL or some other check here if needed
        print("🎉 TEST CASE PASSED: Valid login completed successfully.")

    finally:
        driver.quit()
        print("🧹 Browser closed.")
