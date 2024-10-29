import unittest
import requests

BASE_URL = "http://localhost:5000/api/v1"
url_cake = f"{BASE_URL}/cakes"
url_bakery = f"{BASE_URL}/bakeries"

class TestPOST(unittest.TestCase):
    def test_cakes_post(self):
        data = {
            "name": "Cool",
            "flavor": "Vanila",
            "price": 8,
            "available": True
        }
        response = requests.post(url_cake, json=data)
        response_data = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get("name"), data["name"])
        self.assertEqual(response_data.get("flavor"), data["flavor"])
        self.assertEqual(response_data.get("available"), data["available"])

    def test_bakery_post(self):
        data = {
            "name": "Best Bakery",
            "location": "Av. Vsevolod, 19-21",
            "rating": 11
        }
        response = requests.post(url_bakery, json=data)
        response_data = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get("name"), data["name"])
        self.assertEqual(response_data.get("location"), data["location"])
        self.assertEqual(float(response_data.get("rating")), data["rating"])