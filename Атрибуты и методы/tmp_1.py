# class Node:
#     """ Класс, который описывает узел связного списка. """
#
#     def __init__(self, value, next_=None):
#         self.value = value  # публичный атрибут
#
#         self.__next = None  # непубличный атрибут, потому что перед названием стоят два нижних подчеркивания
#
#
# node = Node("value")
#
# print(node.value)  # value
# print(node.__next)  # AttributeError

if __name__ == "__main__":

    a = 0
    key_TO = True

    for i in range(0, 100, 1):
        print((a + i))
        # print((a + i) % 30)
        # print((a + i) // 30)
        print(((a + i) / 30) * 10)
        print("--------------------")
        # if (a + i) % 30 == 0 and key_TO is True:
        #     print(f"{a + i} Ноль {(a + i) % 30}")
        #     print("Пройдите ТО, через 10 км автомобиль не поедет!")
        #
        # else:
        #     print(f"{a + i} Больше {(a + i) % 30}")

