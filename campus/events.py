import logging

def event_trigger(event_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[EVENT] {event_name}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

class SimulationDay:
    def __init__(self, day_num):
        self.day_num = day_num

    def __enter__(self):
        print(f"--- День {self.day_num} начался ---")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"--- День {self.day_num} закончился ---")