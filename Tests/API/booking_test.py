import requests
import random


class TestBooking:
    base_url = "https://restful-booker.herokuapp.com/"

# TODO Починить нестабильный тест. Почему то иногда падает.
    def test_get_by_id(self):
        # Arrange
        random_id = random.randint(100, 1000)
        url = self.base_url + f"booking/{random_id}"

        # Act
        response = requests.get(url)
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert isinstance(data["firstname"], str)
        assert isinstance(data["lastname"], str)
        assert isinstance(data["totalprice"], int)
        assert isinstance(data["depositpaid"], bool)
        assert isinstance(data["additionalneeds"], str)

# TODO Техдолг, нужно дописать тесты
    def test_create_booking(self):
        pass
        # https://restful-booker.herokuapp.com/apidoc/index.html

    def test_delete_booking(self):
        pass
        # https://restful-booker.herokuapp.com/apidoc/index.html

    # Со звёздочкой, сделать использование токена в посте