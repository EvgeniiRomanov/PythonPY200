class Glass:
    count = 0  # количество созданных стаканов

    def __init__(self):
        cls = self.__class__  # type(self)
        cls.count += 1


# создаем стакан
glass_1 = Glass()
print(Glass.count)  # проверяем количество созданных стаканов

# создаем ещё один стакан
glass_2 = Glass()
print(Glass.count)