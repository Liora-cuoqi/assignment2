"""
Unit tests for Problem 3: Order

Instructions:
Complete the unit test methods below using Python's unittest framework.
Your test methods must assert MULTIPLE ATTRIBUTES on the Order object
(e.g., subtotal, discount_amount, tax_amount, shipping_fee, final_total, status)
to verify state consistency under various conditions.

Running tests:
    python -m unittest test_problem3.py -v
"""
import unittest
from problem3 import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.regular_order = Order("ORD100", customer_tier="regular")
        self.silver_order = Order("ORD200", customer_tier="silver")
        self.gold_order = Order("ORD300", customer_tier="gold")

    def test_initial_order_state(self):
        """Verify initial attributes of an order."""
        self.assertEqual(self.regular_order.order_id, "ORD100")
        self.assertEqual(self.regular_order.customer_tier, "regular")
        self.assertEqual(self.regular_order.status, "PENDING")
        self.assertEqual(self.regular_order.subtotal, 0.0)
        self.assertEqual(self.regular_order.final_total, 0.0)

    def test_add_and_remove_items(self):
        """Test adding and removing items from order."""
        self.regular_order.add_item("Shirt", 20.0, 2)
        self.assertEqual(self.regular_order.subtotal, 40.0)
        self.assertEqual(self.regular_order.shipping_fee, 5.99)

        self.regular_order.remove_item("Shirt", 1)
        self.assertEqual(self.regular_order.subtotal, 20.0)

    def test_tier_discounts_and_shipping(self):
        """Test gold tier discount (10%) and free shipping threshold (>= $50)."""
        self.gold_order.add_item("Phone", 100.0, 1)
        self.assertEqual(self.gold_order.discount_amount, 10.0)
        self.assertEqual(self.gold_order.shipping_fee, 0.0)

    def test_coupon_application(self):
        """Test applying 'SAVE10' coupon."""
        self.regular_order.add_item("Book", 50.0, 1)
        self.regular_order.apply_coupon("SAVE10")
        self.assertEqual(self.regular_order.discount_amount, 5.0)

    def test_checkout_and_cancel_status_transitions(self):
        """Test checkout and cancellation rules."""
        self.regular_order.add_item("Item", 10.0, 1)
        self.assertTrue(self.regular_order.checkout())
        self.assertEqual(self.regular_order.status, "PAID")

        with self.assertRaises(RuntimeError):
            self.regular_order.add_item("Item2", 5.0, 1)
        with self.assertRaises(RuntimeError):
            self.regular_order.cancel()




if __name__ == "__main__":
    unittest.main()
