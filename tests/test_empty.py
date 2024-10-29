import unittest
import requests

BASE_URL = "http://localhost:5000/api/v1"

class TestEmpty(unittest.TestCase):
    url_cake = f"{BASE_URL}/cakes"
    url_bakery = f"{BASE_URL}/bakeries"

    def test_cakes_get_empty(self):
        response = requests.get(self.url_cake)
        response_data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data, [])

    def test_cakes_id_get_empty(self):
        response = requests.get(f"{self.url_cake}/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {})

    def test_bakery_get_empty(self):
        response = requests.get(self.url_bakery)
        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_bakery_id_get_empty(self):
        response = requests.get(f"{self.url_bakery}/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {})

    def test_bakery_cakes_get_empty(self):
        response = requests.get(f"{self.url_bakery}/1/cakes")
        response_data = response.json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["error"], "Bakery was not found")