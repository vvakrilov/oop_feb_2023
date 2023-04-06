class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end = 0
        self.last = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.last >= self.end:
            current_value = self.last
            self.last -= 1
            return current_value
        else:
            raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
