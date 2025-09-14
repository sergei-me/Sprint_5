from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators

class UnauthorizedUserCreateAdLocators(BaseLocators):
    CREATE_AD_BUTTON = (By.XPATH, '//button[contains(@class,"buttonPrimary") and text()="Разместить объявление"]')
    HEADER_AUTH_MESSAGE = (By.CSS_SELECTOR, 'div.popUp_titleRow__M7tGg h1.h1')

class AuthorizedUserCreateAdLocators(BaseLocators):
    IN_BUTTON = (By.XPATH, '//button[contains(@class,"buttonPrimary") and text()="Войти"]')
    CREATE_AD_BUTTON = (By.XPATH, '//button[contains(@class,"buttonPrimary") and text()="Разместить объявление"]')
    NAME_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    CATEGORY_GOODS_MENU_BUTTON = (By.XPATH, "//button[contains(@class,'dropDownMenu_arrowDown__pfGL1')][1]")
    CATEGORY_AVTO_BUTTON = (By.XPATH, "//div[contains(@class,'dropDownMenu_hidden__')]/button/span[text()='Авто']")
    CONDITION_RADIOBUTTON = (By.CSS_SELECTOR, 'input[value="Б/У"]')
    CATEGORY_CITY_MENU_BUTTON = (By.XPATH, "//button[contains(@class,'dropDownMenu_arrowDown__pfGL1')][2]")
    CITY_NOVOSIBIRSK_BUTTON = (By.XPATH, "//div[contains(@class,'dropDownMenu_hidden__')]/button/span[text()='Новосибирск']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'textarea[name="description"]')
    PRICE_FIELD = (By.CSS_SELECTOR, 'input[name="price"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(@class,"buttonPrimary") and text()="Опубликовать"]')
    MY_PROFILE = (By.CSS_SELECTOR, 'h1.h1.zeroMargin')
    MY_NEW_AD_CARD = (By.CSS_SELECTOR, 'img.picture[alt="Продается Автомобиль"]')
