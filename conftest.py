import pytest
import random
import string
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def random_user():
    username = "user_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    email = f"{username}@fmail.com"
    password = "Test12345"
    return {"email": email, "password": password}