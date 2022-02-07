from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value}, {self.next})"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def is_valid(node: Any) -> None:
        """
        Проверка передаваемого значения на принадлежность Node или None
        :param node: передаваемое значение
        """
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        """Свойство возвращает ссылку на след узел"""
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        """
        Свойство устанавлиевает ссылку на след узел
        :param next_: след узел
        """
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """Класс описывающий узел связного списка, связанный с предыдущим и следующим"""
    def __init__(self, value: Any, next_: Optional["Node"] = None, prev_: Optional["Node"] = None):
        """
        Создаем новый узел для двухсвязного списка
        :param value: Любое значение, которое помещено в узел
        :param prev_: предыдущий узел, если он есть
        :param next_: следующий узел, если он есть
        """
        super().__init__(value=value, next_=next_)
        self.prev = prev_

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.prev}, {self.value}, {self.next})"

    # def __str__(self) -> str:
    #     return str(self.value)

    # def is_valid(self, node: Any) -> None:
    #     if not isinstance(node, (type(None), Node)):
    #         raise TypeError

    @property
    def prev(self):
        """Свойство возвращает ссылку на предыдущий узел"""
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        """Свойство устанавливает значение предыдущего узла"""
        self.is_valid(prev_)
        self._prev = prev_


if __name__ == "__main__":
    print("--------Отработка односвязного узла-----------")
    nd1 = Node(1)
    nd2 = Node(2)
    print(nd1)
    print(nd2)
    print(nd2.__repr__())
    nd2.next = nd1
    print(nd2.__repr__())

    print("--------Отработка двусвязного узла-----------")
    nd3 = DoubleLinkedNode(5)
    print(nd3.__repr__())
    nd4 = DoubleLinkedNode(4, Node(7), nd3)
    print(nd4)
    print(nd4.__repr__())

