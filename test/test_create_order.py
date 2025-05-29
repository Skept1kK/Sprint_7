import allure
import pytest
import helper

class TestCreateOrder:

    @allure.title('Создание заказа c различным выбором цвета ')
    @pytest.mark.parametrize("color", [pytest.param(["BLACK"]),pytest.param(["GREY"]),pytest.param(["BLACK", "GREY"]),pytest.param([]),])
    def test_create_order(self, color):
        color_body = {"color": color}
        response = helper.create_order(color_body)
        assert response.status_code == 201 and response.json()["track"] != None
