import time

from driver1 import Driver


class DriverTypeError(Exception):
    pass


class EngineIsNotRunning(Exception):
    pass

class DriverNotFoundError(Exception):
    pass


class TechnicInspection(Exception):
    pass


class Car:
    brand = None
    _max_speed = 180
    __created_car = 0


    def __init__(self, color, body_type, model_name,
                 engine_type, gear_type, complectation):

        self.__model_name = model_name
        self.__body_type = body_type
        self._engine_type = engine_type
        self._gear_type = gear_type
        self.complectation = complectation
        self.color = color


        self.__mileage = 0
        self.__count_TO = 1
        self.__const_TO = 25
        self.__status_TO = False
        self.__driver = None
        self.__engine_status = False

    def __new__(cls, *args, **kwargs):
        cls.__append_new_car_counter()
        print(f"Выпущено {cls.__created_car} автомобилей, класса {cls.__name__}")
        return super().__new__(cls)

    # =============
    # Методы класса
    # =============

    @classmethod
    def change_brand(cls, new_brand: str):
        cls.brand = new_brand

    @classmethod
    def _change_max_speed(cls, max_speed):
        if not isinstance(max_speed, (int, float)):
            raise TypeError(f"Ожидается {int} или {float}, получено {type(max_speed)}")
        cls._max_speed = max_speed

    @classmethod
    def __append_new_car_counter(cls):
        cls.__created_car += 1

    # ==================
    # Статические методы
    # ==================

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver: Driver):
        if not isinstance(driver, Driver):
            raise DriverTypeError(f"Ожидается {Driver}, получено {type(driver)}")
        self.__driver = driver

    # Эквивалент свойствам (property)
    # def set_driver(self, driver: Driver):
    #     if not isinstance(driver, Driver):
    #         raise DriverTypeError(f"Ожидается {Driver}, получено {type(driver)}")
    #     self.__driver = driver
    #
    # def get_driver(self):
    #     return self.__driver

    # Блок отработки движения машины
    def start_engine(self):
        self.__engine_status = True

    def __check_driver(self):
        if self.driver is not None:
            return True
        return False

    def __ready_status(self):
        if not self.__engine_status:
            raise EngineIsNotRunning("двигатель не запущен")
        if not self.__check_driver():
            raise DriverNotFoundError("водитель не найден")
        if not self.__check_technical_inspection():
            raise TechnicInspection(f"без пройденного ТО автомобиль не поедет")
        return True


    def move(self, distance=10):
        try:
            if self.__ready_status():
                for i in range(distance):
                    print(f'\rМашина проехала {i+1} км.', end='')
                    time.sleep(0.1)
                    self.__mileage += 1
                    if self.__mileage > self.__const_TO:
                        print(f" Общий пробег = {self.__mileage}, пройдите ТО {self.__count_TO}")
                        if self.__mileage % 30 == 0:
                            self.__status_TO = True
                            self.__const_TO += self.__mileage
                            raise TechnicInspection(f" ТО {self.__count_TO} НЕ ПРОЙДЕНО!")
                print(f'\nПройдено {self.__mileage}')
        except (EngineIsNotRunning, DriverNotFoundError, TechnicInspection) as e:
            print(f"Машина не может начать движение, т.к. {e}")

    # Блок отработки технического осмотра

    def __check_technical_inspection(self):
        if self.__status_TO is False:
            return True
        return False

    def _make_technical_inspection(self):
        print(f"TO {self.__count_TO} пройдено")
        self.__count_TO += 1
        self.__status_TO = False


    # Блок работы с защищёнными методами
    @property
    def _mileage(self):
        return self.__mileage

    @_mileage.setter
    def _mileage(self, mileage):
        if not isinstance(mileage, (int, float)):
            raise TypeError(f"Ожидается {int} или {float}, получено {type(mileage)}")

        self.__mileage = mileage
    # /Блок работы с защищёнными методами


if __name__ == '__main__':

    car = Car('черный', 'седан', 'модель', 'бензин', 'автомат', 'люкс')
    car_2 = Car('черный', 'седан', 'модель', 'бензин', 'автомат', 'люкс')

    # print(car.brand)
    # print(car_2.brand)
    # Car.change_brand("Nissan")
    # print(car.brand)
    # print(car_2.brand)
    #
    # print(car._max_speed)
    # print(car_2._max_speed)
    # Car._change_max_speed(190)
    # print(car._max_speed)
    # print(car_2._max_speed)


    # Блок работы с защищёнными методами
    # print(car._mileage)
    # car._mileage = '10'
    # print(car._mileage)
    # /Блок работы с защищёнными методами

    # Блок отработки движения машины
    car.start_engine()
    car.driver = Driver("Иван")
    car.move()
    car.move()
    car.move()
    car._make_technical_inspection()
    car.move()
    # car.move()
    # car.make_technical_inspection()
    # car.move()
    # car.move()

    # /Блок отработки движения машины

    # Блок отработки свойств
    # car.driver = Driver('Андрей')
    # print(car.driver)
    # Эквивалент свойствам (property)
    # car.set_driver(Driver('Андрей'))
    # car.get_driver()
    # /Блок отработки свойств
