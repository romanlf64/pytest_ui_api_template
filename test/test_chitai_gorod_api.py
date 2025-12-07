import allure
import pytest


@pytest.mark.api
@allure.title("тестирование корзины")
@allure.description("добавление товара в козину по id")
@allure.feature("корзина")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart(cart_api):
    resp = cart_api.add_item(3001530)
    with allure.step("проверка статус-кода"):
        assert resp.status_code == 200


@pytest.mark.api
@allure.title("тестирование корзины")
@allure.description("просмотр корзины")
@allure.feature("корзина")
@allure.severity(allure.severity_level.CRITICAL)
def test_view_cart(cart_api):
    resp = cart_api.view_cart()
    with allure.step("проверка статус-кода"):
        assert resp.status_code == 200


@pytest.mark.api
@allure.title("тестирование корзины")
@allure.description("очистка корзины")
@allure.feature("корзина")
@allure.severity(allure.severity_level.CRITICAL)
def test_clear_cart(cart_api):
    resp = cart_api.clear_cart()
    with allure.step("проверка статус-кода"):
        assert resp.status_code == 204


@pytest.mark.api
@allure.title("тестирование корзины")
@allure.description("добавление товара в корзину с ID равным 0")
@allure.feature("корзина")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart_negative_1(cart_api):
    resp = cart_api.add_item(0)
    with allure.step("проверка статус-кода"):
        assert resp.status_code == 422


@pytest.mark.api
@allure.title("тестирование корзины")
@allure.description("добавление товара в корзину с title вместо id")
@allure.feature("корзина")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart_negative_2(cart_api):
    payload = {"title": "Почти серьезно... И письма к маме"}
    resp = cart_api.add_item_custom(payload)
    with allure.step("проверка статус-кода"):
        assert resp.status_code == 422
