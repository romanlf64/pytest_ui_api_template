import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_api import CartAPI, BASE_URL, TOKEN 
import allure


@pytest.fixture
def driver():
    with allure.step("открыть и настроить браузер"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.implicitly_wait(7)
        browser.maximize_window()
        yield browser
    with allure.step("закрыть браузер"):    
        browser.quit()


@pytest.fixture
def cart_api():
    return CartAPI(BASE_URL, TOKEN)
    