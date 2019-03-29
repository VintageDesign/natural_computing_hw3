import numpy as np
import math
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
        self.ants = []
        self.objects = []
        self.grid = np.zeros((self.grid_size[0], self.grid_size[0]))
        self.red_density = np.zeros((self.grid_size[0], self.grid_size[0]))
        self.blue_density = np.zeros((self.grid_size[0], self.grid_size[0]))
        self.place_objects()
        self.place_ants()

    def place_objects(self):
        for color in range(self.colors):
            for obj in range(self.object_count):
                x = np.random.randint(0, self.grid_size[0] - 1)
                y = np.random.randint(0, self.grid_size[1] - 1)

                while self.grid[x][y] != 0:
                    x = np.random.randint(0, self.grid_size[0] - 1)
                    y = np.random.randint(0, self.grid_size[1] - 1)
                self.grid[x][y] = color + 1
                self.objects.append([color + 1, x, y])

    def place_ants(self):
        """
        Randomly places ants on the board
        """
        for ant_ind in range(self.ant_count):
            x = np.random.randint(0, self.grid_size[0])
            y = np.random.randint(0, self.grid_size[1])
            self.ants.append(Ant(x, y, self.grid_size[0], self.grid_size[1]))

    def print_board(self, tick):
        plt.savefig("outcomes/cluster" + str(tick) + ".png")
        plt.clf()
        plt.xlim(0, self.grid_size[0])
        plt.ylim(0, self.grid_size[1])

        for obj in self.objects:
            color = ''
            if obj[0] == 0:
                continue
            elif obj[0] == 1:
                color = 'ro'
            elif obj[0] == 2:
                color = 'bo'

            plt.plot(obj[1], obj[2], color)
        '''
        for ant in self.ants:
            x, y = ant.get_pos()
            plt.plot(x, y, 'g+')
        '''
        if tick != self.ticks:
            plt.ion()
        plt.show()
        plt.pause(0.0001)

    def euclid(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def eval_density(self, obj):
        search_range = 5
        alpha = 500

        x = obj[1]
        y = obj[2]
        x_low = 0 if x - search_range < 0 else x - search_range
        x_high = self.grid_size[0] - 1 if x + \
            search_range >= self.grid_size[0] else x + search_range
        y_low = 0 if y - search_range < 0 else y - search_range
        y_high = self.grid_size[0] - 1 if y + \
            search_range >= self.grid_size[1] else y + search_range

        sub = self.grid[x_low:x_high + 1, y_low:y_high + 1]

        color = 1 if obj[0] == 1 else 2
        siblings = np.where(sub == color)

        sum = 0
        for r in range(len(siblings[0])):
            sum += 1 - (self.euclid(x, y, siblings[0][r], siblings[1][r]) / alpha)
        f = (1 / (search_range ** 2)) * sum

        return f if f > 0 else 0

    def run_algorithm(self):
        for tick in range(self.ticks):
            for ant in self.ants:
                state = ant.get_state()
                x, y = ant.get_pos()

                if state is None and self.grid[x][y] != 0:
                    density = self.eval_density([self.grid[x][y], x, y])
                    if ant.pick_up(self.grid[x][y], density) is True:
                        self.grid[x][y] = 0

                        idx = -1
                        for i, o in enumerate(self.objects):
                            if o[1] == x and o[2] == y:
                                idx = i
                        self.objects.pop(idx)

                elif state is not None and self.grid[x][y] == 0:
                    self.grid[x][y] = ant.drop_off(self.eval_density([state, x, y]))

                    if self.grid[x][y] != 0:
                        self.objects.append([self.grid[x][y], x, y])

                ant.walk()

            if tick % 50 == 0:
                self.print_board(tick)
                print ("Tick: ", tick)
        self.print_board(tick);
