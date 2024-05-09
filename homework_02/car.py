"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = ()
        #self.engine = None

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self.engine = engine
        return self.engine

# def main():
#     car_1 = Car(100,17,6)
#     print(type(car_1.engine))
#
# if __name__ == "__main__":
#     main()