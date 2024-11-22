import random
import itertools

# Iterator zwracający 0, 1, 0, 1, 0, 1, ...
class Iterator01:
    def __init__(self):
        self.iterator = itertools.cycle([0, 1])  # Cykl 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

# Iterator zwracający przypadkowo jedną wartość z ("N", "E", "S", "W")
class RandomDirectionIterator:
    def __init__(self):
        self.directions = ["N", "E", "S", "W"]

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.directions)

# Iterator zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... (numery dni tygodnia)
class WeekdayIterator:
    def __init__(self):
        self.day = 0

    def __iter__(self):
        return self

    def __next__(self):
        day = self.day
        self.day = (self.day + 1) % 7
        return day


iter_01 = Iterator01()
print("Iterator 0, 1, 0, 1, 0, 1, ...:")
for _ in range(10):
    print(next(iter_01))

iter_random = RandomDirectionIterator()
print("\nIterator losowych kierunków (N, E, S, W):")
for _ in range(10):
    print(next(iter_random))

iter_weekday = WeekdayIterator()
print("\nIterator numerów dni tygodnia (0-6):")
for _ in range(10):
    print(next(iter_weekday))
