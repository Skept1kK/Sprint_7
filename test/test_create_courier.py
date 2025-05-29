import allure
import requests
import helper
from url import Urls
from conftest import courier

class TestCourier:
    @allure.title("Проверка создания курьера")
    def test_create_courier(self,courier):
        body = helper.generate_courier_data()
        response = helper.create_courier(body)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_second_login (self,courier):
        body = helper.generate_courier_data()
        helper.create_courier(body)
        payload = {
            'login': body['login'],
            'password': helper.generate_courier_data()['password'],
            'firstName': helper.generate_courier_data()['firstName']
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, json=payload)
        assert response.status_code == 409 and response.json() == {'message': 'Этот логин уже используется'}


    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self,courier):
        payload = {
            'login': "",
            'password': helper.generate_courier_data()['password'],  # Генерация нового пароля
            'firstName': helper.generate_courier_data()['firstName']  # Генерация нового имени
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, json=payload)
        assert response.status_code == 400 and response.json() == {'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self,courier):
        payload = {
            'login': helper.generate_courier_data()['login'],
            'password': "",
            'firstName': helper.generate_courier_data()['firstName']
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, json=payload)
        assert response.status_code == 400 and response.json() == {'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title("Создание курьера без имени")
    def test_create_courier_without_name(self,courier):
        payload = {
            'login': helper.generate_courier_data()['login'],
            'password': helper.generate_courier_data()['password'],
            'firstName': ""
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, json=payload)
        assert response.status_code == 400 and response.json() == {'message': 'Недостаточно данных для создания учетной записи'}