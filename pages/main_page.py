from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class MainPage:
    def __init__(self, driver):
        """
        конструктор класса MainPage
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    @allure.step("открытие страницы сайта")
    def open(self):
        self.driver.get('https://www.chitai-gorod.ru/')
        return self

    @allure.step("ввод значения в поле поиска")
    def search(self, query):
        search_field = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name="search"]'))
        )
        search_field.clear()
        search_field.send_keys(query, Keys.RETURN)
        return self

    @allure.step("получение результата позитивного поиска")
    def get_search_results_text(self):
        results_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 
                            'div[class="catalog-products-total"]'))
        )
        result = results_element.text
        return result

    @allure.step("получение результата негативного поиска")
    def get_no_results_text(self):
        no_results_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 
                                '[class="catalog-stub__title"]'))
        )
        return no_results_element.text
    