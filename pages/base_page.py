from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_url(self, text):
        self.wait.until(EC.url_contains(text))

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def accept_cookies_if_present(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(text(), 'Accept') and contains(@onclick, 'acceptCookie')]"
            )))
            cookie_button.click()
            print("✅ Cookie popup accepted.")
        except Exception:
            print("ℹ️ No cookie popup appeared.")

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
