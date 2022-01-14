class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value, next_=None):
        self.value = value  # публичный атрибут

        self.__next = None  # непубличный атрибут, потому что перед названием стоят два нижних подчеркивания


node = Node("value")

print(node.value)  # value
print(node.__next)  # AttributeError