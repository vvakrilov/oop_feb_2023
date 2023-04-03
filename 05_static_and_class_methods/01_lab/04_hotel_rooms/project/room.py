class Room:
    number: int
    capacity: int
    guests: int
    is_taken: bool
    free_space: int

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False
        self.free_space = self.capacity - self.guests

    def take_room(self, people: int):
        if self.is_taken or people > self.free_space:
            return f"Room number {self.number} cannot be taken"
        self.guests = people
        self.is_taken = True

    def free_room(self):
        if self.is_taken is False:
            return f"Room number {self.number} is not taken"
        self.guests = 0
        self.is_taken = False
