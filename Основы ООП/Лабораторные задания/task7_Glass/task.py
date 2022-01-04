from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        # Так предлагает Владислав
        self.capacity_volume = self.init_capacity_volume(capacity_volume)
        # Так предлагает Алексей
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    # Так предлагает Владислав
    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError

        return capacity_volume

    # Так предлагает Алексей
    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError("Объем не может быть меньше 0")
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

 #т


