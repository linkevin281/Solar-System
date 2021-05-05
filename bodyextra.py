# name: Kevin Lin
# date: 02/20/21
# purpose: create body blass

from cs1lib import *
p = 0
v = 0
# simulates a planet
class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

        self.x_b = x
        self.y_b = y
        self.vx_b = vx
        self.vy_b = vy

    def update_position(self, timestep):   #updates the position of the draw
        self.x = self.x + self.vx*timestep
        self.y = self.y + self.vy*timestep

    def update_velocity(self, ax, ay, timestep): #updates the change in the position of the draw
        self.vx = self.vx + ax*timestep
        self.vy = self.vy + ay*timestep


    def draw(self, cx, cy, pixels_per_meter):   #draws the planet
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx+ self.x*pixels_per_meter, cy + self.y*pixels_per_meter, self.radius)

