import random

class Ant:
    def __init__(self, start_x, start_y):
        """
        Creates an ant.

        :param start_x: the starting x coord
        :param start_y: the starting y coord
        """

        self.x = start_x
        self.y = start_y

        self.state = 'empty'

    
    def change_state(self):
        """
        Changes the ants FSM state
        """

        if self.state == 'empty':
            self.state = 'loaded'
        elif self.state == 'loaded':
            self.state = 'empty'

    
    def get_state(self):
        return self.state

    
    def get_pos(self):
        return self.x, self.y


    def pick_up(self, obj):
        self.load = obj
        self.change_state()

    
    def drop_off(self):
        temp = self.load
        self.load = None
        self.change_state()
        return temp


    def walk(self):
        while True:
            xMove = random.choice([-1, 1])
            yMove = random.choice([-1, 1])

            xPos = self.x + xMove
            yPos = self.y + yMove

            if xPos >= 0 and yPos >= 0 and xPos < 200 and yPos < 200:
                self.x = xPos
                self.y = yPos
                return
        
