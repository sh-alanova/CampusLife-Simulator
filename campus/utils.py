import time
import os
import random

def simulate_delay():
    try:
        speed = int(os.getenv("SIMULATION_SPEED", "1"))
        if speed == 1:
            time.sleep(1)
    except:
        pass

def simulate_week_generator(students, professors, days=5):
    subjects = ["Python", "Алгоритмы", "Базы данных"]

    def generate_day(day_num):
        events = []
        sd = SimulationDay(day_num)
        sd.__enter__()

        for prof in professors:
            events.append(prof.conduct_lecture())
            for student in students:
                if student.energy > 0:
                    events.append(student.attend_lecture(prof.subject))

        for i in range(len(students)):
            for j in range(i+1, len(students)):
                if random.random() > 0.8:
                    events.append(students[i].chat_with(students[j]))

        subject = random.choice(subjects)
        for student in students:
            if student.energy > 20:
                events.append(student.do_homework(subject))
                checker = random.choice(professors)
                events.append(checker.check_homework(student.name, subject))

        sd.__exit__(None, None, None)
        return events

    result = []
    for day in range(1, days+1):
        result.append(generate_day(day))
    return result
