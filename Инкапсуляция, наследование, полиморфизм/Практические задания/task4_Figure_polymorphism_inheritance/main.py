import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

      # TODO определить конструктор и перегрузить метод area
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return self.a * self.b


class Circle(Figure):
    """ Производный класс. Круг. """
      # TODO определить конструктор и перегрузить метод area
    def __init__(self, radius: int):
        self.radius = radius
        self.const_pi = 3.14


    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return self.const_pi * self.radius ** 2


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
