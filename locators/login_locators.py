from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators

class LogInLocators(BaseLocators):
    IN_BUTTON = (By.XPATH, '//button[contains(@class,"buttonPrimary") and text()="Войти"]')
