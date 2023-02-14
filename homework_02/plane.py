"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0


    def load_cargo(self, y):
        self.y = y
        if y + self.cargo <= self.max_cargo:
            self.cargo += y
        else:
            raise CargoOverload("Возникла перегрузка")

    def remove_all_cargo(self):
        new_cargo = self.cargo
        self.cargo = 0
        return new_cargo


