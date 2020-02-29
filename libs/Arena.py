from tkinter import *

from libs.Vector import *

class Arena(Frame):
    """This class provides the user interface for an arena of turtles."""

    ####################################################
    # Initialization
    ####################################################
    def __init__(self, parent, width=1200, height=600, verbose=False, gui=True, **options):
        Frame.__init__(self, parent, **options)

        self._turtles = []
        self._items = {}
        self._running = 0
        self._timestamp = 0
        self._period = 10  # milliseconds
        self._verbose = verbose
        self._gui = gui
        self.initial_position = {}
        self.initial_heading = {}
        self.widget = {}
        self.radius_label = {}
        self.angle_label = {}
        self.new_angle_label = {}
        # new version
        self._canvas_offset = Vector(400, 100)


        self.runtime_period = 10  # actual time for each period

        if not self._gui:
            self.run()
        else:
            self.canvas = Canvas(self, width=width, height=height)
            self.canvas.pack()
            parent.title("UC Berkeley CS9H Turtle Arena")
            Button(self, text='reset', command=self.reset).pack(side=LEFT)
            Button(self, text='step', command=self.step).pack(side=LEFT)
            Button(self, text='run', command=self.run).pack(side=LEFT)
            Button(self, text='stop', command=self.stop).pack(side=LEFT)
            Button(self, text='quit', command=parent.quit).pack(side=LEFT)
            # Button(self, text='Menu', command=self.mymenu).pack(side=TOP)
            self.canvas.bind('<ButtonPress>', self.press)
            self.canvas.bind('<Motion>', self.motion)
            self.canvas.bind('<ButtonRelease>', self.release)
            self.width, self.height = width, height
            self.dragging, self.drag_start, self.start = (None, None, None)

    ####################################################
    # Info Gathering Methods
    ####################################################

    def get_timestamp(self):
        """Return current simulation time (in milliseconds)"""
        return self._timestamp

    def is_running(self):
        """Return if the simulation is running"""
        return self._running

    def make_time_widgets(self):
        self.widget = Label(self, text='Time [seconds]: ' + str(round(self._timestamp/1000,2)))
        # timestamp in milliseconds
        self.widget.pack(side=RIGHT)
        return self.widget

    ####################################################
    # GUI Related Methods
    ####################################################
    def press(self, event):
        """Handles button press event"""
        drag_start = Vector(event.x, event.y)
        for turtle in self._turtles:
            if (drag_start - turtle.position).length() < 10:
                self.dragging = turtle
                self.drag_start = drag_start
                self.start = turtle.position
                # self.startdirect = turtle.heading
                return

    def motion(self, event):
        """Handles drag event"""
        drag = Vector(event.x, event.y)
        if self.dragging:
            self.dragging.position = self.start + drag - self.drag_start
            self.update(self.dragging)

    def release(self, event):
        """Handles button release event"""
        self.dragging = None

    def update(self, turtle):
        """Update the drawing of a turtle according to the turtle object."""
        item = self._items[turtle]
        # old version
        # vertices = [(v.x, v.y) for v in turtle.getshape()]
        # new version
        vertices = [(v.x + self._canvas_offset.x, v.y + self._canvas_offset.y) for v in turtle.getshape()]
        self.canvas.coords(item, sum(vertices, ()))
        self.canvas.itemconfigure(item, **turtle.style)

    def make_radius_label(self,turtle):
        turtle.radius_for_label = (turtle.position.x**2 + turtle.position.y**2)**0.5
        self.radius_label = Label(self, text='CatRadius: N/A')
        self.radius_label.pack(side=RIGHT)
        return self.radius_label

    def make_angle_label(self,turtle):
        turtle.angle_for_label = turtle.heading + 90
        self.angle_label = Label(self, text='CatAngle: N/A')
        self.angle_label.pack(side=RIGHT)
        return self.angle_label

    def make_new_angle_label(self,turtle):
        turtle.angle_for_label = turtle.heading + 90
        self.new_angle_label = Label(self, text='MouseAngle: N/A')
        self.new_angle_label.pack(side=RIGHT)
        return self.new_angle_label

    ####################################################
    # Simulation Related Methods
    ####################################################
    def add(self, turtle):
        """Add a new turtle to this arena."""
        self._turtles.append(turtle)
        if self._gui:
            self._items[turtle] = self.canvas.create_polygon(0, 0)
            self.update(turtle)


    def step(self, stop=True):
        """Advance all the turtles one step."""
        next_states = {}
        self._timestamp += self._period
        self.widget.config(text='Time [seconds]: ' +  str(round(self._timestamp/1000,2)))
        # turtle.radius = (turtle.position.x**2 + turtle.position.y**2)**0.5
        # self.radius_label.config(text='Radius: ' + str(round(turtle.radius/100,3)))
        # self.radius_label = Label(self, text='Radius: ' + str(round(turtle.radius/100,3)))
        for turtle in self._turtles:
            next_states[turtle] = turtle.getnextstate()
            # turtle.radius = (turtle.position.x**2 + turtle.position.y**2)**0.5
            # self.radius_label.config(text='Radius: ' + str(round(turtle.radius/100,3)))
        for turtle in self._turtles:
            turtle.setstate(next_states[turtle])
            if self._gui:
                self.update(turtle)
        if stop:
            self._running = 0
        if self._verbose:
            self.track()
        # self.make_time_widgets()

    def stop(self):
        """Stop the running turtles."""
        self._running = 0

    def run(self):
        """Start the turtles running."""
        self._running = 1
        self.loop()
        # self.make_time_widgets()


    def getinitial(self):
        if self._timestamp == 0:
            # print(self._timestamp)
            # initial_position = {}
            # initial_heading = {}
            for turtle in self._turtles:
                self.initial_position[turtle] = turtle.position
                self.initial_heading[turtle] = turtle.heading
        # print(self.initial_position, self.initial_heading)
        return self.initial_position, self.initial_heading

    def reset(self):
        next_states = {}
        if self._running:
            self.stop()
            # self.getinitial()
        for turtle in self._turtles:
            turtle.position = self.initial_position[turtle]
            turtle.heading = self.initial_heading[turtle]
            turtle.radius_for_label = (turtle.position.x**2 + turtle.position.y**2)**0.5
            self.radius_label.config(text='CatRadius: ' + str(round(turtle.radius_for_label/100,3)))
            self._timestamp = 0.00
            self.update(turtle)
            self.widget.config(text= 'Time [seconds]: ' +  str(round(self._timestamp/1000,2)))

    def loop(self):
        """Repeatedly advance all the turtles one step."""
        self.step(False)
        if self._running:
            self.tk.createtimerhandler(self.runtime_period, self.loop)
        elif not self._gui:
            exit(0)

    def track(self):
        """Print positions for Cat and Mouse"""
        if self._timestamp % 1000 == 0:
            print("Timestamp: {} s".format(self._timestamp / 1000))
            for turtle in self._turtles:
                print('{} {}'.format(turtle.__class__.__name__, turtle.position))
            print('-' * 20)
