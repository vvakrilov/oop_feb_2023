from project.services.base_service import BaseService


class MainService(BaseService):
    SERVICE_CAPACITY = 30

    def __init__(self, name: str, ):
        super().__init__(name, self.SERVICE_CAPACITY)

    def details(self):
        robots = [r.name for r in self.robots]
        message = f"{self.name} Main Service:\n"f"Robots: {' '.join(robots) if robots else 'none'}"
        return message
