from selenium.webdriver.common.by import By

class BaseLocators:
    IN_AND_REG_BUTTON = (By.XPATH, '//button[contains(@class,"buttonSecondary") and text()="Вход и регистрация"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PASS_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    