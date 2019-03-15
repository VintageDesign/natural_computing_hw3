import numpy as np
from .ant import Ant

class Cluster:
    def __init__(self, pop_size, object_count, color_count, grid_size_x, grid_size_y):
        """ Initialize the clustering algorithm
        :param pop_size: the number of ants
        :param object_count: the number of objects per color
        :param color_count: the number of colors
        :param grid_size_x:
        :param grid_size_x:
        """
        self.ant_count = pop_size
        self.object_count = object_count
        self.colors = color_count
        self.grid_size = (grid_size_x, grid_size_y)

        init_board()

    def init_board(self):
        """
        Generates the board of objects
        0: will represent an empty board
        1: will represent an ant
        2 - color_count + 1: will represent an object
        """
        self.objects = []
        self.ants = []

        place_objects()

        place_ants()

    def place_objects(self):
        """
        Distributes objects across the board
        """
        for color in range(self.color_count):

            for obj in range(self.object_count):
                x = np.random.randint(0, this.grid_size[0])
                y = np.random.randint(0, this.grid_size[1])
                object_instance = (obj, x, y)
                self.objects.append(object_instance)

    def place_ants(self):
        """
        Randomly places ants on the board
        """
        for ant_ind in range(ant_count):
            self.ants.append(Ant())

