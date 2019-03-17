import numpy as np
import matplotlib.pyplot as plt
from .ant import Ant


class Cluster:
    def __init__(self, pop_size, object_count, color_count, grid_size_x, grid_size_y, ticks):
        """ Initialize the clustering algorithm
        :param pop_size: the number of ants
        :param object_count: the number of objects per color
        :param color_count: the number of colors
        :param grid_size_x: the number of rows on the board
        :param grid_size_y: the number of cols on the board
        :param ticks:       the number of iterations the algorithm runs
        """
        self.ant_count = pop_size
        self.object_count = object_count
        self.colors = color_count
        self.grid_size = (grid_size_x, grid_size_y)
        self.ticks = ticks
        self.init_board()

    
    def init_board(self):
        """
        Generates the board of objects
        0: will represent an empty board
        1: will represent an ant
        2 - color_count + 1: will represent an object
        """
        self.objects = []
        self.ants = []

        self.place_objects()

        self.place_ants()

    
    def place_objects(self):
        """
        Distributes objects across the board
        """
        for color in range(self.colors):

            for obj in range(self.object_count):
                x = np.random.randint(0, self.grid_size[0])
                y = np.random.randint(0, self.grid_size[1])
                object_instance = (color, x, y)
                self.objects.append(object_instance)

    
    def place_ants(self):
        """
        Randomly places ants on the board
        """
        for ant_ind in range(self.ant_count):
            x = np.random.randint(0, self.grid_size[0])
            y = np.random.randint(0, self.grid_size[1])
            self.ants.append(Ant(x, y))


    def print_board(self):

        plt.clf()
        for obj in self.objects:
            color = ''
            if obj[0] == 0 :
                color = 'ro'
            elif obj[0] == 1 :
                color = 'bo'
            elif obj[0] == 2 :
                raise notImplementedError

            plt.plot(obj[1], obj[2], color)
        
        for ant in self.ants:
            x, y = ant.get_pos()
            plt.plot(x, y, 'g+')
        
        plt.xlim(0, self.grid_size[0])
        plt.ylim(0, self.grid_size[1])
        plt.ion()
        plt.show()
        plt.pause(0.5)


    def run_algorithm(self):

        for tick in range(self.ticks):
            # TODO make this loop run in parallel
            # TODO It might cause problems running in parallel actually, data races in objects
            for ant in self.ants:
                state = ant.get_state()
                ant.walk()
                #if state = 'empty':
            
            self.print_board()


