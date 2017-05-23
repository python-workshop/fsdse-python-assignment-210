from unittest import TestCase


class TestFind_max_profit(TestCase):
    def test_find_max_profit(self):
        try:
            from build import find_max_profit
        except ImportError:
            self.assertFalse("no function found")
        self.assertRaises(TypeError, find_max_profit, None)
        self.assertRaises(ValueError, find_max_profit, [])
        self.assertEqual(find_max_profit([8, 5, 3, 2, 1]), -1)
        self.assertEqual(find_max_profit([5, 3, 7, 4, 2, 6, 9]), 7)
