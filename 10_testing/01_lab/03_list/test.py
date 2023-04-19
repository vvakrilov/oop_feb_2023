from unittest import TestCase, main

from extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(*[1, 2, 3, 4, 5])

    def test_get_data_list(self):
        self.assertEqual([1, 2, 3, 4, 5], self.integer_list.get_data())


if __name__ == '__main__':
    main()
