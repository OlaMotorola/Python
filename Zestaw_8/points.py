import math
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstruktor
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"  # zwraca string "(x, y)"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"  # zwraca string "Point(x, y)"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y  # porównanie punktów

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)  # suma wektorów

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)  # różnica wektorów

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  # iloczyn skalarny

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)  # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(2, 3)), "(2, 3)")

    def test_repr(self):
        self.assertEqual(repr(Point(2, 3)), "Point(2, 3)")

    def test_eq(self):
        self.assertTrue(Point(2, 3) == Point(2, 3))
        self.assertFalse(Point(2, 3) == Point(3, 2))

    def test_ne(self):
        self.assertTrue(Point(2, 3) != Point(3, 2))
        self.assertFalse(Point(2, 3) != Point(2, 3))

    def test_add(self):
        result = Point(2, 3) + Point(1, 1)
        self.assertEqual(result, Point(3, 4))

    def test_sub(self):
        result = Point(3, 4) - Point(1, 1)
        self.assertEqual(result, Point(2, 3))

    def test_mul(self):
        result = Point(2, 3) * Point(1, 4)
        self.assertEqual(result, 14)  # (2*1 + 3*4) = 2 + 12 = 14

    def test_length(self):
        self.assertAlmostEqual(Point(3, 4).length(), 5.0)  # sqrt(3^2 + 4^2) = 5.0
        self.assertAlmostEqual(Point(1, 1).length(), math.sqrt(2))

    def test_hash(self):
        p1 = Point(2, 3)
        p2 = Point(2, 3)
        p3 = Point(3, 2)
        self.assertEqual(hash(p1), hash(p2))
        self.assertNotEqual(hash(p1), hash(p3))

if __name__ == "__main__":
    unittest.main()
