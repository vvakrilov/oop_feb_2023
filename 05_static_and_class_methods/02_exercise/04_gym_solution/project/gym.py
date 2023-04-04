from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    customers: list
    trainers: list
    equipment: list
    plans: list
    subscriptions: list

    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        #   - add the customer in the customer list if the customer is not already in it
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        # - add the trainer to the trainers' list, if the trainer is not already in it
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        # add the equipment to the equipment list, if the equipment is not already in it
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        # add the plan to the plans' list, if the plan is not already in it
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        # add the subscription in the subscriptions list if the subscription is not already in it
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        attr_order = [self.subscriptions, self.customers, self.trainers, self.equipment, self.plans]
        str_list = []
        for attr in attr_order:
            for obj in attr:
                if obj.id == subscription_id:
                    str_list.append(repr(obj))
        return '\n'.join(x for x in str_list)
