import requests
import allure
import pytest
import helper
from data import Data
from url import Urls

class TestCourierLogin:

    @allure.title('Возвращение id при успешной аутентификации курьера')
    def test_login_success(self):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, json=Data.correct_data)
        assert response.status_code == 200 and 'id' in response.text

    @pytest.mark.parametrize('incorrect_data', [helper.generate_courier_data(), Data.incorrect_password ])
    @allure.title('Появление ошибки при аутентификации с невалидными данными')
    def test_login_incorrect__data(self,incorrect_data):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, json=incorrect_data)
        assert response.status_code == 404 and response.json() == {'message': 'Учетная запись не найдена'}


    @pytest.mark.parametrize('incomplete_data', [
        {'login': '', 'password': helper.generate_courier_data()['password']},
        {'login': Data.correct_login, 'password': ''},
    ])
    @allure.title('Появление ошибки при аутентификации с пустым полем логина или пароля')
    def test_login_incomplete_data(self,incomplete_data):
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, json=incomplete_data)
        assert response.status_code == 400 and response.json() == {'message': 'Недостаточно данных для входа'}