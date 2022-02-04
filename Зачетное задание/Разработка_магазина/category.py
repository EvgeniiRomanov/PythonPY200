import checktypes
from product import Product


class Category:
    """
    Класс, который описывает категорию товаров
    """
    def __init__(self, category_name: str):
        """
        Создаем категорию товаров
        :param category_name:    имя категории

        """
        checktypes.check_type(category_name, str)

        self._category_name = category_name
        self._category_data = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self._category_name}, {self._category_data})"

    def __str__(self):
        return f"Категория товара: {self._category_name}\n{self.to_list()}\n"

    def to_list(self) -> list:
        return [str(value) for value in self._category_data]

    def get_category_name(self):
        """Метод возвращает имя категории"""
        return self._category_name

    def set_category_name(self, new_name):
        """
        Метод переименования категории с проверкой на валидность типа
        :param new_name: новое имя товара
        """
        checktypes.check_type(new_name, str)
        self._category_name = new_name

    @property
    def category_data(self):
        """
        Свойство, которое возвращает значение товара класса Product
        :return: self._category_data
        """
        return self._category_data

    @category_data.setter
    def category_data(self, data: Product):
        """
        Свойство, которое присваивает значение атрибуту self._category_data.
        :param data: аргумент класса Product.
        """
        checktypes.check_type(data, Product)
        self._category_data.append(data)


if __name__ == "__main__":
    cat1 = Category("Штаны")
    cat1.category_data = Product("Джинсы", 100, 1)
    cat1.category_data = Product("Брюки", 200, 2)
    cat1.category_data = Product("Ватники", 500, 3)
    print(cat1)

    cat2 = Category("Верхняя одежда")
    cat2.category_data = Product("Джинсовка", 150, 1)
    cat2.category_data = Product("Пуховик", 350, 3)
    print(cat2)
