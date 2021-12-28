#---------------------------Практика с Владиславом---------------------------------
"""from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO инициализировать объект "Стакан"

        self.capacity_capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.occupied_volume = occupied_volume

    def __check_capacity_volume(self, value):
        if not isinstance(capacity_volume, (value, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError

#     @staticmethod
#     def __check_occupied_volume(self, value):
#         """
#         Функция проверяет занятый объем стакана
#         :param self:
#         :param value: Значение занятого объема стакана
#         :return: Значение занятого стакана после проверки типов
#         """
#         if not isinstance(value, (int, float)):
#             raise TypeError
#         if value < 0:
#             raise ValueError
#         return value
#
# if __name__ == "__main__":
#     glass1 = Glass(500, 100)
#
#     glass2 = Glass(200, "100")
#
#     glass
#     ...  # TODO инициализировать два объекта типа Glass
#
#     # TODO попробовать инициализировать не корректные объекты
"""
"""
#--------------------------------на практике Первушина-----------------------------

from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Для инициализации - это как бы искиз, по которому мы будем создавать экземпляры
        :param capacity_volume: объем стакана, должен быть больше 0, должен быть числом
        :param occupied_volume: наполненость стакана, не может быть меньше 0 и больше его обёма
        """
        #  TODO инициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем должен быть числом")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана не может быть меньше 0")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Наполняемость должна быть числом")
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError("Стакан не Изделие №1, ")
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    # TODO инициализировать два объекта типа Glass
    glass1 = Glass(200, 100)
    glass2 = Glass(300, 250)

    print(glass1)
    print(glass2)
    # TODO попробовать инициализировать не корректные объекты
    #glass3 = Glass("400", "100")
    glass4 = Glass(100, -80)
    print(glass4)