#!/bin/python3

import random as rand
import numpy as np
import matplotlib.pyplot as plt

n_events = 10000001
R = 1
n_events_array = np.linspace(1, n_events, n_events)
x_array = []
y_array = []
circle_area = 0
ratio = []
square_area = np.arange(0.25, n_events / 4 + 0.25, 0.25)

for i in range(n_events):
    x = rand.uniform(-R, R)
    y = rand.uniform(-R, R)
    x_array.append(x)
    y_array.append(y)


def inside_circle(x_value, y_value):
    if (x_value ** 2 + y_value ** 2) <= (R ** 2):
        return True
    else:
        return False


for n in range(n_events):
    if inside_circle(x_array[n], y_array[n]):
        circle_area += 1
    ratio.append(circle_area / square_area[n])

plt.plot(n_events_array, ratio, color='orange', linewidth=0.5)
plt.axhline(y=np.pi, color='black', linestyle='dashed', linewidth=0.5)
plt.ylim(3.1, 3.2)
plt.title(f'Estimate of π using Monte Carlo methods: {ratio[n_events - 1]}')
plt.xlabel(f'Iterations')
plt.ylabel('Area Ratio ($\mathregular{πR^{2}/R^{2}}$)')
plt.savefig('pi_estimate.png')
plt.show()
