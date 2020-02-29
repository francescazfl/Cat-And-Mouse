# subclasses of Turtle
# The Mouse should just runs around in the circle,
# on the edge of the Statue,
# with a linear speed of 1 m/s
# 1 meter = 100 pixels and every time step is 10 milliseconds.
# speed = 1 in your program, it means 1 pixel per 10 ms,
#  which is also equivalent to 1 m/s.
# The distance between coordinates (100, 100) and (100, 200) is 1 meter or 100 pixels.

# pass in the Arena and Statue instance to both Cat and Mouse.

# The Mouse should just run forever while the Cat should control the simulation.
# While the Cat catches the mouse, it should call the following command to stop the simulation.
# (The Arena instance should be passed into Cat.__init__() as an argument)
# arena.stop()
# The cat will give up after 30 seconds.
# use the time computed by the Arena with the following command:
# arena.get_timestamp() # Time in milliseconds

from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *
from libs.Arena import Arena
import math

class Mouse(Turtle):  # Inherit behavior from Turtle
    def __init__(self, position, heading, radius, mouse_speed, mouse_angle, arena, fill=grey, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        # heading is the angle of the turtle's direction
        self.radius = radius
        self.mouse_speed = mouse_speed
        self.mouse_angle = mouse_angle
        self.heading = self.mouse_angle - 90
        #self.position = self.position + unit(self.heading + 90)*self.radius
        self.position = self.position + unit(self.heading + 90)*self.radius
        self.arena = arena
        # assume the heading is the direction that the tutle is facing

    def getnextstate(self):
        self.heading = self.heading - 360/(2*math.pi*self.radius)
        self.position = self.position + unit(self.heading)*self.mouse_speed
        self.arena.new_angle_label.config(text = 'MouseAngle [°]: ' + str(round((self.heading + 90)%360,3)))
        return self.position, self.heading
