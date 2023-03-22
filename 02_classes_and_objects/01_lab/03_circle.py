class Circle:
    PI = 3.14

    def __init__(self, radius: int, ):
        self.radius = radius

    def set_radius(self, param):
        self.radius = param

    def get_area(self):
        return Circle.PI * self.radius ** 2

    def get_circumference(self):
        return 2 * Circle.PI * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
