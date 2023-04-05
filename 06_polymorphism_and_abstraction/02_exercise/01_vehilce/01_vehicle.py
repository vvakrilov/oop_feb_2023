from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        trip_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER)
        if not self.fuel_quantity <= trip_fuel:
            self.fuel_quantity -= trip_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER = 1.6
    FUEL_TANK_TINY_HOLE = .95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        trip_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER)
        if not self.fuel_quantity <= trip_fuel:
            self.fuel_quantity -= trip_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_TANK_TINY_HOLE


print("*" * 20)
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print("*" * 20)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
print("*" * 20)

# test car
import unittest


class VehiclesTests(unittest.TestCase):
    def test_first_zero(self):
        car = Car(20, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 2.299999999999997)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 12.299999999999997)


if __name__ == '__main__':
    unittest.main()
