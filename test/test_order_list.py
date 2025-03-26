import requests
import allure
from url import Urls


class TestOrdersList:

    @allure.title('Получения списка заказов')
    def test_orders_list(self):
        response = requests.get(Urls.BASE_URL + Urls.ORDER_CREATE)
        orders = response.json().get('orders',[])
        assert isinstance(orders, list) and 'id' in orders[0]