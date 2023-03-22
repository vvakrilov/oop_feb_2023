from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int, ):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.workers: List[Worker] = []
        self.animals: List[Animal] = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker, ):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str, ):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_sum = sum([w.salary for w in self.workers])
        if not self.__budget >= salary_sum:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salary_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        care_sum = sum([a.money_for_care for a in self.animals])
        if not self.__budget >= care_sum:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= care_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount, ):
        self.__budget += amount

    @staticmethod
    def string_message(given_dict: dict, given_list: List[object]):
        msg = ""
        for k, v in given_dict.items():
            msg += f"----- {len([o for o in given_list if o.__class__.__name__ == k])} {v}:\n"
            msg += '\n'.join([str(o) for o in given_list if o.__class__.__name__ == k]) + '\n'
        return msg[:-1]  # cuts off last 'newline' => \n

    def animals_status(self):
        animals_order = {"Lion": "Lions", "Tiger": "Tigers", "Cheetah": "Cheetahs"}
        msg = f"You have {len(self.animals)} animals\n"
        msg += self.string_message(animals_order, self.animals)
        return msg

    def workers_status(self):
        workers_order = {"Keeper": "Keepers", "Caretaker": "Caretakers", "Vet": "Vets", }
        msg = f"You have {len(self.workers)} workers\n"
        msg += self.string_message(workers_order, self.workers)
        return msg
