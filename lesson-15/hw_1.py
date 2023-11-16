# Задание 1
class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return "Название автомобиля: {} Скорость: {} Пробег: {}".format(
            Autobus.name, Autobus.max_speed, Autobus.mileage)


Autobus = Transport("Renaul Logan", 180, 12)
print(Autobus)
