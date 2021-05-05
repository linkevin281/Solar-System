# name: Kevin Lin
# date: 02/20/21
# purpose: create system class

from math import *
from bodyextra import Body

G = 6.67384e-11

class System:
    def __init__(self, body_list):
        self.list = body_list
        self.stop = False

    def update(self, timestep, stop): # from the list of bodies go through each one and update its position and velocity
        if stop:
            self.stop = True
        if self.stop:
            return
        if not stop:
            self.stop = False

        for i in range(0, 101): # will update the position and velocity 100 times with sub-time steps before drawing once for higher precision
            for i in range(0, len(self.list)):
                self.list[i].update_position(timestep/101)

            for i in range(0, len(self.list)):  # self.ax and ay calculated through compute acceleration
                self.list[i].update_velocity(self.compute_acceleration(self.list[i])[0], self.compute_acceleration(self.list[i])[1], timestep/101)

    def compute_acceleration(self, body): #calculates acceleration at the current time for each planets
        temp = self.list.copy()

        temp.remove(body)

        x = 0
        y = 0

        for i in range(0, len(temp)):

            dx = temp[i].x - body.x
            dy = temp[i].y - body.y

            r = sqrt((dx**2) + (dy**2))
            if r == 0:
                continue
            a = G * temp[i].mass / (r**2)

            x = (x + (a * dx)/r)
            y = (y + (a * dy)/r)

        return x, y

    def draw(self, cx, cy, pixels_per_meter, stop): # draw all the bodies in the list
        if stop:
            self.stop = True
        if self.stop:
            return

        for i in range(0, len(self.list)):
            self.list[i].draw(cx, cy, pixels_per_meter)