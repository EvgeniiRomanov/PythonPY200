from typing import Union
#from Chekking_types import check_type


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
        if not isinstance(product_name, str) and not isinstance(product_price, (int, float)) and \
                not isinstance(product_rating, (int, float)):
            raise TypeError("Введено не корректное значение.")
        if (product_price and product_rating) < 0:
            raise ValueError("Значение должно быть больше 0.")

        self._product_name = product_name
        self._product_price = product_price
        self._product_rating = product_rating

    def __repr__(self):
        return f"{self.__class__.__name__}({self._product_name}, {self._product_price}, {self._product_rating})"



if __name__ == "__main__":
    pr = Product("Ovoshi", 100, 1.5)

    print(pr)