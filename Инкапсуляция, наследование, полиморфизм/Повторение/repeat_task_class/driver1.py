class PropertyClass:

    def __init__(self):
        self.__inside_attr = None

    @property
    def ggg(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        print("Вызван prop getter")
        return self.__inside_attr

    @ggg.setter
    def ggg(self, value):
        """Сеттер принимает один агрумент, и не должен возвращать результат."""
        print("Вызван prop setter")
        self.__inside_attr = value


obj = PropertyClass()
print(obj.ggg)  # вызов getter
obj.__inside_attr = 456
print(obj.__inside_attr)
print(obj.__dict__)
print(PropertyClass.__dict__)
print(obj.ggg)
# obj.__inside_attr = 456
# print(obj.ggg)