import unittest
from app import crud
from app.database import SessionLocal
from app.schemas import ProductCreate

class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()

    def test_delete_product(self):
        data = ProductCreate(
            name="Delete Test",
            description="Desc",
            quantity=5,
            price=50
        )

        product = crud.create_product(self.db, data)
        deleted = crud.delete_product(self.db, product.id)

        self.assertIsNotNone(deleted)

        check = crud.get_product(self.db, product.id)
        self.assertIsNone(check)


if __name__ == "__main__":
    unittest.main()