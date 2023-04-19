from typing import List

from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPE = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[CargoVan, PassengerCar] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str, ):
        if list(filter(lambda l: l.driving_license_number == driving_license_number, self.users)):
            return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPE:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if list(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles)):
            return f"{license_plate_number} belongs to another vehicle."
        vehicle = self.VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point:
                if r.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                if r.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                if r.length > length:
                    r.is_locked = True
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, d_l_n: str, l_p_n: str, route_id: int, is_accident_happened: bool):
        if list(filter(lambda d: (d.is_blocked is True and d.driving_license_number == d_l_n), self.users)):
            return f"User {d_l_n} is blocked in the platform! This trip is not allowed."
        if list(filter(lambda v: (v.is_damaged is True and v.license_plate_number == l_p_n), self.vehicles)):
            return f"Vehicle {l_p_n} is damaged! This trip is not allowed."
        if list(filter(lambda r: (r.is_locked is True and r.route_id == route_id), self.routes)):
            return f"Route {route_id} is locked! This trip is not allowed."

        given_user = [u for u in self.users if u.driving_license_number == d_l_n][0]
        given_route = [r for r in self.routes if r.route_id == route_id][0]
        given_vehicle = [v for v in self.vehicles if v.license_plate_number == l_p_n][0]

        given_vehicle.drive(given_route.length)
        if is_accident_happened:
            given_vehicle.is_damaged = True
            given_user.decrease_rating()
        else:
            given_user.increase_rating()
        return str(given_vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged is True]
        damaged_vehicles.sort(key=lambda x: (x.brand, x.model))
        damaged_vehicles = damaged_vehicles[:count]
        for vehicle in damaged_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()
        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sort_users = self.users
        sort_users.sort(key=lambda u: u.rating, reverse=True)
        joined = '\n'.join(str(u) for u in sort_users)
        return f"*** E-Drive-Rent ***\n{joined}"


app = ManagingApp()
print(app.register_user('Tisha', 'Reenie', '7246506'))
print(app.register_user('Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user('Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle('PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
