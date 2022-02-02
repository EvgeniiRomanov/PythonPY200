"""Модуль, который содержит функции для проверки типов данных check_type и check_types"""

from typing import Any


def check_type(value: Any, types: Any):
    """
    Функция проверяет тип введеного значения на соовтетствие типу(типам)
    Если тип int или float проверка, что значение больше 0
    """
    if not isinstance(value, types):
        raise TypeError(f"Ожидается {types}, получено {type(value)}")
    if isinstance(value, (int, float)):
        if value < 0:
            raise ValueError(f"Значение не может быть меньше 0!")
    else:
        return f'ok'


# def check_value(value: Any, types: Any):
#     """Функция проверяет что значение больше 0"""
#     if value < 0:
#         raise ValueError(f"Значение не может быть меньше 0!")
#     else:
#         return f'ok'


if __name__ == '__main__':
    a = "10"

    print(check_type(a, str))