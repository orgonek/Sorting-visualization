from src.data import DataGenerator

class TestDataGenerator:
    """ Class containing tests for generating data """

    def test_instance(self):
        g = DataGenerator()
        assert type(g) is DataGenerator

    def test_random_data_length(self):
        g = DataGenerator(50, max_value=250)
        data = g.random()
        assert len(data) == 50

    def test_random_data_max(self):
        g = DataGenerator(50, max_value=550)
        data = g.random()
        assert max(data) <= 550

    def test_reversed_default(self):
        g = DataGenerator()
        data = g.reversed()
        assert len(data) == 50