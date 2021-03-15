from data import DataGenerator
from visualizer import Visualizer

g = DataGenerator()
data = g.random()
v = Visualizer(data)
v.visualize_algorithm('insertion_sort')