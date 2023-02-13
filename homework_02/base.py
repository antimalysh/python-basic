from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=30, fuel_consumption=10, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False
    def start(self):
       if not self.started:
           if self.fuel > 0:
               self.started = True
           else:
               raise LowFuelError("Низкий уровень топлива")

    def move(self, distance=1000):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel("Не достаточно топлива")

