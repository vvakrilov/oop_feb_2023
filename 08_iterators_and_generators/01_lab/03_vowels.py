class vowels:
    def __init__(self, string: str):
        self.string = string
        self.i = 0
        self._vowels = "aeiouyw"

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= len(self.string) - 1:
            i = self.i
            el = self.string[i]
            self.i += 1
            return el if el.lower() in self._vowels else self.__next__()
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
