"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        if self.max_cargo >= self.cargo + value:
            self.cargo += value
        else:
            raise CargoOverload("Cargo over load!")

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo


# def main():
#     plain_1 = Plane(100,100,1,400)
#     print(plain_1.load_cargo(5))
#
# if __name__ == "__main__":
#     main()
