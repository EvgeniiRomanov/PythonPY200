from typing import Union

class Trapezoid:
    """Класс который описывает трапецию."""
    def __init__(self, base_down: Union[int, float], base_up: Union[int, float], side_left: Union[int, float],
                 side_right: Union[int, float]):
        """
        Создаём трапецию.
        :param base_down:  длина основания трапеции
        :param base_up:    длина второго основания
        :param side_left:  длина левой стороны
        :param side_right: длина правой стороны
        """
        if not isinstance((base_down or base_up or side_left or side_right), (int, float)):
            raise TypeError("Значение должно быть числом.")
        if (base_down or base_up or side_left or side_right) < 0:
            raise ValueError("Значение должно быть больше 0.")

        self.base_down = base_down
        self.base_up = base_up
        self.side_left = side_left
        self.side_right = side_right


    def __repr__(self) ->str:
        return f"Trapezoid({self.base_down}, {self.base_up}, {self.side_left}, {self.side_right})"


    def get_hight(self):
        """
        Метод получения высоты трапеции.
        :return: возвращает высоту трапеции, значение округлено до 2 знаков.
        """
        tmp_chis = (self.base_down - self.base_up) ** 2 + self.side_left ** 2 - self.side_right ** 2
        tmp_znam = 2 * (self.base_down * self.base_up)
        tmp_hight = self.side_left ** 2 - (tmp_chis/tmp_znam) ** 2
        hight_ = round(tmp_hight ** (0.5), 2)
        return hight_


    def get_perimetr(self):
        """
        Метод получения периметра трапеции.
        :return: возвращает периметр трапеции, значение округлено до 2 знаков.
        """
        return round(self.base_down + self.base_up + self.side_left + self.side_right, 2)


    def get_square(self):
        """
        Метод получения площади трапеции.
        :return: возвращает площадь трапеции, значение округлено до 2 знаков.
        """
        return ((self.base_down + self.base_up) / 2) * self.get_hight()


if __name__ == "__main__":

    tr1 = Trapezoid(9, 6, 4, 5)
    print(tr1)
    print(tr1.get_perimetr())
    print(tr1.get_hight())
    print(tr1.get_square())

    tr2 = Trapezoid(3, 1, 4, 5)
    print(tr2)
    print(tr2.get_perimetr())
    print(tr2.get_hight())
    print(tr2.get_square())

    print(tr1.__repr__())