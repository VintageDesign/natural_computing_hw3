import numpy as np
import random
import sys
from .particle import Particle

class Swarm:

    def __init__(self, population_size, cities_size):
        """

        """
        self.cities = self.init_cities_list(cities_size)
        self.swarm = self.make_swarm(population_size)
        self.gBest = self.find_gBest()

    def init_cities_list(self, cities_size):
        """
        Creates a city list for all particles
        """
        return (np.random.rand(cities_size, 2) * 100).astype(int)
        
    def make_swarm(self, population_size):
        """
        Creates all of the particles in the swarm
        """
        swarm = []
        while (len(swarm) < population_size):
            swarm.append(Particle(self.cities))
        return swarm

    def find_gBest(self):
        gBest = sys.maxsize
        for particle in self.swarm:
            if particle.getSolution() < gBest:
                gBest = particle.getSolution()
        return gBest

    def run_algorithm(self):
        """

        """
        j = 0
        while (j < 500):
            for particle in self.swarm:
                phi1 = 0.1 + np.random.randn()
                phi2 = 0.1 + np.random.randn()

                curr_solution = particle.getSolution()

                curr_velocity = particle.getVelocity() + \
                    (phi1 * (particle.getPBest() - curr_solution) + phi2 * (self.gBest - curr_solution))
                
                particle.setVelocity(curr_velocity)

                if (curr_solution + curr_velocity > 0) and (curr_solution + curr_velocity < 2):
                    curr_solution += curr_velocity