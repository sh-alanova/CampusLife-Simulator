from .utils import simulate_week_generator
from .events import event_trigger

class CampusSimulation:
    def __init__(self, students, professors):
        self.students = students
        self.professors = professors

    @event_trigger("SIMULATION_START")
    def simulate_week(self):
        return simulate_week_generator(self.students, self.professors)

    def add_student(self, student):
        self.students.append(student)
