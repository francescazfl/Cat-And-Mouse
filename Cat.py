# subclasses of Turtle
# The Cat should move towards the center of Statue
# if it can see the Mouse (not blocked by Statue),
# with a linear speed of 1 m/s,
# or runs around in the circle, with a linear speed of 1.25 m/s.
# 1 meter = 100 pixels and every time step is 10 milliseconds.
# speed = 1 in your program, it means 1 pixel per 10 ms,
# which is also equivalent to 1 m/s.
# The distance between coordinates (100, 100) and (100, 200) is 1 meter or 100 pixels.

# In your Cat.__init__(), you may want to pass in the Mouse instance as an argument
# so that the Cat can know about the position of the Mouse.
# pass in the Arena and Statue instance to both Cat and Mouse.

import argparse

from tkinter import *

from libs.Arena import Arena                      # Import our Arena

from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *
from Mouse import *
import math
#from tkinter import *

class Cat(Turtle):
    def __init__(self, position, heading, radius, cat_radius, cat_cycle_speed, cat_linear_speed, cat_angle, mouse_angle, mouse, arena, stoptime, fill=orange, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        # heading is the angle of the turtle's direction
        self.radius = radius
        self.cat_radius = cat_radius
        self.cat_cycle_speed = cat_cycle_speed
        self.cat_linear_speed = cat_linear_speed
        self.cat_angle = cat_angle
        self.mouse_angle = mouse_angle
        # print(mouse_angle)
        self.heading = self.cat_angle - 90
        #self.position = self.position + unit(self.heading + 90)*self.radius
        self.position = self.position + unit(self.heading + 90)*self.cat_radius
        self.mouse = mouse
        self.arena = arena
        self.stoptime = stoptime

    def getnextstate(self):
        self.arena.radius_label.config(text = 'CatRadius [m]: ' + str(round(self.cat_radius/100,3)))
        self.arena.angle_label.config(text = 'CatAngle [°]: ' + str(round((self.heading + 90)%360,3)))
        if int(self.arena.get_timestamp()) > int(self.stoptime):
            print('Ugh, I give up.')
            self.arena.stop()
            return self.position, self.heading
        else:
            self.cat_radius = ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5
            self.cat_angle = self.heading + 90
            if ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5 <= self.radius:
                C = self.heading - 360/(2*math.pi*self.radius/self.cat_cycle_speed)
                A = self.heading
                B = self.mouse.heading
                if math.cos((B-A)*math.pi/180) > math.cos((C-A)*math.pi/180) and math.cos((C-B)*math.pi/180) > math.cos((C-A)*math.pi/180):
                    # when the cat radius is 1.0 and the mouse angle lies between the old cat angle and the new cat angle.
                    # An angle B is between angles A and C in the following circumstances:
                    # cos (B - A) > cos (C - A), and cos (C - B) > cos (C - A) (angles in radian)
                    # The difference C - A is assumed to be less than 90°, or π/2 radians.
                    print('I got you at ' + str(self.arena.get_timestamp()/10**3) + ' seconds!')
                    # get_timestamp returns current simulation time (in milliseconds)
                    self.arena.stop()
                    return self.position, self.heading
                else:
                    print('I am coming!')
                    self.heading = self.heading - 360/(2*math.pi*self.radius/self.cat_cycle_speed)
                    self.position = self.position + unit(self.heading)*self.cat_cycle_speed
                    return self.position, self.heading
            elif ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5 > self.radius and (self.cat_radius) * math.cos((self.cat_angle - (self.mouse.heading + 90))*math.pi/180) >= 1.0:
                print('I am coming!')
                self.heading = self.heading
                self.position = self.position + unit(self.heading - 90)*self.cat_linear_speed

                return self.position, self.heading
            elif ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5 > self.radius and (self.cat_radius) * math.cos((self.cat_angle - (self.mouse.heading + 90))*math.pi/180) < 1.0:
                print('Where is the mouse? I am circling.')
                self.heading = self.heading - 360/(2*math.pi*self.cat_radius/self.cat_cycle_speed)
                self.position = self.position + unit(self.heading)*self.cat_cycle_speed
                return self.position, self.heading
