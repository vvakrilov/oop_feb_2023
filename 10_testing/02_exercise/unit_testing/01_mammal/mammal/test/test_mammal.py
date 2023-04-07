from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    unittest_str_name = 'unittest string name'
    unittest_str_type = 'unittest string type'
    unittest_str_sound = 'unittest string sound'
    unittest_private_attribute = "animals"

    def setUp(self):
        self.mammal = Mammal(
            self.unittest_str_name,
            self.unittest_str_type,
            self.unittest_str_sound,
        )

    def test_true_initialization(self):
        self.assertEqual(self.unittest_str_name, self.mammal.name)
        self.assertEqual(self.unittest_str_type, self.mammal.type)
        self.assertEqual(self.unittest_str_sound, self.mammal.sound)

    def test_do_make_sound_return_correct_message(self):
        expected_return = f"{self.unittest_str_name} makes {self.unittest_str_sound}"
        test_case_return = self.mammal.make_sound()
        self.assertEqual(expected_return, test_case_return)

    def test_do_get_kingdom_return_kingdom(self):
        expected_return = self.unittest_private_attribute
        test_case_return = self.mammal.get_kingdom()
        self.assertEqual(expected_return, test_case_return)

    def test_do_info_return_correct_message(self):
        expected_return = f"{self.unittest_str_name} is of type {self.unittest_str_type}"
        test_case_return = self.mammal.info()
        self.assertEqual(expected_return, test_case_return)


if __name__ == '__main__':
    main()
