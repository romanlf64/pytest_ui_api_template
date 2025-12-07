from pages.main_page import MainPage
import allure
import pytest


@pytest.mark.ui
@allure.title("тестирование поля поиска")
@allure.description("ввод значения на кирилице")
@allure.feature("поле поиска")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_cyrillic(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search('мэттью перри')
    result = main_page.get_search_results_text()
    
    print(f"Результат поиска: {result}")
    with allure.step("проверка результата"):
        assert result == '9 товаров'


@pytest.mark.ui
@allure.title("тестирование поля поиска")
@allure.description("ввод значения на латиннице")
@allure.feature("поле поиска")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_latin(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search('python')
    result = main_page.get_search_results_text()
    
    print(f"Результат поиска: {result}")
    with allure.step("проверка результата"):
        assert result == '346 товаров' 


@pytest.mark.ui
@allure.title("тестирование поля поиска")
@allure.description("ввод значения на кирилице в верхнем регистре")
@allure.feature("поле поиска")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_cyrillic_uppercase(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search('ПИТОН')
    result = main_page.get_search_results_text()
    
    print(f"Результат поиска: {result}")
    with allure.step("проверка результата"):
        assert result == '25 товаров'


@pytest.mark.ui
@allure.title("тестирование поля поиска")
@allure.description("ввод значения на латиннице в верхнем регистре")
@allure.feature("поле поиска")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_latin_uppercase(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search('PYTHON')
    result = main_page.get_search_results_text()
    
    print(f"Результат поиска: {result}")
    with allure.step("проверка результата"):
        assert result == '346 товаров'


@pytest.mark.ui
@allure.title("тестирование поля поиска")
@allure.description("ввод цифр")
@allure.feature("поле поиска")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_numbers(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search('123456789')
    results_text = main_page.get_no_results_text()
    
    print(f"Результат поиска: {results_text}")
    with allure.step("проверка результата"):
        assert results_text == 'Похоже, у нас такого нет'


@pytest.mark.ui
@allure.title("тестирование поля поиска")
@allure.description("ввод китайских иероглифов")
@allure.feature("поле поиска")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_chinese(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.search('冬天去哪玩儿')
    results_text = main_page.get_no_results_text()
    
    print(f"Результат поиска: {results_text}")
    with allure.step("проверка результата"):
        assert results_text == 'Похоже, у нас такого нет'
    