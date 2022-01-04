from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        # Так предлагает Алексей
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)


    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    # Так предлагает Алексей
    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError("Объем не может быть меньше 0")
        self.occupied_volume = occupied_volume

    def add_water(self, value_water_):
        if not isinstance(value_water_, (int, float)):
            raise TypeError
        if value_water_ > self.capacity_volume - self.occupied_volume:
            raise ValueError("Стакан не изделие №1")

        self.occupied_volume = self.occupied_volume + value_water_


    def remove_water(self, remove_water_):
        if not isinstance(remove_water_, (int, float)):
            raise TypeError
        if remove_water_ > self.occupied_volume:
            raise ValueError("Нельзя вылить воды больше, чем есть")

        self.occupied_volume = self.occupied_volume - remove_water_


if __name__ == "__main__":
    glass = Glass(300, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(150)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.remove_water(70)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(120)
    print(glass.capacity_volume, glass.occupied_volume)
 #т





# TODO Добавит