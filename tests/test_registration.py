from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_locators import RegistrationLocators
from config import BASE_URL, REGISTRATION_URL

class TestRegistration:
    def test_reg_new_user(self, driver, random_user):
        driver.get(BASE_URL)

        driver.find_element(*RegistrationLocators.IN_AND_REG_BUTTON).click()
        driver.find_element(*RegistrationLocators.NO_ACC_BUTTON).click()
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(random_user["email"])
        driver.find_element(*RegistrationLocators.PASS_FIELD).send_keys(random_user["password"])
        driver.find_element(*RegistrationLocators.REPEAT_PASS_FIELD).send_keys(random_user["password"])
        driver.find_element(*RegistrationLocators.CREATE_ACC_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(REGISTRATION_URL))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegistrationLocators.USER_NAME))

        assert driver.current_url == REGISTRATION_URL
        assert driver.find_element(*RegistrationLocators.USER_NAME).is_displayed()
        assert driver.find_element(*RegistrationLocators.USER_AVATAR).is_displayed()


    def test_error_reg_not_valid_email(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*RegistrationLocators.IN_AND_REG_BUTTON).click()
        driver.find_element(*RegistrationLocators.NO_ACC_BUTTON).click()
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys("mezhov_25fmail.com")
        driver.find_element(*RegistrationLocators.PASS_FIELD).send_keys("123456")
        driver.find_element(*RegistrationLocators.REPEAT_PASS_FIELD).send_keys("123456")
        driver.find_element(*RegistrationLocators.CREATE_ACC_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegistrationLocators.ERROR_MESSAGE))

        assert "Ошибка" in error_message.text

        for field_locator in [
            RegistrationLocators.EMAIL_FIELD,
            RegistrationLocators.PASS_FIELD,
            RegistrationLocators.REPEAT_PASS_FIELD,
        ]:
            field = driver.find_element(*field_locator)
            parent_div = field.find_element("xpath", "./..")
            parent_class = parent_div.get_attribute("class")

        assert "Error" in parent_class


    def test_error_reg_already_exist_user(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*RegistrationLocators.IN_AND_REG_BUTTON).click()
        driver.find_element(*RegistrationLocators.NO_ACC_BUTTON).click()
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys("mezhov_25fmail.com")
        driver.find_element(*RegistrationLocators.PASS_FIELD).send_keys("123456")
        driver.find_element(*RegistrationLocators.REPEAT_PASS_FIELD).send_keys("123456")
        driver.find_element(*RegistrationLocators.CREATE_ACC_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegistrationLocators.ERROR_MESSAGE))

        assert "Ошибка" in error_message.text

        for field_locator in [
            RegistrationLocators.EMAIL_FIELD,
            RegistrationLocators.PASS_FIELD,
            RegistrationLocators.REPEAT_PASS_FIELD,
        ]:
            field = driver.find_element(*field_locator)
            parent_div = field.find_element("xpath", "./..")
            parent_class = parent_div.get_attribute("class")

        assert "Error" in parent_class
