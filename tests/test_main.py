import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestMain(unittest.TestCase):

    def test_home(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_products(self):
        response = client.get("/products/")
        self.assertEqual(response.status_code, 200)

    def test_get_product_not_found(self):
        response = client.get("/products/9999")
        self.assertEqual(response.status_code, 404)

    def test_delete_product_not_found(self):
        response = client.delete("/products/9999")
        self.assertEqual(response.status_code, 404)

    def test_update_product_not_found(self):
        data = {
            "name": "Updated",
            "description": "Updated Desc",
            "quantity": 5,
            "price": 50
        }
        response = client.put("/products/9999", json=data)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()