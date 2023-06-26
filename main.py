import numpy as np
import matplotlib
import matplotlib.pyplot as plots
import scipy.optimize as opt

import simulation
from simulation import evolve, apply_gravity, Body

SECONDS = 150  # How long will the simulation last
STEPS = 150  # How many steps there will be
DESIDERED_DISTANCE = 300
#STEP = 0.1  # in seconds
STARTING_VELOCITY = (0, 80)

SIM_SPEED = 10




plots.ion()

matplotlib.use('Qt5Agg')


def create_bodies(velx, vely):
    p1 = Body(10 * np.float_power(10, 15), np.array([500, 500]), np.array([0, 0]))
    p2 = Body(10 * np.float_power(10, 13), np.array([500 + DESIDERED_DISTANCE, 500]), np.array([velx, vely]))

    return [p1, p2]



# Simulation, calculating radius
x_space = np.linspace(0, SECONDS, STEPS)
# ax[0].plot(x_space, simulation.simulate_radius(np.array(bodies), x_space, 0.1, np.array([0, 0]), np.array([0, -45])))
# plots.show()


def fit_func(x: np.ndarray[float], v2x: float, v2y: float):
    bodies = create_bodies(v2x, v2y)
    return simulation.simulate_radius(np.array(bodies), x, 0.5, np.array([0, 0]), np.array([v2x, v2y]))


popt, _ = opt.curve_fit(fit_func, x_space, np.full(STEPS, DESIDERED_DISTANCE), p0=STARTING_VELOCITY)
print('v1=(' + str(popt[0]) + ', ' + str(popt[1]) + ')') #', v2=(' + str(popt[2]) + ', ' + str(popt[3]) + ')')


fig, p = plots.subplots(2)

bx = p[0]
bx.plot(x_space, fit_func(x_space, *popt))


ax = p[1]
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
step = SECONDS/STEPS
graph, = ax.plot(5, 5, 'o')

current_time: float = 0.0

bodies = create_bodies(*popt)
while True:
    for i in range(0, len(bodies) - 1):
        for j in range(i+1, len(bodies)):
            apply_gravity(bodies[i], bodies[j])

    for body in bodies:
        graph.set_xdata(np.append(graph.get_xdata(), [body.get_position()[0]]))
        graph.set_ydata(np.append(graph.get_ydata(), [body.get_position()[1]]))
        evolve(step, body)

    current_time += step
    plots.draw()
    plots.pause(step / SIM_SPEED)


