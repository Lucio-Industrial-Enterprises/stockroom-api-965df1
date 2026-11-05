import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit(self):
        """Passing service='standard' must give the same result as omitting it."""
        self.assertEqual(shipping_quote(2, "local", "standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", "standard"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    # ------------------------------------------------------------------
    # Express service (+$7 surcharge)
    # ------------------------------------------------------------------
    def test_express_local(self):
        # 5.0 + 1.5*2 + 7.0 = 15.0
        self.assertEqual(shipping_quote(2, "local", "express"), 15.0)

    def test_express_regional(self):
        # 8.0 + 1.5*2 + 7.0 = 18.0
        self.assertEqual(shipping_quote(2, "regional", "express"), 18.0)

    def test_express_seven_dollars_more_than_standard(self):
        for zone in ("local", "regional"):
            std = shipping_quote(5, zone, "standard")
            exp = shipping_quote(5, zone, "express")
            self.assertAlmostEqual(exp - std, 7.0)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", "overnight")

    def test_unknown_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")
