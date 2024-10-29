import unittest
import requests

BASE_URL = "http://localhost:5000/api/v1"
url_cake = f"{BASE_URL}/cakes"
url_bakery = f"{BASE_URL}/bakeries"

class TestGET(unittest.TestCase):
    def test_cakes_get(self):
        res = requests.get(url_cake)
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(res.json()), 1)

    def test_cakes_get_id(self):
        res= requests.get(f"{url_cake}/1")
        res_data = res.json()

        self.assertEqual(res.status_code, 200)
        # self.assertEqual(res_data.get("name"), "Cool")

    def test_bakeries_get(self):
        res = requests.get(url_bakery)
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(res.json()), 1)

    def test_bakeries_get_id(self):
        res = requests.get(f"{url_bakery}/1")
        res_data = res.json()

        self.assertEqual(res.status_code, 200)
        # self.assertEqual(res_data.get("name"), "Best Bakery")

    def test_bakery_cakes(self):
        res = requests.get(f"{url_bakery}/1/cakes")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [])

    def test_cakes_get_with_filters(self):
        params = {
            "flavor": "Vanila",
            "price": 8
        }
        res = requests.get(url_cake, params=params)
        res_data = res.json()

        self.assertEqual(res.status_code, 200)
        for cake in res_data:
            self.assertEqual(cake.get("flavor"), "Vanila")
            self.assertEqual(float(cake.get("price")), 8)

    def test_cakes_get_pagination(self):
        params = {
            "page": 1,
            "limit": 2
        }
        res = requests.get(url_cake, params=params)
        res_data = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertLessEqual(len(res_data), 2)

    def test_cakes_get_nonexistent_id(self):
        res = requests.get(f"{url_cake}/999")
        self.assertEqual(res.status_code, 404)

    def test_bakeries_get_nonexistent_id(self):
        res = requests.get(f"{url_bakery}/999")
        self.assertEqual(res.status_code, 404)

    def test_bakery_cakes_nonexistent_bakery(self):
        res = requests.get(f"{url_bakery}/999/cakes")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json().get("error"), "Bakery was not found")




