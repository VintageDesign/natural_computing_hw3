import numpy as np
#from scipy import optimize
import matplotlib.pyplot as plt
import random
import math


class Particle_Swarm:

    def __init__(self, pop_size, it_max, v_min, v_max):
        """
        Initializes particles
        """
        plt.rcParams['font.family'] = "Bitstream Vera Sans"
        self.it_max = it_max
        if v_min > v_max:
            raise Exception('V_min cannot be bigger than V_max')

        self.v_min = v_min
        self.v_max = v_max
        self.swarm = []
        self.velocity = []
        self.pr = []
        self.fitness = []
        self.fitbest = []

        for individual in range(pop_size):
            x = np.random.rand()
            fit = self.evaluate(x)

            self.swarm.append(x)
            self.velocity.append(0)
            self.fitness.append(fit)
            
            self.pr.append(x)
            self.fitbest.append(fit)

        self.g = self.swarm[self.fitness.index(min(self.fitness))]
        self.top = min(self.fitness)


    def evaluate(self, x):
        exponent = -2 * (((x-0.1)/0.9) ** 2)
        num = (2 ** exponent) * (math.sin(5 * math.pi * x) ** 6)
        return num


    def pso(self):
        j = 0
        avg_x = []
        best_x = []
        it = []
        
        while j < self.it_max and 1 - self.top > 0.001:
            for i in range(len(self.swarm)):
                phi1 = np.random.randn() * np.random.uniform(self.v_min, self.v_max)
                phi2 = 4 * np.random.randn() * np.random.uniform(self.v_min, self.v_max)

                self.velocity[i] += phi1 * (self.pr[i] - self.swarm[i]) + phi2 * (self.g - self.swarm[i])
                print(self.velocity[i])
                
                while (self.swarm[i] + self.velocity[i] < 0) or (self.swarm[i] + self.velocity[i] > 1):
                    print("bad")
                    self.velocity[i] *= np.random.uniform(self.v_min, self.v_max)

                self.swarm[i] += self.velocity[i]
                self.fitness[i] = self.evaluate(self.swarm[i])

            for i in range(len(self.swarm)):
                if self.fitness[i] > self.fitbest[i]:
                    self.pr[i] = self.swarm[i]
                    self.fitbest[i] = self.fitness[i]

                if self.fitness[i] > self.top:
                    self.g = self.swarm[i]
                    self.top = self.fitness[i]

            avg_x.append(np.average(self.swarm))
            best_x.append(self.g)
            it.append(j)
            j += 1
        
        self.plot(avg_x, best_x, it)
        print("Best found at x=%f, y=%f (%f iterations)" % (self.g, self.top, j) )
        return self.g, self.top, j


    def plot(self, avg_x, best_x, it):
        plt.plot(it, avg_x, color='green', linewidth=0.5)
        plt.plot(it, best_x, color='blue', linewidth=0.5)
        plt.axis('off')
        plt.ion()
        plt.show()
        plt.pause(.0001)

    def save_plot(self):
        plt.plot(0, 0, color='green', linewidth=0.3, label='Average position of swarm')
        plt.plot(0, 0, color='blue', linewidth=0.3, label='Best position')
        plt.axis('on')
        plt.yticks(np.arange(0, 1, 0.1))
        plt.xticks(np.arange(0, 30, 1))
        ax = plt.gca()
        ax.set_xlim(0, 30)
        ax.set_title("Particle Swarm Algorithm", fontsize=20)
        leg = ax.legend()
        ax.legend(loc='upper right', frameon=False, fontsize=15, shadow=True, ncol=2)
        plt.ion()
        plt.show()
        plt.pause(15)

        fig = plt.gcf()
        fig.savefig('plot.png')

