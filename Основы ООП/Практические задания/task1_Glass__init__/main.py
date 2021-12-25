from typing import Union


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

    @staticmethod
    def __check_occupied_volume(self, value):
        """
        Функция проверяет занятый объем стакана
        :param self:
        :param value: Значение занятого объема стакана
        :return: Значение занятого стакана после проверки типов
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

if __name__ == "__main__":
    glass1 = Glass(500, 100)

    glass2 = Glass(200, "100")

    glass
    ...  # TODO инициализировать два объекта типа Glass

    # TODO попробовать инициализировать не корректные объекты
