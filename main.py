from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from numpy import random
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort



NUMBERS = 30
X_AXIS = np.arange(1,31,1)
data = np.random.choice(range(100), NUMBERS, replace=False)

fig = plt.figure()
rects = plt.bar(X_AXIS, X_AXIS, color='#45b6fe')
plt.ylim(0, max(data))

def animate(i):
    for rect, value in zip(rects,data):
        rect.set_height(value)

    return rect


anim = animation.FuncAnimation(fig, animate, frames = bubble_sort(data), interval=150)
plt.show()