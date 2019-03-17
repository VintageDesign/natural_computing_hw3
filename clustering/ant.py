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
        self.load = None
   

    def change_state(self):
        """
        Changes the ants FSM state
        """
        self.state = 'loaded' if self.state == 'empty' else 'empty'
    
    
    def get_state(self):
        return self.state

    
    def get_pos(self):
        return self.x, self.y


    def pick_up(self, obj, density, avg):
        rule = avg

        if self.state == 'loaded':
            return False

        if density < rule: 
            self.load = obj
            self.change_state()
            return True

    
    def drop_off(self, red_density, blue_density, red_avg, blue_avg):

        if self.state == 'empty':
            return 0
        
        rule = red_avg if self.load == 1 else blue_avg
        density = red_density if self.load == 1 else blue_density

        if density > round(rule):
            temp = self.load
            self.load = None
            self.change_state()
            return temp
        
        return 0


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
        
