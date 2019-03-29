import numpy as np
import random


class Ant:
    def __init__(self, start_x, start_y, x_max, y_max):
        """
        Creates an ant.

        :param start_x: the starting x coord
        :param start_y: the starting y coord
        """
        self.x = start_x
        self.y = start_y
        self.x_max = x_max
        self.y_max = y_max
        self.state = None
        self.load = None

    def change_state(self, color):
        """
        """
        self.state = color

    def get_state(self):
        return self.state

    def get_pos(self):
        return self.x, self.y

    def pick_up(self, obj, density, tick):
        thresh = (tick/1000 * .05) + .1
        prob = (thresh / (thresh + density)) ** 2
        chance = np.random.rand()

        if chance < prob:
            self.state = obj
            return True
        return False

    def drop_off(self, density, tick):
        thresh = (tick/1000 * .05) + .1
        chance = np.random.rand()

        prob = (density / (thresh + density)) ** 2

        if chance < prob:
            temp = self.state
            self.state = None
            return temp
        return 0

    def walk(self):
        xMove = random.choice([-4, 4])
        yMove = random.choice([-4, 4])

        xPos = self.x + xMove
        yPos = self.y + yMove

        self.x = xPos % self.x_max
        self.y = yPos % self.y_max
        return
