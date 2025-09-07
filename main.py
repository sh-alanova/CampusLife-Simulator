import logging
from dotenv import load_dotenv
import os
import sys
sys.path.append(".")

load_dotenv("config.env")

log_level = os.environ.get("LOG_LEVEL", "DEBUG")
logging.basicConfig(level=log_level)

print("🎓 Запуск симулятора...")

students = [
    Student("Алиса", energy=80, intelligence=70),
    Student("Боб", energy=60, intelligence=90),
    Student(None, energy=50, intelligence=50),
]

professors = [
    Professor("Доктор Смит", subject="Python"),
    Professor("Профессор Ли", subject="Алгоритмы"),
]

sim = CampusSimulation(tuple(students), tuple(professors))

try:
    for day_num, day_log in enumerate(sim.simulate_week(), 1):
        print(f"\n📆 День {day_num}")
        for event in day_log:
            print(" -> " + event)
except Exception as e:
    print("Ошибка в симуляции:", e)

print("\n📊 Рейтинги:")
for i, student in enumerate(students):
    if student:
        print(f"{i+1}. {student.name or '???'}: {student.rating} (энергия: {student.energy})")
    else:
        print(f"{i+1}. ????: ???")
