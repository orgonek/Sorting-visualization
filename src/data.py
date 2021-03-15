import numpy as np

class DataGenerator:
    """ Class responsible for generating data for sorting  """
    def __init__(self, numbers : int = 50, max_value : int = 200):
        self.numbers = numbers
        self.max_value = max_value

    def random(self) -> list:
        """ Generates array with random values """
        return np.random.choice(range(self.max_value), self.numbers, replace = True)

    def reversed(self) -> list:
        """ Creates a reverse-ordered array """
        return sorted(np.random.randint(self.max_value, size=(self.numbers)), reverse=True)


    def part_sorted(self) -> list:
        """ Generates a partially ordered array """
        sorted = np.arange(1, np.random.randint(self.numbers // 2), 1)
        rand = np.random.choice(range(self.max_value), self.numbers - len(sorted), replace = True)
        return np.concatenate((sorted, rand))

