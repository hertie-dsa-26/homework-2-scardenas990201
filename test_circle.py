import math
import unittest

from circle import Circle


class TestCircle(unittest.TestCase):
    # Testing perimeter
    def test_perimeter(self):
        circle = Circle(3)
        expected = 2 * math.pi * 3
        self.assertAlmostEqual(circle.perimeter(), expected, places=7)
    # Testing Area

    def test_area(self):
        circle = Circle(3)
        expected = math.pi * (3 ** 2)
        self.assertAlmostEqual(circle.area(), expected, places=7)
    # Testing Radius

    def test_zero_radius(self):
        circle = Circle(0)
        self.assertEqual(circle.perimeter(), 0)
        self.assertEqual(circle.area(), 0)


if __name__ == "__main__":
    unittest.main()
