class Driver:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name})"

    def __str__(self):
        return f"Водитель {self.__name}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


if __name__ == '__main__':
    ivan = Driver("Иван")
    ivan = Driver("Алексей")



