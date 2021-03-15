from data import DataGenerator
from visualizer import Visualizer

g = DataGenerator()
data = g.reversed()
v = Visualizer(data)
v.visualize_algorithm('quick_sort')

