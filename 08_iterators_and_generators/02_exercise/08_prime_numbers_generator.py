import math
from typing import List


def get_primes(numbers: List[int]):
    for num in numbers:
        if num <= 1:
            continue
        for next_num in range(2, int(math.sqrt(num)) + 1):
            if num % next_num == 0:
                break
        else:
            yield num


# import sympy
#
#
# def get_primes(numbers):
#     for num in numbers:
#         if sympy.isprime(num):
#             yield num


# test zero
import unittest


class Tests(unittest.TestCase):
    def test_zero(self):
        res = list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
        self.assertEqual(res, [2, 3, 5])


if __name__ == '__main__':
    unittest.main()
