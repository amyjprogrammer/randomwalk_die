from random import choice

class RandomWalk:
    """generating random walks"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # walk starts at (0,0)
        self.x_values= [0]
        self.y_values= [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        while len(self.x_values) < self.num_points:

            #Decide which direction to go
            x_step = self.get_step()
            y_step = self.get_step()

            #Ignore moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #New position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        return step
