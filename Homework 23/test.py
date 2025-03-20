import unittest
from main import process_orders

class TestProcessOrders(unittest.TestCase):
    def test_product_not_in_inventory(self):
        orders = [{"product": "banana", "quantity": 3}]
        inventory = {"apple": 10}

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)
        self.assertEqual(str(context.exception), "Product 'banana' not found in inventory")

    def test_not_enough_stock(self):
        orders = [{"product": "apple", "quantity": 15}]
        inventory = {"apple": 10}

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)
        self.assertEqual(str(context.exception), "Not enough stock for 'apple'")

    def test_successful_order(self):
        orders = [{"product": "apple", "quantity": 5}]
        inventory = {"apple": 10}

        successful_orders = process_orders(orders, inventory)

        self.assertEqual(successful_orders, orders)  # Ensure order is processed
        self.assertEqual(inventory["apple"], 5)  # Ensure stock is updated correctly


if __name__ == "__main__":
    unittest.main()
