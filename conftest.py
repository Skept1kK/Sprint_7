import pytest
import helper


@pytest.fixture
def courier():
    body = helper.generate_courier_data()
    response = helper.create_courier(body)
    assert response.status_code == 201 and response.json() == {'ok': True}
    courier_id = response.json().get('id')
    yield courier_id

    if courier_id:
        helper.delete_courier(courier_id)