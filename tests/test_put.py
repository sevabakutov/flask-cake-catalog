import unittest
import requests

BASE_URL = "http://localhost:5000/api/v1"
url_cake = f"{BASE_URL}/cakes"
url_bakery = f"{BASE_URL}/bakeries"

class TestPUT(unittest.TestCase):
    def test_cake_put(self):
        data = {
            "name": "Updated Cake",
            "flavor": "Chocolate",
            "price": 10,
            "available": False
        }
        res = requests.put(f"{url_cake}/1", json=data)
        res_data = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data.get("name"), data["name"])
        self.assertEqual(res_data.get("flavor"), data["flavor"])
        self.assertEqual(float(res_data.get("price")), data["price"])
        self.assertEqual(res_data.get("available"), data["available"])

    def test_bakery_put(self):
        data = {
            "name": "Updated Bakery",
            "location": "Updated Location",
            "rating": 9.5
        }
        res = requests.put(f"{url_bakery}/1", json=data)
        res_data = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data.get("name"), data["name"])
        self.assertEqual(res_data.get("location"), data["location"])
        self.assertEqual(float(res_data.get("rating")), data["rating"])

    def test_cake_put_nonexistent_id(self):
        data = {
            "name": "Nonexistent Cake",
            "flavor": "Strawberry"
        }
        res = requests.put(f"{url_cake}/999", json=data)
        self.assertEqual(res.status_code, 404)

    def test_bakery_put_nonexistent_id(self):
        data = {
            "name": "Nonexistent Bakery",
            "location": "Nowhere",
            "rating": 0
        }
        res = requests.put(f"{url_bakery}/999", json=data)
        self.assertEqual(res.status_code, 404)

    def test_cake_put_with_invalid_data(self):
        data = {
            "flavor": 12
        }
        res = requests.put(f"{url_cake}/1", json=data)
        self.assertEqual(res.status_code, 400)

    def test_bakery_put_with_invalid_data(self):
        data = {
            "name": 12,
            "location": ["Unknown Location", 12, 2]
        }
        res = requests.put(f"{url_bakery}/1", json=data)
        self.assertEqual(res.status_code, 400)