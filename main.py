import numpy as np
import matplotlib
import matplotlib.pyplot as plots
from simulation import evolve, Body as Body

plots.ion()

matplotlib.use('Qt5Agg')

fig, ax = plots.subplots()

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
graph, = ax.plot(5, 5, 'o')

plots.show()

p1 = Body(50, np.array([5, 5]), np.array([5, 5]))
p1.set_acceleration(np.array([5, 0]))

p2 = Body(50000, np.array([50, 50]), np.array([-5, -5]))

bodies = [p1, p2]

step = 0.1
while True:
    for body in bodies:
        graph.set_xdata(np.append(graph.get_xdata(), [body.get_position()[0]]))
        graph.set_ydata(np.append(graph.get_ydata(), [body.get_position()[1]]))
        evolve(step, body)

    plots.draw()
    plots.pause(0.01)
