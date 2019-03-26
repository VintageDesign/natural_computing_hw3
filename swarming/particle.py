import numpy as np
import random

class Particle:

    def __init__(self, cities):
        """

        """
        cities_list = cities.copy()
        self.cities = self.shuffle_cities(cities_list)
        self.solution = self.fit(cities)
        self.pbest = self.solution
        self.velocity = 0

    def shuffle_cities(self, cities_list):
        """
        Creates a new order of city visitation
        """        
        cities = []
        while (len(cities_list) > 0):
            idx = random.randint(0, len(cities_list) - 1)
            city = cities_list[idx].copy()
            cities_list = np.delete(cities_list, idx, 0)
            cities.append(city)
        return cities


    def fit(self, indv):
        """
        Finds the distance of the tour
        """
        distance = 0
        
        for index in range(len(indv)):
            a = indv[index]
            if index == len(indv) - 1:
                b = indv[0]
            else:
                b = indv[index + 1]

            distance += np.linalg.norm(a - b)
            index += 1

        return distance

    def getSolution(self):
        """

        """
        return self.solution

    def getPBest(self):
        """

        """
        return self.pbest

    def getVelocity(self):
        """

        """
        return self.velocity

    def setVelocity(self, velocity):
        """

        """
        self.velocity = velocity