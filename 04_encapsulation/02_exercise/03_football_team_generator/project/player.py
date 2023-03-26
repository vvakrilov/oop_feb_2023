class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        nm, sp, dr, pa, sh = self.name, self.__sprint, self.__dribble, self.__passing, self.__shooting
        msg = f"Player: {nm}\nSprint: {sp}\nDribble: {dr}\nPassing: {pa}\nShooting: {sh}"
        return msg

