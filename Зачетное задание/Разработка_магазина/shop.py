"""Модуль, который описывает класс Shop."""
import product, checktypes, category, basket, user
import hashlib
#from user import *
from user import User

class Shop:
    """Класс описывающий магазин"""
    def __init__(self, shop_name: str):
        """
        Создаем магазин
        :param shop_name: имя магазина
        """
        checktypes.check_type(shop_name, str)
        self._shop_name = shop_name

        self.shop_catalogs = []
        self.shop_catalogs_product = []

        while True:
            try:
                user_name_ = input("Введите Имя пользователя: ")
                if User.shop_users.get(user_name_) is None:
                    print("Вы еще не зарегистрированы в нашем магазине, давайте пройдем регистрацию!")
                    new_username_ = input("Введите Ваше имя: ")
                    new_userpassword_ = input("Придумайте пароль: ")
                    new_user_ = User(new_username_, new_userpassword_)
                    print(f"Добро пожаловать в магазин покупатель {new_username_}!")
                    break
                else:
                    try:
                        user_password_ = input("Введите пароль пользователя:")
                        checktypes.check_type(user_password_, str)
                        hash_ = bytes(user_password_, "UTF-8")
                        hash_password_ = hashlib.sha256(hash_).hexdigest()
                        if hash_password_ == User.shop_users.get(user_name_):
                            print(f"Добро пожаловать в магазин покупатель {user_name_}!")
                            break
                        else:
                            print(f"Вы ввели неправильный пароль, попробуйте снова.")
                            continue
                    except ValueError:
                        print("Дописать!!!")
                        break
            except ValueError:
                print("Дописать_2!!!")
                break


if __name__ == "__main__":
    sh1 = Shop("Магазин")
    sh1

