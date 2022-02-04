"""Модуль, который описывает класс Shop."""
import product, checktypes, category, basket, user


class Shop:
    """Класс описывающий магазин"""
    def __init__(self, shop_name: str):
        """
        Создаем магазин
        :param shop_name: имя магазина
        """
        checktypes.check_type(shop_name, str)
        self._shop_name = shop_name

        self.shop_users = []
        self.shop_catalogs = []
        self.shop_catalogs_product = []
