from typing import Union

import CheckTypes


class Product:
    """
    Класс, который описывает товар
    """
    def __init__(self, product_name: str, product_price: Union[int, float], product_rating: Union[int, float]):
        """
        Создаем экземпляр товара
        :param product_name:    имя товара
        :param product_price:   цена товара
        :param product_rating:  рейтинг товара
        """
        # if not isinstance(product_name, str) and not isinstance(product_price, (int, float)) and \
        #         not isinstance(product_rating, (int, float)):
        #     raise TypeError("Введено не корректное значение типа.")
        # if (product_price and product_rating) < 0:
        #     raise ValueError("Значение должно быть больше 0.")
        CheckTypes.check_type(product_name, str)
        CheckTypes.check_type(product_price, (float, int))
        CheckTypes.check_type(product_rating, (float, int))

        self._product_name = product_name
        self._product_price = product_price
        self._product_rating = product_rating

    def __repr__(self):
        return f"{self.__class__.__name__}({self._product_name}, {self._product_price}, {self._product_rating})"

    def get_product_name(self):
        """Метод возвращает имя товара"""
        return self._product_name

    def set_product_name(self, new_name):
        """
        Метод переименования товара с проверкой на валидность типа
        :param new_name: новое имя товара
        """
        CheckTypes.check_type(new_name, str)
        self._product_name = new_name

    def get_product_price(self):
        """Метод возвращает значение стоимости товара"""
        return self._product_price

    def set_product_price(self, new_price):
        """
        Метод изменяет стоимость товара с проверкой на валидность типа и величину вводимого значения больше 0
        :param new_price: новая стоимость товара
        """
        CheckTypes.check_type(new_price, (float, int))
        self._product_price = new_price

    def get_product_rating(self):
        """Метод возвращает значение рейтинга товара"""
        return self._product_rating

    def set_product_rating(self, new_rating):
        """
        Метод изменяет рейтинг товара с проверкой на валидность типа и величину значения больше 0
        :param new_rating: новый рейтинг товара
        """
        CheckTypes.check_type(new_rating, (float, int))
        self._product_rating = new_rating

if __name__ == "__main__":
    pr = Product(kkkk, -100, 1.5)
    print(pr.__dict__)
    print(pr)
    pr.set_product_name("-111")
    pr.set_product_price(10)
    pr.set_product_rating(1)

    print(pr.__dict__)
    print(pr._product_name, pr._product_price)
    print(pr)