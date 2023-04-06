class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary: dict = dictionary
        self.i = 0
        self.dict_len = len(self.dictionary) - 1
        self.dict_to_list = list((k, v) for k, v in self.dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.dict_len:
            i = self.i
            self.i += 1
            return self.dict_to_list[i]
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
