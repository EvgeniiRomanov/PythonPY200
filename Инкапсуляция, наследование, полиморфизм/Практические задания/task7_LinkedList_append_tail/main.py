from typing import Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0                           # O(1)
        self.head: Optional[Node] = None       # O(1)
        self.tail = self.head                   # O(1)

        if data is not None:
            for value in data:                 # 0(N)
                self.append(value)

    def append(self, value: Any):               #O(N)
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)               # O(1)

        if self.head is None:
            self.head = self.tail = append_node  # TODO добавить использование self.tail # O(1)
        else:
            self.linked_nodes(self.tail, append_node)  # O(N)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:            # O(N)
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):                  # O(N)
            raise TypeError()

        if not 0 <= index < self.len:  # для for           # O(1)
            raise IndexError()

        current_node = self.head                        # O(1)
        for _ in range(index):                          # O(N)
            current_node = current_node.next            # O(N)

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:   # O(N)
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node  # TODO next теперь свойство имеет setter, используйте это # O(N)

    def __getitem__(self, index: int) -> Any:     # O(N)
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)   # O(N)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:   # O(N)
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)                        # O(N)
        node.value = value                                             # O(1)

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]         #O(N)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"           # O(N)

    def __str__(self) -> str:
        return f"{self.to_list()}"                                      #O(N)


if __name__ == "__main__":
    list_ = [1, 2, 3]

    ll = LinkedList(list_)
    print(ll)

    ll.append(100)
    print(ll)
