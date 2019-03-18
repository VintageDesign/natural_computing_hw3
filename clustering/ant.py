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
        Changes the ants FSM state
        """
        self.state = color

    def get_state(self):
        return self.state

    def get_pos(self):
        return self.x, self.y

    def pick_up(self, obj, density):
        thresh = 0.1
        prob = (thresh / (thresh + density)) ** 2
        chance = np.random.rand()

        if chance < prob:
            self.change_state(obj)
            print("Pick up: %f, %f" % (density, prob))
            return True
        print("No pick up: %f, %f" % (density, prob))
        return False

    def drop_off(self, density):
        thresh = 0.05
        chance = np.random.rand()

        prob = (density / (thresh + density)) ** 2

        if chance < prob:
            temp = self.state
            self.change_state(None)
            print("Drop: %f, %f" % (density, prob))
            return temp
        return 0

    def walk(self):
        while True:
            xMove = random.choice([-1, 1])
            yMove = random.choice([-1, 1])

            xPos = self.x + xMove
            yPos = self.y + yMove

            if xPos >= 0 and yPos >= 0 and xPos < self.x_max and yPos < self.y_max:
                self.x = xPos
                self.y = yPos
                return
