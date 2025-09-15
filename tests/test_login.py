from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LogInLocators
from config import BASE_URL, LOGIN_URL

class TestLogin:
    def test_login_valid_user(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*LogInLocators.IN_AND_REG_BUTTON).click()
        driver.find_element(*LogInLocators.EMAIL_FIELD).send_keys("mezhov_25@fmail.com")
        driver.find_element(*LogInLocators.PASS_FIELD).send_keys("123456")
        driver.find_element(*LogInLocators.IN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LogInLocators.USER_NAME))

        assert driver.current_url == LOGIN_URL
        assert driver.find_element(*LogInLocators.USER_NAME).is_displayed()
        assert driver.find_element(*LogInLocators.USER_AVATAR).is_displayed()
