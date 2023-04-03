from typing import List
from project.room import Room


class Hotel:
    name: str
    rooms: List[Room]
    guests: int

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        new_hotel = f"{stars_count} stars Hotel"
        return cls(new_hotel)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [r.take_room(people) for r in self.rooms if r.number == room_number][0]
        if not isinstance(room, str):
            self.guests += people

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        """
        :return:
        "Hotel {name} has {guests} total guests
        Free rooms: {numbers of all free rooms separated by comma and space}
        Taken rooms: {numbers of all taken rooms separated by comma and space}"
        """
        free_rooms = ""
        occupied_rooms = ""
        for r in self.rooms:
            if r.is_taken:
                occupied_rooms += str(r.number)
            else:
                free_rooms += str(r.number)

        message = f"Hotel {self.name} has {self.guests} total guests\n" \
                  f"Free rooms: " + ', '.join(free_rooms) + '\n' + \
                  f"Taken rooms: " + ', '.join(occupied_rooms)

        return message

#
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# print(hotel.status())
