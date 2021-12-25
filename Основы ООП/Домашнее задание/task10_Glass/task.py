# TODO написать класс Glass согласно условию
# Написать класс с одним атрибутом - нут типа из чего был создан дерева, металла, стекло
class Glass:
    """Класс описывающий материал изготовления стакана."""
    def __init__(self, material: str):
        """
        Создаем стакан. Материал изготовления только буквы или цифры.
        :param material: материал изготовления
        """
        if not isinstance(material, str):
            raise TypeError("Материал класса задается строкой")
        if not material.isalnum():
            raise ValueError("Состав материала только из букв и цифр!")
        self.material = material

    def get_material(self):
        return self.material

if __name__ == "__main__":
    glass1 = Glass("Дерево")
    glass2 = Glass("Металл")
    glass3 = Glass("Titan345")
    #glass4 = Glass("Олово_-56")

    print(glass3.get_material())