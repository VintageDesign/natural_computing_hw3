import numpy as np
import random
from .particle import Particle

class Swarm:

    def __init__(self, population_size, cities_size):
        """

        """
        self.cities = self.init_cities_list(cities_size)
        self.swarm = self.make_swarm(population_size)

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

    def run_algorithm(self):
        """

        """

