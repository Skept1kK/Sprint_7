import requests
from faker import Faker
import allure
from url import Urls


fake = Faker()
fakeRU = Faker(locale='ru_RU')


@allure.step("Генерация данных для курьера в сервисе 'Самокат'")
def generate_courier_data():
    return {
        "login": fake.user_name(),
        "password": fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
        "firstName": fakeRU.first_name()
    }


@allure.step("Создание курьера в сервисе 'Самокат'")
def create_courier(body):
    response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, json=body)
    return response


@allure.step("Создание заказа в сервисе 'Самокат'")
def create_order(order_body):
    response = requests.post(Urls.BASE_URL + Urls.ORDER_CREATE, json=order_body)
    return response


@allure.step("Удаление курьера в сервисе 'Самокат'")
def delete_courier(courier_id):
    response = requests.delete(Urls.BASE_URL + Urls.DELETE_COURIER + str(courier_id))
    return response