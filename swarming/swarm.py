import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import random
import math


class Particle_Swarm:

    def __init__(self, pop_size, v_min, v_max):
        """
        Initializes particles
        """

        if v_min > v_max:
            raise Exception('V_min cannot be bigger than V_max')

        self.v_min = v_min
        self.v_max = v_max
        self.swarm = []
        self.velocity = []
        self.bestind = []
        self.fitness = []
        self.fitbest = []

        for individual in range(pop_size):
            x = np.random.rand()
            fit = self.evaluate(x)

            self.swarm.append(x)
            self.velocity.append(np.random.uniform(v_min,v_max))
            self.fitness.append(fit)
            
            self.bestind.append(x)
            self.fitbest.append(fit)

        self.best = self.swarm[self.fitness.index(min(self.fitness))]
        self.top = min(self.fitness)


    def evaluate(self, x): # This is g() in the book
        exponent = -2 * (((x-0.1)/0.9) ** 2)
        num = (2 ** exponent) * (math.sin(5 * math.pi * x) ** 6)
        return num
        #y = float((x - 0.1)/0.9)
        #y = math.pow(y, 2.0)
        #y = math.pow(2.0,(-2.0 * y) )
        #y = y * math.pow(math.sin(5*math.pi*x), 6)
        #return y;


    def run(self, max_iterations):
        j = 0
        while (j < max_iterations):
            for i in range(len(self.swarm)):
                phi1 = 0.1 + np.random.randn()
                phi2 = 0.1 + np.random.randn()

                self.velocity[i] += phi1 + (self.bestind[i] - self.swarm[i]) + phi2 + (self.best - self.swarm[i])
                if (self.swarm[i] + self.velocity[i] > 0) and (self.swarm[i] + self.velocity[i] < 1):
                    self.swarm[i] += self.velocity[i]
                    self.fitness[i] = self.evaluate(self.swarm[i])

            for i in range(len(self.swarm)):
                if self.fitness[i] > self.fitbest[i]:
                    self.bestind[i] = self.swarm[i]
                    self.fitbest[i] = self.fitness[i]

                if self.fitness[i] > self.top:
                    self.best = self.swarm[i]
                    self.top = self.fitness[i]

            j += 1

        print("Best is: %f, %f" % (self.best, self.top) )

                

    def plot(self, point, path, wait):
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

