"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
class Car(Vehicle):
    engine: int


    def set_engine(self, x):
        self.engine = x
        return



