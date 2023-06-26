import numpy as np
import matplotlib
import matplotlib.pyplot as plots
from simulation import evolve, apply_gravity, Body

plots.ion()

matplotlib.use('Qt5Agg')

fig, ax = plots.subplots()

ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
graph, = ax.plot(5, 5, 'o')

plots.show()

p1 = Body(10 * np.float_power(10, 15), np.array([350, 500]), np.array([0, 0]))

p2 = Body(10 * np.float_power(10, 13), np.array([650, 500]), np.array([0, -45]))

bodies = [p1, p2]

step = 0.1
while True:
    for i in range(0, len(bodies) - 1):
        for j in range(i+1, len(bodies)):
            apply_gravity(bodies[i], bodies[j])

    for body in bodies:
        graph.set_xdata(np.append(graph.get_xdata(), [body.get_position()[0]]))
        graph.set_ydata(np.append(graph.get_ydata(), [body.get_position()[1]]))
        evolve(step, body)

    plots.draw()
    plots.pause(0.01)
