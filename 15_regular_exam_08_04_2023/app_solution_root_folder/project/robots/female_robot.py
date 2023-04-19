from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    ROBOT_WEIGHT = 8
    WEIGHT_INCREASE = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.ROBOT_WEIGHT)

    def eating(self):
        self.weight += self.WEIGHT_INCREASE
