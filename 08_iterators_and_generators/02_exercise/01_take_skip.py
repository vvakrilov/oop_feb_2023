class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            i = self.i
            self.i += 1
            return i * self.step
        else:
            raise StopIteration()

#
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
