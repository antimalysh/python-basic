"""
создайте класс `Car`, наследник `Vehicle`
"""
import engine
from homework_02.base import Vehicle
from homework_02.engine import Engine
class Car(Vehicle):
    engine: int


    def set_engine(self, x):
        self.engine = x
        # self.volume = Engine(engine.Engine.volume)
        # self.pistons = Engine(engine.Engine.pistons)
        return



