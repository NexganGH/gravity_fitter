import numpy as np
import matplotlib
import matplotlib.pyplot as plots
import scipy.optimize as opt

import simulation
from simulation import evolve, apply_gravity, Body
import fitter
from initialiser import *

plots.ion()
matplotlib.use('Qt5Agg')

# This places #steps amount of points from 0 to #seconds, thus creating a total amount of #steps points.
# Each step will therefore #seconds/#steps amount of seconds.
x_space = np.linspace(0, SECONDS, CHECKS)



popt, _ = opt.curve_fit(fitter.fit_func, x_space, np.full(CHECKS, DESIRED_DISTANCE),
                        p0=(STARTING_VELOCITY))

print('BEST VALUES ARE v1=(' + str(popt[0]) + ', ' + str(popt[1]) + ')')
#print('BEST VALUES ARE m1=' + str(popt[2]) + ' m2=' + str(popt[3]))

# Creating 2 subplots. One is to see the radius changing with time, the other display the two bodies in (x,y)
fig, p = plots.subplots(2)

# Drawing the first graph with the best parameters
p0 = p[0]
p0.plot(x_space, fitter.fit_func(x_space, *popt))


p1 = p[1]
p1.set_xlim(0, 2000)
p1.set_ylim(0, 2000)
step = SECONDS / CHECKS
graph, = p1.plot(5, 5, 'o')

current_time: float = 0.0

bodies = create_bodies(*popt, M1, M2)
while True:
    for i in range(0, len(bodies) - 1):
        for j in range(i+1, len(bodies)):
            apply_gravity(bodies[i], bodies[j])

    for body in bodies:
        graph.set_xdata(np.append(graph.get_xdata(), [body.get_position()[0]]))
        graph.set_ydata(np.append(graph.get_ydata(), [body.get_position()[1]]))
        evolve(step, body)

    current_time += step
    p1.relim()
    p1.autoscale()
    plots.draw()
    plots.pause(step / SIM_SPEED)


