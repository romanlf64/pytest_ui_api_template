import requests
import allure


BASE_URL = "https://web-agr.chitai-gorod.ru"
TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyNzI0NTk3LCJpYXQiOjE3NjUxMTAwODYsImV4cCI6MTc2NTExMzY4NiwidHlwZSI6MjAsImp0aSI6IjAxOWFmOGMyLTdiMzctN2MzNC1iZTE4LWRkNDA3NDM2YzQ0OSIsInJvbGVzIjoxMH0.ALPEZ5kDJI4OQZkkwGUAdYFcg7zDaXble4KXtbOkPq4'


class CartAPI:
    def __init__(self, base_url, token):
        """
        конструктор класса CartAPI
        """
        self.base_url = base_url
        self.headers = {
            'accept': 'application/json',
            'authorization': token,
            'content-type': 'application/json'
        }

    @allure.step("добавление товара в корзину")
    def add_item(self, item_id):
        payload = {"id": item_id}
        resp = requests.post(self.base_url + '/web/api/v1/cart/product', 
                             headers=self.headers, json=payload)
        return resp

    @allure.step("просмотр корзины")
    def view_cart(self):
        resp = requests.get(self.base_url + '/web/api/v1/cart', 
                            headers=self.headers)
        return resp

    @allure.step("очистка корзины")
    def clear_cart(self):
        resp = requests.delete(self.base_url + '/web/api/v1/cart', 
                               headers=self.headers)
        return resp

    @allure.step("добавление товара в корзину с негативными данными")
    def add_item_custom(self, payload):
        resp = requests.post(self.base_url + '/web/api/v1/cart/product', 
                             headers=self.headers, json=payload)
        return resp
    