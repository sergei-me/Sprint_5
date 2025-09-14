from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.ad_locators import UnauthorizedUserCreateAdLocators
from locators.ad_locators import AuthorizedUserCreateAdLocators

def click_with_retry(driver, locator, retries=3, wait=5):
    for _ in range(retries):
        try:
            element = WebDriverWait(driver, wait).until(EC.visibility_of_element_located(locator))
            WebDriverWait(driver, wait).until(EC.element_to_be_clickable(locator))
            element.click()
            break
        except (StaleElementReferenceException, TimeoutException):
            pass

def test_add_ad_unauth_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*UnauthorizedUserCreateAdLocators.CREATE_AD_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(UnauthorizedUserCreateAdLocators.HEADER_AUTH_MESSAGE))

    assert driver.find_element(*UnauthorizedUserCreateAdLocators.HEADER_AUTH_MESSAGE).is_displayed()


def test_add_ad_auth_user(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    click_with_retry(driver, AuthorizedUserCreateAdLocators.IN_AND_REG_BUTTON)
    driver.find_element(*AuthorizedUserCreateAdLocators.EMAIL_FIELD).send_keys("mezhov_25@fmail.com")
    driver.find_element(*AuthorizedUserCreateAdLocators.PASS_FIELD).send_keys("123456")
    driver.find_element(*AuthorizedUserCreateAdLocators.IN_BUTTON).click()

    click_with_retry(driver, AuthorizedUserCreateAdLocators.CREATE_AD_BUTTON)

    WebDriverWait(driver, 10).until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/create-lisiting"))

    driver.find_element(*AuthorizedUserCreateAdLocators.NAME_FIELD).send_keys("Продается Автомобиль")

    click_with_retry(driver, AuthorizedUserCreateAdLocators.CATEGORY_GOODS_MENU_BUTTON)
    click_with_retry(driver, AuthorizedUserCreateAdLocators.CATEGORY_AVTO_BUTTON)
    click_with_retry(driver, AuthorizedUserCreateAdLocators.CONDITION_RADIOBUTTON)
    click_with_retry(driver, AuthorizedUserCreateAdLocators.CATEGORY_CITY_MENU_BUTTON)
    click_with_retry(driver, AuthorizedUserCreateAdLocators.CITY_NOVOSIBIRSK_BUTTON)

    driver.find_element(*AuthorizedUserCreateAdLocators.DESCRIPTION_FIELD).send_keys("Моя самая быстрая ласточка!")
    driver.find_element(*AuthorizedUserCreateAdLocators.PRICE_FIELD).send_keys("1000000")

    click_with_retry(driver, AuthorizedUserCreateAdLocators.SUBMIT_BUTTON)

    click_with_retry(driver, AuthorizedUserCreateAdLocators.USER_AVATAR)

    click_with_retry(driver, AuthorizedUserCreateAdLocators.MY_PROFILE)

    target_card = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthorizedUserCreateAdLocators.MY_NEW_AD_CARD))
    driver.execute_script("arguments[0].scrollIntoView(true);", target_card)
    
    assert target_card.is_displayed()
