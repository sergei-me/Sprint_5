from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from locators.logout_locators import LogOutLocators
from config import BASE_URL

def is_not_visible(driver, locator):
    try:
        return not driver.find_element(*locator).is_displayed()
    except NoSuchElementException:
        return True
class TestLogOut:
    def test_logout_valid_user(sekf, driver):
        driver.get(BASE_URL)

        driver.find_element(*LogOutLocators.IN_AND_REG_BUTTON).click()
        driver.find_element(*LogOutLocators.EMAIL_FIELD).send_keys("mezhov_25@fmail.com")
        driver.find_element(*LogOutLocators.PASS_FIELD).send_keys("123456")
        driver.find_element(*LogOutLocators.IN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LogOutLocators.OUT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LogOutLocators.IN_AND_REG_BUTTON))

        assert is_not_visible(driver, LogOutLocators.USER_NAME)
        assert is_not_visible(driver, LogOutLocators.USER_AVATAR)
        assert driver.find_element(*LogOutLocators.IN_AND_REG_BUTTON).is_displayed()
