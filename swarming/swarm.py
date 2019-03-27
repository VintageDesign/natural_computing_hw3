import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import random
import math


class Particle_Swarm:

    def __init__(self, pop_size, v_min, v_max):
        """
        Initialzes particles
        """

        if v_min > v_max:
            raise Exception('V_min cannot be bigger than V_max')

        self.v_min = v_min
        self.v_max = v_max

        for individual in range(0,pop_size):
            self.particles.append(np.random.rand(0,1))
            self.velocities.append(np.random.rand(v_min,v_max))




    def evaluate(self, x): # This is g() in the book
        y = float((x - .1)/.9)
        y = math.pow(y, 2.0)
        y = math.pow(2.0,(-2.0 * y) )
        y = y * math.pow(math.sin(5*math.pi*x), 6)
        return y;


    def run(self, max_iterations):
        j = 0
        while (j < max_iterations):
            for particle in self.swarm:
                phi1 = 0.1 + np.random.randn()
                phi2 = 0.1 + np.random.randn()

                particle_location = particle.getLocation()

                curr_velocity = particle.getVelocity() + \
                    (phi1 * (particle.getPBest() - curr_solution) + phi2 * (self.gBest - curr_solution))

                particle.setVelocity(curr_velocity)

                if (curr_solution + curr_velocity > 0) and (curr_solution + curr_velocity < 2):
                    curr_solution += curr_velocity


    def plot(point, path, wait):
        plt.clf()
        if (path == 1):
            plt.plot(point[0], point[1], color='red', zorder=0, label='Approximate')
            plt.plot(.1, evaluate(.1),color='blue', label='Actual')
        plt.scatter(point[0], point[1], marker='o')
        plt.scatter(.1, evaluate(.1),marker='^')
        plt.xlim(-.1,1.1)
        plt.ylim(-.5,1.5)
        plt.axis('on')
        if (wait == 0):  plt.ion()
        leg = plt.legend()
        plt.show()
        plt.pause(.001)

