import pytest
from points import Point
from rectangles import Rectangle

def test_str():
    rect = Rectangle(1, 2, 3, 4)
    assert str(rect) == "[(1, 2), (3, 4)]"

def test_repr():
    rect = Rectangle(1, 2, 3, 4)
    assert repr(rect) == "Rectangle(1, 2, 3, 4)"

def test_eq():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(1, 2, 3, 4)
    rect3 = Rectangle(0, 0, 3, 4)
    assert rect1 == rect2
    assert rect1 != rect3

def test_from_points():
    pt1 = Point(1, 2)
    pt2 = Point(3, 4)
    rect = Rectangle.from_points((pt1, pt2))
    assert rect == Rectangle(1, 2, 3, 4)

def test_virtual_attributes():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.top == 4
    assert rect.bottom == 2
    assert rect.left == 1
    assert rect.right == 3
    assert rect.width == 2
    assert rect.height == 2
    assert rect.topleft == Point(1, 4)
    assert rect.bottomleft == Point(1, 2)
    assert rect.topright == Point(3, 4)
    assert rect.bottomright == Point(3, 2)

def test_center():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.center == Point(2, 3)

def test_area():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.area() == 4

def test_move():
    rect = Rectangle(1, 2, 3, 4)
    moved_rect = rect.move(1, 1)
    assert moved_rect == Rectangle(2, 3, 4, 5)

#Wywołanie: pytest rectangles_test.py