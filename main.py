from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from numpy.core.fromnumeric import repeat
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort




NUMBERS = 100
X_AXIS = np.arange(1,101,1)
data = np.random.choice(range(100), NUMBERS, replace=False)

fig = plt.figure()
rects = plt.bar(X_AXIS, X_AXIS, color='#fda4ba')
plt.ylim(0, max(data))

def animate(i):
    for rect, value in zip(rects,data):
        rect.set_height(value)
    return rect


anim = animation.FuncAnimation(fig, animate, frames = merge_sort(data,0, 100), interval=1, repeat=False)
plt.show()