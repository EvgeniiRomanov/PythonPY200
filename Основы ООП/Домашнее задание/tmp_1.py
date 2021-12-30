class Glass:
    material = "paper"

    @classmethod
    def set_material(cls, material):
        cls.material = material

    def __str__(self):
        return f"Стакан из материала - {self.__class__.material}"


glass_1 = Glass()
glass_2 = Glass()
glass_1.set_material("wood")

print(glass_1)
print(glass_2)