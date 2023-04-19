from project.toy_store import ToyStore

from unittest import TestCase, main


class TestToyStore(TestCase):
    test_toy_shelf_dict = {
        "A": None,
        "B": None,
        "C": None,
        "D": None,
        "E": None,
        "F": None,
        "G": None,
    }

    def setUp(self):
        self.toy_store = ToyStore()
        self.assertEqual(self.test_toy_shelf_dict, self.toy_store.toy_shelf)


if __name__ == '__main__':
    main()
