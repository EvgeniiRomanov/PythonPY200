from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """

        self.value = value
        self.nextnode = next_
          # TODO добавить атрибуты

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        #...  # TODO вернуть значение узла
        return self.value
    # TODO добавить метод get_next
    def get_next(self) -> Optional["Node"]:
        return self.nextnode

if __name__ == '__main__':
    first_node = Node(1, 3)  # первый узел
    second_node = Node(2)  # второй узел
    third_node = Node(3)
    # TODO с помощью метода распечатать значение первого узла
    # TODO  с помощью метода распечатать следующий узел второго узла
    #print(first_node.value)
    print(first_node.get_value()) #равнсильно преды
    print(second_node.get_value())
    print(third_node.get_value())
    print(first_node.get_next())
    print(second_node.get_next())