class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod   #т.к. просто проверка
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
          # TODO
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
          # TODO
        if self.is_leap_year(year):
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]


    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        # TODO
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("Вводится целое число!")
        if not 0 < day <= 31:
            raise ValueError("В месяце от 1 до 31 дня, а в феврале до 28 или 29")
        if self.is_leap_year(year) and month == 2:
            if not 0 < day <= 29:
                raise ValueError("В высокосном году в феврале от 1 до 29 дней")
        elif not self.is_leap_year(year) and month == 2:
            if not 0 < day <= 28:
                raise ValueError("В обычном году в феврале от 1 до 28 дней")
        if not 0 < month <= 12:
            raise ValueError("В году от 1 до 12 месяцев")
        if year <= 0:
            raise ValueError("Рассматриваем нашу эру")

        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.__class__.__name__}({self.day}.{self.month}.{self.year})"


if __name__ == "__main__":
    # Write your solution here
    y = Date(31, 1, 2021)
    print(y)

    x = Date(29, 2, 2001)  # ошибка на количество дней в феврале в обычном году
    print(x)

