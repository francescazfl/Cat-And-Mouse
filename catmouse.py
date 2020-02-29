# Write a driver program catmouse.py that
# sets everything up and calls the main driver loop.

# After the Cat catches the Mouse,
# or if the Cat gives up,
# the simluation should be stopped by calling arena.stop().
# Not exit the program at this time

# 1 meter = 100 pixels and every time step is 10 milliseconds.
# speed = 1 in the program, it means 1 pixel per 10 ms,
# which is also equivalent to 1 m/s.
# The distance between coordinates (100, 100) and (100, 200) is 1 meter or 100 pixels.

import argparse
import math

from tkinter import *
from PIL import Image, ImageTk
import mynewwindow
import updatetime

from libs.Arena import Arena
from libs.Color import *

from Cat import *
from Mouse import *
from Statue import Statue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Project 3: Turtle Behavior')
    parser.add_argument('--no-gui', action='store_true')
    args = parser.parse_args()

    tk = Tk()
    if args.no_gui:
        arena = Arena(tk, verbose=True, gui=False)
        # The Arena runs in real-time by default,
        # which means each 10 ms time step will actually takes 10 milliseconds.
        # Can speed up or slow down the simulation by using the following command
        arena.runtime_period = 0
    else:
        arena = Arena(tk)
    arena.pack()

    # For Arena class, one can use verbose=False argument
    # to print the position of Cat and Mouse during simulation
    # Use gui=True to turn off the GUI and run in command-line only.

    # create more pulldown menus
    # editmenu = Menu(menubar, tearoff=0)
    # editmenu.add_command(label="Cut", command=hello)
    # editmenu.add_command(label="Copy", command=hello)
    # editmenu.add_command(label="Paste", command=hello)
    # menubar.add_cascade(label="Edit", menu=editmenu)

    # helpmenu = Menu(menubar, tearoff=0)
    # helpmenu.add_command(label="About", command=hello)
    # menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu

    from libs.Vector import *
    import math

    radius = 1

    '''
    # case 1
    mouse_angle = 396.000
    mouse_heading = mouse_angle - 90
    cat_angle = 35.000
    cat_heading = cat_angle - 90
    cat_radius = 1.000
    '''

    # case 2
    mouse_angle = -57.000
    mouse_heading = mouse_angle - 90
    cat_angle = 0.000
    cat_heading = cat_angle - 90
    cat_radius = 3.200

    '''
    # case 3
    mouse_angle = 45.000
    mouse_heading = mouse_angle - 90
    cat_angle = 0.1000
    cat_heading = cat_angle - 90
    cat_radius = 8.100
    '''

    '''
    # case 4
    mouse_angle = 240.000
    mouse_heading = mouse_angle - 90
    cat_angle = 150.000
    cat_heading = cat_angle - 90
    cat_radius = 8.100
    '''

    '''
    # case 5
    mouse_angle = -57.000
    mouse_heading = mouse_angle - 90
    cat_angle = 0.000
    cat_heading = cat_angle - 90
    cat_radius = 4.000
    # stoptime = 30*10**3
    '''

    statue = Statue(Vector(200, 200), 0, radius*100)
    mouse = Mouse(Vector(200, 200), mouse_heading, radius*100, 1, mouse_angle, arena)
    cat = Cat(Vector(200, 200),cat_heading, radius*100, cat_radius*100, 1.25, 1, cat_angle, mouse_angle, mouse, arena, updatetime.callback())

    arena.add(statue)
    arena.add(mouse)
    arena.add(cat)
    arena.getinitial()
    arena.make_time_widgets()

    def cursor_motion(event):
        if arena.is_running() != 1:
            # print('stopped')
            if round(cat.position.x + arena._canvas_offset.x - 15) <= round(event.x) <= round(cat.position.x + arena._canvas_offset.x + 15) and round(cat.position.y + arena._canvas_offset.y - 15) <= round(event.y) <= round(cat.position.y + arena._canvas_offset.y + 15):
                print('Cat: Hey! You want to move me around?')
                cat.style['fill'] = black
                cat.arena.update(cat)
            else:
                cat.style['fill'] = orange
                cat.arena.update(cat)

    def move_cat(event):
        if arena.is_running() != 1:
            if round(cat.position.x + arena._canvas_offset.x - 15) <= round(event.x) <= round(cat.position.x + arena._canvas_offset.x + 15) and round(cat.position.y + arena._canvas_offset.y - 15) <= round(event.y) <= round(cat.position.y + arena._canvas_offset.y + 15):
                cat.position.x = event.x - arena._canvas_offset.x
                cat.position.y = event.y - arena._canvas_offset.y
                # cat.heading = math.atan((cat.position.x-200)/(abs(200-cat.position.y)))/math.pi*180
                if ((cat.position.x - 200)**2 + (cat.position.y - 200)**2)**0.5 < 200:
                    print('Just note that the Cat cannot get into the statue!')
                if cat.position.x - 200 >= 0 and 200 - cat.position.y > 0:
                    cat.heading = (math.atan((cat.position.x-200)/(200-cat.position.y))/math.pi*180 + 180) % 360
                elif cat.position.x - 200 >= 0 and 200 - cat.position.y < 0:
                    cat.heading = (math.atan((cat.position.x-200)/(200-cat.position.y))/math.pi*180) % 360
                elif cat.position.x - 200 <= 0 and 200 - cat.position.y < 0:
                    cat.heading = (math.atan((cat.position.x-200)/(200-cat.position.y))/math.pi*180) % 360
                elif cat.position.x - 200 <= 0 and 200 - cat.position.y > 0:
                    cat.heading = (math.atan((cat.position.x-200)/(200-cat.position.y))/math.pi*180 + 180) % 360
                # print(cat.heading)
                cat.arena.update(cat)
                cat.arena.radius_label.config(text = 'CatRadius [m]: ' + str(round(cat.cat_radius/100,3)))
                cat.arena.angle_label.config(text = 'CatAngle [°]: ' + str(round((cat.heading + 90)%360,3)))

    def get_back_normal(event):
        if arena.is_running() != 1:
            if round(cat.position.x + arena._canvas_offset.x - 15) <= round(event.x) <= round(cat.position.x + arena._canvas_offset.x + 15) and round(cat.position.y + arena._canvas_offset.y - 15) <= round(event.y) <= round(cat.position.y + arena._canvas_offset.y + 15):
                # print(cat.heading)
                cat.heading = cat.heading + 90
                # print(cat.heading)
                cat.arena.update(cat)
                cat.arena.radius_label.config(text = 'CatRadius [m]: ' + str(round(cat.cat_radius/100,3)))
                cat.arena.angle_label.config(text = 'CatAngle [°]: ' + str(round((cat.heading + 90)%360,3)))

    tk.bind('<Motion>', cursor_motion)
    tk.bind('<B1-Motion>', move_cat)

    tk.bind('<ButtonRelease>', get_back_normal)

    menubar = Menu(tk)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    # filemenu.add_command(label="Open", command=hello)
    # filemenu.add_command(label="Save", command=hello)
    # filemenu.add_command(label="About", command=draft.newwindow)
    filemenu.add_command(label="About", command=mynewwindow.newwindow)

    filemenu.add_command(label="Quit", command=tk.quit)
    # filemenu.add_separator()
    # filemenu.add_command(label="Exit", command=tk.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    tk.config(menu=menubar)

    arena.make_radius_label(cat)
    arena.make_angle_label(cat)
    arena.make_new_angle_label(mouse)

    tk.mainloop()
