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
        self.objects = np.zeros((self.grid_size[0], self.grid_size[0]))
        self.ants = []
        self.grid = []
        self.red_density = np.zeros((self.grid_size[0], self.grid_size[0]))
        self.blue_density = np.zeros((self.grid_size[0], self.grid_size[0]))

        self.place_objects()
        self.eval_density()

        self.place_ants()

    
    def place_objects(self):
        """
        Distributes objects across the board
        """
        for color in range(self.colors):
            for obj in range(self.object_count):
                x = np.random.randint(0, self.grid_size[0] - 1)
                y = np.random.randint(0, self.grid_size[1] - 1)
                
                self.objects[x][y] = color + 1
                self.grid.append([color + 1, x, y])

    
    def place_ants(self):
        """
        Randomly places ants on the board
        """
        for ant_ind in range(self.ant_count):
            x = np.random.randint(0, self.grid_size[0])
            y = np.random.randint(0, self.grid_size[1])
            self.ants.append(Ant(x, y))


    def print_board(self, tick):
        
        if tick % 1000 == 0:
            plt.savefig("cluster" + str(tick) + ".png")
        plt.clf()
        plt.xlim(0, self.grid_size[0])
        plt.ylim(0, self.grid_size[1])

        for obj in self.grid:
            color = ''
            if obj[0] == 0:
                continue
            elif obj[0] == 1:
                color = 'ro'
            elif obj[0] == 2:
                color = 'bo'

            plt.plot(obj[1], obj[2], color)

        for ant in self.ants:
            x, y = ant.get_pos()
            plt.plot(x, y, 'g+')
        
        plt.ion()
        plt.show()
        plt.pause(0.0001)


    def eval_density(self):
        search_range = 10
        
        for r in range(self.grid_size[0]):
            for c in range(self.grid_size[1]):
                x_low = 0 if r - search_range < 0 else r - search_range
                x_high = self.grid_size[0] - 1 if r + search_range >= self.grid_size[0] else r + search_range
                y_low = 0 if c - search_range < 0 else c - search_range
                y_high = self.grid_size[0] - 1 if c + search_range >= self.grid_size[1] else c + search_range

                sub = self.objects[x_low:x_high+1, y_low:y_high+1]
                unique, count = np.unique(sub, return_counts = True)
                sub_dict = dict(zip(unique, count))
                if 1 in sub_dict:
                    self.red_density[r][c] = sub_dict[1]
                if 2 in sub_dict:
                    self.blue_density[r][c] = sub_dict[2]


    def run_algorithm(self):

        for tick in range(self.ticks):
            self.eval_density()
            print(np.average(self.red_density), np.average(self.blue_density))
            print(len(self.grid))
            # TODO make this loop run in parallel
            # TODO It might cause problems running in parallel actually, data races in objects
            for ant in self.ants:
                state = ant.get_state()
                ant.walk()

                x, y = ant.get_pos()

                if self.objects[x][y] == 0:
                    self.objects[x][y] = ant.drop_off(self.red_density[x][y], self.blue_density[x][y], np.average(self.red_density), np.average(self.blue_density))
                    
                    if self.objects[x][y] != 0:
                        self.grid.append([self.objects[x][y], x, y])
                        print("Drop off")
                
                else:
                    density = self.red_density[x][y] if self.objects[x][y] == 1 else self.blue_density[x][y]
                    if ant.pick_up(self.objects[x][y], density, np.average(self.blue_density)) == True:
                        self.objects[x][y] = 0

                        idx = -1
                        for i, o in enumerate(self.grid):
                            if o[1] == x and o[2] == y:
                                idx = i
                        self.grid.pop(idx)
                        print("Pick up")
            if tick % 200 == 0:
                self.print_board(tick)

