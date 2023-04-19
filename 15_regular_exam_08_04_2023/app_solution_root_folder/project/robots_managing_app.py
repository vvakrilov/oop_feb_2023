from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    ROBOTS_TYPES = {
        "FemaleRobot": FemaleRobot,
        "MaleRobot": MaleRobot}
    SERVICES_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService}
    ROBOT_SERVICES = {
        "FemaleRobot": "SecondaryService",
        "MaleRobot": "MainService"}

    def __init__(self):
        self.robots: List = []
        self.services: List = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICES_TYPES:
            raise Exception("Invalid service type!")
        new_service = self.SERVICES_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOTS_TYPES:
            raise Exception("Invalid robot type!")
        new_robot = self.ROBOTS_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    @staticmethod
    def get_object_by_name(obj_key, obj_list):
        is_object = [o for o in obj_list if o.name == obj_key]
        if is_object:
            return is_object[0]

    @staticmethod
    def get_type_of_object(obj):
        return type(obj).__name__

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = self.get_object_by_name(service_name, self.services)
        robot = self.get_object_by_name(robot_name, self.robots)
        robot_type = self.get_type_of_object(robot)
        service_type = self.get_type_of_object(service)
        if self.ROBOT_SERVICES[robot_type] != service_type:
            return "Unsuitable service."
        elif service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.get_object_by_name(service_name, self.services)
        robot = self.get_object_by_name(robot_name, service.robots)
        if not robot:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.get_object_by_name(service_name, self.services)
        [robot.eating() for robot in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.get_object_by_name(service_name, self.services)
        robots_service_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {robots_service_price:.2f}."

    def __str__(self):
        message = '\n'.join(s.details() for s in self.services)
        return message


# main_app = RobotsManagingApp()
# print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
# print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
# print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
# print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
#
# print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))
#
# print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
# print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
#
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))
#
# print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))
