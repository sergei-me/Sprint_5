from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators

class LogOutLocators(BaseLocators):
    IN_BUTTON = (By.XPATH, '//button[contains(@class,"buttonPrimary") and text()="Войти"]')
    OUT_BUTTON = (By.CSS_SELECTOR, "div.columnSmall button.spanGlobal")