# set stoptime from the entry given by the users

from tkinter import *

master = Tk()

# tk = Tk()
# tk = Tk()

v = StringVar()
e = Entry(master, width=85, textvariable=v)
e.pack()

v.set("Enter a numerical stoptime in mintues after which the cat would give up. First 'Update'to check and then 'OK' to start.")

# stoptime = 30

def callback():
        stoptime_inmin = v.get()
        stoptime = float(stoptime_inmin)*60*1000
        #entered number x in min, so x*60*10^3 ms

        if stoptime <=0:
            print("Please enter something bigger than 0!")
        else:
            print('The Cat would give up after ' + stoptime_inmin + ' minutes.')
        return stoptime
ok = Button(master, text='OK', command=master.destroy).pack(side=BOTTOM)
b = Button(master, text="Check", width=10, command=callback)
b.pack()


master.mainloop()
