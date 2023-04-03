from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    name: str
    customers: List
    dvds: List

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    @staticmethod
    def get_obj(obj_id, obj_list):
        obj = [obj for obj in obj_list if obj.id == obj_id]
        if obj:
            return obj[0]

    def get_customer(self, customer_id: int):
        return self.get_obj(customer_id, self.customers)

    def get_dvd(self, dvd_id: int):
        return self.get_obj(dvd_id, self.dvds)

    def rent_dvd(self, customer_id: int, dvd_id):

        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)

        if self.get_obj(dvd_id, customer.rented_dvds):
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):

        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)

        if self.get_obj(dvd_id, customer.rented_dvds):
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    @staticmethod
    def str_repr(obj):
        return '\n'.join(str(s) for s in obj)

    def __repr__(self):
        str_repr = ''
        str_repr += self.str_repr(self.customers) + '\n'
        str_repr += self.str_repr(self.dvds)
        return str_repr
