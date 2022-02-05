"""Модуль, который описывает класс Shop."""
import product, checktypes, category, basket, user
import hashlib


class Shop:
    """Класс описывающий магазин"""
    def __init__(self, shop_name: str):
        """
        Создаем магазин
        :param shop_name: имя магазина
        """
        checktypes.check_type(shop_name, str)
        self._shop_name = shop_name

        self.shop_users = {"Иван": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
                           "Федор": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
                           "Мария": "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"}

        self.shop_catalogs = []
        self.shop_catalogs_product = []

        while True:
            try:
                user_name_ = input("Введите Имя пользователя: ")
                if self.shop_users.get(user_name_) is None:
                    raise "Вы не наш клиент!"  # Далее можно добавлять тут нового пользователя, если его нет в словаре
                else:
                    try:
                        user_password_ = input("Введите пароль пользователя:")
                        checktypes.check_type(user_password_, str)
                        hash_ = bytes(user_password_, "UTF-8")
                        hash_password_ = hashlib.sha256(hash_).hexdigest()
                        #print(self.shop_users.values())
                        #print( hash_password_)
                        if hash_password_ == self.shop_users.get(user_name_):
                            print(f"Добро пожаловать в магазин покупатель {user_name_}!")
                            break
                        else:
                            print(f"Вы ввели неправильный пароль, попробуйте снова.")
                            continue
                    except ValueError:
                        print("!!!!!.")
                        break
            except ValueError:
                print("Вы пп.")
                break

if __name__ == "__main__":
    sh1 = Shop("Магазин")


