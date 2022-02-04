import hashlib
import checktypes

shop_users = {"Иван": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
                           "Федор": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
                           "Мария": "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"}

while True:
            try:
                user_name_ = input("Введите Имя пользователя: ")
                if shop_users.get(user_name_) is None:
                    raise "Вы не наш клиент!"
                else:
                    try:
                        user_password_ = input("Введите пароль пользователя:")
                        checktypes.check_type(user_password_, str)
                        hash_ = bytes(user_password_, "UTF-8")
                        hash_password_ = hashlib.sha256(hash_).hexdigest()
                        print(shop_users.values())
                        print( hash_password_)
                        #if hash_password_ in shop_users.values():
                        if hash_password_ == shop_users.get(user_name_):
                            print(f"Добро пожаловать в магазин покупатель {user_name_}!")
                            break
                        else:
                            print(f"Вы ввели неправильный пароль, попробуйте снова.")
                            continue
                    except ValueError:
                        print("Вы ввели не число, попробуйте снова.")
                        break
            except ValueError:
                print("Вы пп.")
                break

if __name__ == "__main__":
    pass