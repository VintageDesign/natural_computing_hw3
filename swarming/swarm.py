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

                curr_location = particle.getLocation()
                # TO-DO: figure out a way to map the location of each particle in relation to each other

                curr_velocity = particle.getVelocity() + \
                    (phi1 * (particle.getPBest() - curr_location) + \
                        phi2 * (self.gBest - curr_location))
                
                particle.setVelocity(curr_velocity)

                if (curr_location + curr_velocity > 0) and (curr_location + curr_velocity < 2):
                    curr_location += curr_velocity
