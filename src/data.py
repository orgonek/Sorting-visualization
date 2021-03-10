import numpy as np
from numpy.core.defchararray import replace

class DataGenerator:
    def __init__(self, numbers : int = 50, max_value : int = 100):
        self.numbers = numbers
        self.max_value = max_value

    def random(self) -> list:
        return np.random.choice(range(self.max_value), self.numbers, replace = False)

