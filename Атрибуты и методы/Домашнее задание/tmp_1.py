class Glass:
    count = 0  # количество созданных стаканов

    def __init__(self):
        print(self.__dict__)
        cls = self.__class__
        cls.count += 1
        print(self.__dict__)


# инициализируем стакан
glass = Glass()
glass1 = Glass()

print(Glass.count)
#print(Glass.count)