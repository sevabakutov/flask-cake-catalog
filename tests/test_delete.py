import unittest
import requests

BASE_URL = "http://localhost:5000/api/v1"
url_cake = f"{BASE_URL}/cakes"
url_bakery = f"{BASE_URL}/bakeries"

class TestDELETE(unittest.TestCase):
    def test_cake_delete(self):
        res = requests.delete(f"{url_cake}/1")
        print(res)
        self.assertEqual(res.status_code, 204)

        check_res = requests.get(f"{url_cake}/1")
        self.assertEqual(check_res.status_code, 404)

    def test_bakery_delete(self):
        res = requests.delete(f"{url_bakery}/1")
        self.assertEqual(res.status_code, 204)

        check_res = requests.get(f"{url_bakery}/1")
        self.assertEqual(check_res.status_code, 404)

    def test_cake_delete_nonexistent_id(self):
        res = requests.delete(f"{url_cake}/999")
        self.assertEqual(res.status_code, 404)

    def test_bakery_delete_nonexistent_id(self):
        res = requests.delete(f"{url_bakery}/999")
        self.assertEqual(res.status_code, 404)