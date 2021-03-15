import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from numpy.core.fromnumeric import repeat
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.selection_sort import selection_sort


class Visualizer:

    def __init__(self, data : list):
        self.data = data
        self.fig = plt.figure()
        self.x_axis = np.arange(1, len(self.data) + 1, 1)
        self.rects = plt.bar(self.x_axis, max(self.data), color='#00FF00')
    
    def visualize_algorithm(self, name : str = 'insertion_sort'):
        options = {
            'insertion_sort' : insertion_sort(self.data),
            'bubble_sort' : bubble_sort(self.data),
            'selection_sort' : selection_sort(self.data),
            'quick_sort' : quick_sort(self.data, 0, len(self.data)-1),
            'merge_sort' : merge_sort(self.data, 0, len(self.data))
        }

        algorithm = options[name]

        self.ani = animation.FuncAnimation(self.fig, func=self._update_animation, frames=algorithm, interval=1, repeat=False)
        plt.show()


    def _update_animation(self, i):
        for rect, value in zip(self.rects, self.data):
            rect.set_height(value)
        return rect
