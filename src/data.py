import numpy as np

class DataGenerator:
    def __init__(self, numbers : int = 50, max_value : int = 100):
        self.numbers = numbers
        self.max_value = max_value

    def random(self) -> list:
        return np.random.choice(range(self.max_value), self.numbers, replace = True)

    def reversed(self) -> list:
        return np.arange(self.max_value, self.max_value - self.numbers, -1)

    def part_sorted(self) -> list:
        sorted = np.arange(1, np.random.randint(self.numbers // 2), 1)
        rand = np.random.choice(range(self.max_value), self.numbers - len(sorted), replace = True)
        return np.concatenate((sorted, rand))

