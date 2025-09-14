from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators

class RegistrationLocators(BaseLocators):
    NO_ACC_BUTTON = (By.XPATH, '//button[contains(@class,"buttonSecondary") and text()="Нет аккаунта"]')
    REPEAT_PASS_FIELD = (By.CSS_SELECTOR, "input[name='submitPassword']")
    CREATE_ACC_BUTTON = (By.XPATH, '//button[contains(@class,"buttonPrimary") and text()="Создать аккаунт"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'span.input_span__yWPqB')
