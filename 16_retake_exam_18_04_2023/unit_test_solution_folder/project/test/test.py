from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot("ID1", "Military", 100, 100)
        self.robot2 = Robot("ID2", "Education", 90, 90)

    def test_class_attributes(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_correct_initialization(self):
        self.assertEqual("ID1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_value_error_on_not_allowed_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "BUG"
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_value_less_than_zero_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -100
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_returns_the_robot_was_not_upgraded(self):
        self.robot.hardware_upgrades = ["RAM"]
        result = self.robot.upgrade("RAM", 10)
        self.assertEqual("Robot ID1 was not upgraded.", result)

    #
    def test_successful_upgrade(self):
        self.robot.hardware_upgrades = []
        result = self.robot.upgrade("RAM", 10)
        self.assertEqual(["RAM"], self.robot.hardware_upgrades)
        self.assertEqual(115, self.robot.price)
        self.assertEqual('Robot ID1 was upgraded with RAM.', result)

    def test_unsuccessful_lesser_version_update(self):
        self.robot.software_updates = [1.0, 1.1]
        result = self.robot.update(1.0, 10)
        self.assertEqual([1.0, 1.1], self.robot.software_updates)
        self.assertEqual("Robot ID1 was not updated.", result)

    def test_unsuccessful_update_less_than_available_capacity(self):
        self.robot.software_updates = [1.0, 1.1]
        self.robot.available_capacity = 30
        result = self.robot.update(1.3, 50)
        self.assertEqual([1.0, 1.1], self.robot.software_updates)
        self.assertEqual("Robot ID1 was not updated.", result)

    def test_successful_first_update(self):
        result = self.robot.update(1.0, 10)
        self.assertEqual('Robot ID1 was updated to version 1.0.', result)

    def test_successful_second_update(self):
        self.robot.software_updates = [1.0]
        self.robot.available_capacity = 90
        result = self.robot.update(1.1, 10)
        self.assertEqual([1.0, 1.1], self.robot.software_updates)
        self.assertEqual(80, self.robot.available_capacity)
        self.assertEqual('Robot ID1 was updated to version 1.1.', result)

    def test_grater_then_by_price_returns_true_statement(self):
        # setUp case
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID ID1 is more expensive than Robot with ID ID2.', result)

    def test_equal_then_by_price_returns_equal_statement(self):
        self.robot.price = self.robot2.price
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID ID1 costs equal to Robot with ID ID2.', result)

    def test_grater_then_by_price_returns_false_statement(self):
        self.robot2.price += self.robot.price
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID ID1 is cheaper than Robot with ID ID2.', result)


if __name__ == '__main__':
    main()
