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

    def test_create_token(self):
        # Arrange
        url = self.base_url + f"auth"
        headers = {'Content-Type': 'application/json'}
        payload = {"username": "admin", "password": "password123"}

        # Act
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        # Assert
        assert isinstance(data["token"], str)
        assert len(data["token"]) > 10
        assert response.status_code == 200

# TODO Техдолг, нужно дописать тест
    def test_create_booking(self):
        pass
        # https://restful-booker.herokuapp.com/apidoc/index.html
