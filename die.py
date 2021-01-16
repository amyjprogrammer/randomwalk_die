from random import randint

class Die:
    """a single die roll"""

    def __init__(self, num_sides=6):
        """Rolling with a six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value"""
        return randint(1, self.num_sides)
