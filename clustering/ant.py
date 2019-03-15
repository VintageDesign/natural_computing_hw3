

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


    def pick_up(self, obj):
        self.load = obj
        change_state()

    def drop_off(self):
        temp = self.load
        self.load = None
        change_state()
        return temp


