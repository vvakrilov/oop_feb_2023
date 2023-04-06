class sequence_repeat:
    zero_index = -1

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_index = self.zero_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == self.number - 1:
            raise StopIteration
        self.current_index += 1
        return self.sequence[self.current_index % len(self.sequence)]
        # MY WORKING SOLUTION
        # if self.zero_index <= self.current_index <= self.number - 1:
        #     i = self.current_index
        #     if i > len(self.sequence) - 1:
        #         self.number -= len(self.sequence)
        #         self.current_index = self.zero_index
        #         return self.__next__()
        #     self.current_index += 1
        #     return self.sequence[i]
        # else:
        #     raise StopIteration()

# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
