import numpy as np
import matplotlib
import matplotlib.pyplot as plots

import simulation
from simulation import evolve, apply_gravity, Body

plots.ion()

matplotlib.use('Qt5Agg')

fig, ax = plots.subplots(2)


p1 = Body(10 * np.float_power(10, 15), np.array([350, 500]), np.array([0, 0]))

p2 = Body(10 * np.float_power(10, 13), np.array([650, 500]), np.array([0, -45]))

bodies = [p1, p2]

# Simulation, calculating radius
x_space = np.linspace(0, 10, 10000)
ax[0].plot(x_space, simulation.simulate_radius(np.array(bodies), x_space, 0.1, np.array([0, 0]), np.array([0, -45])))
plots.show()

# Simulation, calculating plot on (x, y)
p1 = Body(10 * np.float_power(10, 15), np.array([350, 500]), np.array([0, 0]))

p2 = Body(10 * np.float_power(10, 13), np.array([650, 500]), np.array([0, -45]))

bodies = [p1, p2]


ax[1].set_xlim(0, 1000)
ax[1].set_ylim(0, 1000)
step = 0.1
graph, = ax[1].plot(5, 5, 'o')
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
