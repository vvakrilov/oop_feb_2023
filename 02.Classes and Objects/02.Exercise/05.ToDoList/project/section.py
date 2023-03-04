from typing import List
from project.task import Task


def get_task(name, tasks) -> list:
    return [t for t in tasks if t.name == name]


class Section:
    def __init__(self, name: str, ):
        self.name = name
        self.tasks: List = []

    def add_task(self, new_task: Task):
        task = get_task(new_task.name, self.tasks)
        # if new_task.name not in [t.name for t in self.tasks]:
        if task:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task = get_task(task_name, self.tasks)
        if task:
            task[0].completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [self.tasks.remove(x) for x in self.tasks if x.completed is True]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        new_row = '\n'
        information = f"Section {self.name}:\n{new_row.join([t.details() for t in self.tasks])}"
        return information
