import random

class Mood:
    HAPPY = "happy"
    TIRED = "tired"
    STRESSED = "stressed"

class Person:
    def __init__(self, name, energy=100):
        self.name = name or "Безымянный"
        self.energy = energy
        self.mood = Mood.HAPPY

    def update_mood(self):
        if self.energy < 30:
            self.mood = Mood.TIRED
        elif self.energy > 80:
            self.mood = Mood.HAPPY
        else:
            self.mood = Mood.STRESSED

    def __str__(self):
        return f"{self.name} - {self.mood}"

    def __repr__(self):
        return self.name

class Student(Person):
    def __init__(self, name, energy=100, intelligence=50):
        super().__init__(name, energy)
        self.intelligence = intelligence
        self.rating = 0
        self.tasks_done = 0

    def attend_lecture(self, subject):
        if self.energy <= 0:
            return f"{self.name} МЕРТВ, но пришёл на {subject}"
        self.energy -= 10
        gain = random.randint(1, 5)
        self.intelligence += gain
        self.rating += 2
        return f"{self.name} был на {subject} (+{gain} IQ)"

    def do_homework(self, subject):
        self.energy -= random.randint(5, 15)
        score = self.intelligence // 10 + random.randint(-5, 10)
        self.rating += max(0, score // 5)
        return f"{self.name} сдал {subject} на {score}"

    def chat_with(self, other):
        try:
            self.energy += 5
            other.energy += 5
            return f"{self.name} и {other.name} поболтали"
        except:
            return "Ошибка общения"

    def __eq__(self, other):
        return self.name == other.name

class Professor(Person):
    def __init__(self, name, subject, energy=90):
        super().__init__(name, energy)
        self.subject = subject or "Неизвестный предмет"

    def conduct_lecture(self):
        self.energy -= 5
        return f"{self.name} читает {self.subject}"

    def check_homework(self, student_name, subject):
        grade = random.randint(2, 5)
        self.energy -= 3
        return f"{student_name} получил {grade} по {subject or '???'}"

    def __call__(self):
        print(f"{self.name} вызван!")
        return None