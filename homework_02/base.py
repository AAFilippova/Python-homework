from abc import ABC  #, abstractmethod
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = int(weight)
        self.started = False
        #self.started = self.start(started)
        self.fuel = int(fuel)
        self.fuel_consumption = int(fuel_consumption)

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
            print(self.started)
        elif self.started:
            return self.started
        else:
            raise LowFuelError('Low fuel error!')

    def move(self, distance):
        if self.fuel >= distance * self.fuel_consumption:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel('Not enough fuel!')


# def main():
#     vehicle_1 = Vehicle(100, 1, 6)
#     distance = 500
#     print(vehicle_1.started)
#     print(vehicle_1.move(500))
#
#
# #print(vehicle_1.start())
#
# #print(vehicle_1.move())
# if __name__ == "__main__":
#     main()
