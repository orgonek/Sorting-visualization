from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from algorithms.quick_sort import quick_sort
from data import DataGenerator


NUMBERS = 50
X_AXIS = np.arange(1,51,1)
generator = DataGenerator(NUMBERS, max_value=100)
data =  generator.random()

fig = plt.figure()
rects = plt.bar(X_AXIS, X_AXIS, color='#fda4ba')
plt.ylim(0, max(data))

def animate(i):
    for rect, value in zip(rects,data):
        rect.set_height(value)
    return rect


anim = animation.FuncAnimation(fig, animate, frames = quick_sort(data, 0, len(data)-1), interval=1, repeat=False)
plt.show()