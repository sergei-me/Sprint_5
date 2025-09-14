from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LogInLocators

def test_login_valid_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*LogInLocators.IN_AND_REG_BUTTON).click()
    driver.find_element(*LogInLocators.EMAIL_FIELD).send_keys("mezhov_25@fmail.com")
    driver.find_element(*LogInLocators.PASS_FIELD).send_keys("123456")
    driver.find_element(*LogInLocators.IN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/login"))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LogInLocators.USER_NAME))

    assert driver.current_url == "https://qa-desk.stand.praktikum-services.ru/login"
    assert driver.find_element(*LogInLocators.USER_NAME).is_displayed()
    assert driver.find_element(*LogInLocators.USER_AVATAR).is_displayed()

    # driver.quit() - не нужен, так как есть в фикстуре
