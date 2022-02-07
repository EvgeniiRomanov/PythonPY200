import checktypes
import hashlib
from basket import Basket, Product


class User:

    shop_users = {"Иван": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
                  "Федор": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
                  "Мария": "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"}

    def __init__(self, user_name: str, user_password: str):
        """
        Создаем пользователя
        :param user_name:       имя пользователя
        :param user_password:   пароль пользователя
        """
        checktypes.check_type(user_name, str)
        checktypes.check_type(user_password, str)

        self._user_name = user_name
        # self._user_password = None
        self.user_password = user_password  # это свойство (через =)
        self._user_basket = None
        cls = self.__class__
        cls.shop_users[self._user_name] = self.user_password
        print(cls.shop_users)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._user_name}, {self._user_password})"

    def __str__(self):
        return f"Пользователь: {self._user_name}. В корзине: {self._user_basket}"


    @property
    def user_password(self):
        """Метод возвращает пароль пользователя"""
        return self._user_password

    @user_password.setter
    def user_password(self, user_password: str):
        """
        Метод изменения пароля пользователя, хранится хэш пароля
        :param user_password: пароль введенный пользователем
        """
        checktypes.check_type(user_password, str)
        hash_ = bytes(user_password, "UTF-8")
        hash_password = hashlib.sha256(hash_).hexdigest()
        self._user_password = hash_password


    @property
    def user_basket(self):
        """Метод возвращает содержимое корзины пользователя"""
        return self._user_basket

    @user_basket.setter
    def user_basket(self, data: Basket):
        """
        Метод помещает в атрибут self._user_basket содержимое корзины
        :param data: содержимое корзины
        """
        checktypes.check_type(data, Basket)
        self._user_basket = data



if __name__ == "__main__":
    # Создаем товары - продукты

    pr = Product("Овощи", 100, 1.5)
    pr_1 = Product("Бананы", 200, 10)
    # print(pr.__dict__)
    print(pr)
    # Создаем корзину и помещаем в неё продукты

    bas1 = Basket()
    bas1.basket_data = pr
    bas1.basket_data = pr_1
    print(bas1)
    # Создаем пользователя и выдаем ему корзину

    us1 = User("Вася", "123")
    us1.user_basket = bas1
    print(us1._user_password)
    print(us1.user_password)

    # print()
