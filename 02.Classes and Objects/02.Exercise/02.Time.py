class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    max_clock_time = {
        'hours': 23,
        'minutes': 59,
        'seconds': 59,
    }

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = {
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds,
        }

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        for _time, _digit in self.time.items():
            if len(str(_digit)) < 2:
                self.time[_time] = "0" + str(_digit)
            else:
                self.time[_time] = str(_digit)
        return f"{self.time['hours']}:{self.time['minutes']}:{self.time['seconds']}"

    def next_second(self):
        # TODO set right time if input exceeds max_time
        for t in ["seconds", "minutes", "hours"]:
            increased_time = self.time[t] + 1
            max_clock_time = Time.max_clock_time[t]
            if increased_time <= max_clock_time:
                self.time[t] = increased_time
                self.set_time(self.time['hours'], self.time['minutes'], self.time['seconds'])
                return self.get_time()
            else:
                self.time[t] = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
time = Time(24, 1, 59)
print(time.next_second())