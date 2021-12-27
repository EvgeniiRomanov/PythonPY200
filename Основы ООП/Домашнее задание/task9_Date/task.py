
class Date:
    """
    Класс который описывает дату в формате день, месяц, год - DD/MM/YYYY.
    """
    def __init__(self, day_: int, month_: int, year_: int):
        """
        Создаём новую дату
        :param day_: задаём дату
        :param month_: задаём месяц
        :param year_: задаём год
        """
        if not isinstance((day_ | month_ | year_), int):
            raise TypeError("Вводится целое число!")

        self.day_ = day_
        self.month_ = month_
        self.year_ = year_

    def __repr__(self) -> str:
        return f"{self.day_:02}/{self.month_:02}/{self.year_}"

    def __str__(self) -> str:
        return f"{self.day_:02}/{self.month_:02}/{self.year_}"


if __name__ == "__main__":
    Date1 = Date(10, 12, 2021)
    Date2 = Date(1, 2, 2022)
    # Проверяем __str__
    print(Date1)
    print(Date2)
    # Проверяем __repr__
    print([Date(i, i, 2000+i) for i in range(1, 12)])



