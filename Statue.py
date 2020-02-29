# The Statue should be a fixed object that looks like a circle,
# placed at (200, 200), with radius of 1 meter, or 100 pixels.
# The statue needs to be drawn the statue on the canvas.
# subclasses of Turtle

from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *

class Statue(Turtle):
    def __init__(self, position, heading, radius):
        Turtle.__init__(self, position, heading)
        self.radius = radius

    def getshape(self):
        # Return a list of vectors giving the polygon for this turtle.
        statue_pts = []
        for i in range(360):
            forward = unit(i)
            statue_pts = statue_pts + [self.position + forward * self.radius]
        return statue_pts
