import checktypes
from category import Category, Product


class Basket:
    """
    Класс, который описывает корзину с купленными товарами
    """
    def __init__(self):
        """Создаем корзину товаров"""
        self._basket = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self._basket})"

    def __str__(self):
        return f"Товары в корзине: {self.to_list_basket()}"

    def to_list_basket(self) -> list:
        return [str(value) for value in self._basket]

    @property
    def basket_data(self):
        """
        Свойство, возвращающее содержимое корзины
        :return: self._basket
        """
        return self._basket

    @basket_data.setter
    def basket_data(self, data: Product):
        """
        Свойство, которое присваивает значение атрибуту self._basket.
        :param data: аргумент класса Product.
        """
        checktypes.check_type(data, Product)
        self._basket.append(data)


if __name__ == "__main__":

    print("-----Создаем Продукт-----")
    pr1 = Product("Джинсы", 100, 1)
    pr2 = Product("Брюки", 200, 2)
    print(pr1)
    print(pr2)

    pr3 = Product("Джинсовка", 150, 1)
    pr4 = Product("Пуховик", 350, 3)
    print(pr3)
    print(pr4)
    print("----------")
    print("-----Помещаем в корзину-----")
    bas1 = Basket()
    bas1.basket_data = pr1
    bas1.basket_data = pr3
    bas1.basket_data = Product("Носки", 10, 5)
    print(bas1)