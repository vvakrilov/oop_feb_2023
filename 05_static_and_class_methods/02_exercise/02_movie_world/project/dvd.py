import datetime


class DVD:
    name: str
    id: int
    creation_year: int
    creation_month: str
    age_restriction: int
    is_rented: bool

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _, month, year = date.split('.')
        x = datetime.datetime(int(year), int(month), int(_))
        return cls(name, id, int(year), x.strftime("%B"), age_restriction)

    def __repr__(self):
        _id, _name, _mont, _year, _restr = \
            self.id, self.name, self.creation_month, self.creation_year, self.age_restriction

        def is_rented(r):
            if r:
                return 'rented'
            return 'not rented'

        return f"{_id}: {_name} ({_mont} {_year}) has age restriction {_restr}. Status: {is_rented(self.is_rented)}"
