class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, param):
        if param > Glass.capacity - self.content:
            return f'Cannot add {param} ml'
        self.content = param
        return f'Glass filled with {param} ml'

    def empty(self):
        self.content -= self.content
        return 'Glass is now empty'

    def info(self):
        return f'{Glass.capacity - self.content} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
