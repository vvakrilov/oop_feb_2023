from typing import List
from itertools import permutations


def possible_permutations(numbers: List[int]):
    for number in list(permutations(numbers)):
        yield list(number)


[print(n) for n in possible_permutations([1, 2, 3])]

