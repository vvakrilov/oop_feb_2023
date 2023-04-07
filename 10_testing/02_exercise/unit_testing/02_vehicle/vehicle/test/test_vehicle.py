from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    unittest_default_fuel_consumption = 1.25
    unittest_fuel_consumption = unittest_default_fuel_consumption
    unittest_fuel = 111.11
    unittest_capacity = unittest_fuel
    unittest_horse_power = 123.45
    unittest_not_enough_fuel_ex_msg = "Not enough fuel"
    unittest_too_much_fuel_ex_msg = "Too much fuel"

    def setUp(self):
        self.vehicle = Vehicle(self.unittest_fuel, self.unittest_horse_power)

    def test_default_class_value_in_this_case_default_fuel_consumption(self):
        self.assertEqual(self.unittest_default_fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_init_sets_correct_values(self):
        self.assertEqual(self.unittest_fuel, self.vehicle.fuel)
        self.assertEqual(self.unittest_horse_power, self.vehicle.horse_power)
        self.assertEqual(self.unittest_capacity, self.vehicle.capacity)
        self.assertEqual(self.unittest_capacity, self.vehicle.fuel)
        self.assertEqual(self.unittest_fuel_consumption, self.vehicle.fuel_consumption)
        self.assertEqual(self.unittest_default_fuel_consumption, self.vehicle.fuel_consumption)

    def test_do_drive_method_set_correct_fuel_subtraction(self):
        test_case_kilometers = 10
        test_case_fuel_needed = self.unittest_fuel_consumption * test_case_kilometers
        test_case_result = self.unittest_fuel - test_case_fuel_needed
        self.vehicle.drive(test_case_kilometers)
        self.assertEqual(test_case_result, self.vehicle.fuel)

    def test_do_drive_method_raise_exception_message(self):
        self.vehicle.capacity, self.vehicle.fuel = 0, 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1)
        self.assertEqual(self.unittest_not_enough_fuel_ex_msg, str(ex.exception))

    def test_do_refuel_method_refill_correct_amount_of_fuel(self):
        self.vehicle.fuel, self.vehicle.capacity = 0, 10
        self.assertEqual(10, self.vehicle.capacity)
        self.vehicle.refuel(1)
        self.assertEqual(1, self.vehicle.fuel)

    def test_do_refuel_method_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual(self.unittest_too_much_fuel_ex_msg, str(ex.exception))

    def test_do__str__method_return_correct_message(self):
        test_case_msg = f"The vehicle has {self.unittest_horse_power} " \
                        f"horse power with {self.unittest_fuel} fuel left and {self.unittest_fuel_consumption} fuel consumption"
        self.assertEqual(test_case_msg, str(self.vehicle))


if __name__ == '__main__':
    main()
