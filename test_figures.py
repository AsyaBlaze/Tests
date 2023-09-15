import math
from abc import ABC, abstractmethod

import pytest


#Фигура
class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.get_area() + other_figure.get_area()
        raise ValueError(f'Object {other_figure} is not Figure')


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'Can not create Rectangle')
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)



class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if ((side_a + side_b <= side_c or
            side_c + side_a <= side_b or
            side_c + side_b <= side_a)
                or (side_a <= 0 or side_c <= 0 or side_b <= 0)):
            raise ValueError(f'Can not create Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = 'Triangle'

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return int(math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError(f'Can not create Square')
        self.side = side
        self.name = 'Square'

    def get_area(self):
        return math.pow(self.side, 2)

    def get_perimeter(self):
        return self.side * 4


# Тесты

# тесты для прямоугольника
@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (4, 5, 18, 20),
                             (10, 20, 60, 200),
                             (7, 5, 24, 35),
                         ])
def test_rectangle(side_a, side_b, perimeter, area):
    r = Rectangle(side_a, side_b)
    assert r.name == 'Rectangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (-4, 5, 2, 20),
                             (0, 20, 40, 0),
                         ])
def test_rectangle_negative(side_a, side_b, perimeter, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


# тесты для треугольника
@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (9, 8, 7, 24, 26),
                             (11, 6, 7, 24, 18),
                             (21, 12, 10, 43, 34),
                             (19, 13, 15, 47, 97)
                         ])
def test_triangle(side_a, side_b, side_c, perimeter, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == 'Triangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (-4, 5, 6, 2, 20),
                             (0, 20, 40, 4, 0),
                             (20, 2, 4, 54, 56)
                         ])
def test_triangle_negative(side_a, side_b, side_c, perimeter, area):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


# тесты для квадрата
@pytest.mark.parametrize('side, perimeter, area',
                         [
                             (1, 4, 1),
                             (3, 12, 9),
                             (10, 40, 100),
                             (12, 48, 144)
                         ])
def test_triangle(side, perimeter, area):
    r = Square(side)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side, perimeter, area',
                         [
                             (-4, 5, 6),
                             (0, 20, 40)
                         ])
def test_triangle_negative(side, perimeter, area):
    with pytest.raises(ValueError):
        Square(side)