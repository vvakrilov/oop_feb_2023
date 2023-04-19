from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    ROBOT_WEIGHT = 9
    WEIGHT_INCREASE = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.ROBOT_WEIGHT)

    def eating(self):
        self.weight += self.WEIGHT_INCREASE
