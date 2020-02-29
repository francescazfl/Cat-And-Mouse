from libs.Vector import *
from libs.Color import *


class Turtle:
    """This is the base class for all turtles."""

    def __init__(self, position, heading,
                 outline=black, fill=white, width=1):
        self.position, self.heading = position, heading
        self.style = dict(outline=outline, fill=fill, width=width)
        # print(self.position, self.heading)

    '''
    def getinitial(self):
        initial_position =  self.position
        initial_heading =  self.heading
        # print(initial_position, initial_heading)
        return initial_position, initial_heading
    '''

    def getshape(self):
        """Return a list of vectors giving the polygon for this turtle."""
        forward = unit(self.heading)
        right = unit(self.heading + 90)
        return [self.position + forward * 15,
                self.position - forward * 8 - right * 8,
                self.position - forward * 5,
                self.position - forward * 8 + right * 8]

    def getnextstate(self):
        """Determine the turtle's next step and return its new state."""
        return self.position, self.heading
        # the state returned is a tuple containing the current position and heading
        # i.e. the next state is the same as the current statue
        # and the turtle is not going to move

    def setstate(self, state):
        """Update the state of the turtle."""
        self.position, self.heading = state
