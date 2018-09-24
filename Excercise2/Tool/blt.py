#!/bin/sh
import time
from Tkinter import *  # The Tk package
import Pmw  # The Python MegaWidget package
import math  # import the sin-function
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')


class equations:
    #h(t) = 3 * pi * exp(-lambda [t] )
    #lambda ( t ) = 5 * sin ( 2 * pi * 1 * t )
    @staticmethod
    def h(t):
        h=3*math.pi*math.exp(-1 * equations.lambdaT(t)) #lambdaT to differentiate from predefined one
        return h
    @staticmethod
    def lambdaT(t):
        lambdaT= 5 * math.sin(2 * math.pi * 1 * t)
        return lambdaT



def animate():

     for t in range(10):  # In 31 steps...
         for c in range(ncurves):  # ...on each curve
             for x in range(npoints):  # on each point...
                 vector_y[c][x] = equations.h(x)

         master.update_idletasks()  # update screen


def symbolsOnOff():
    global symbols
    symbols = not symbols

    for curvename in g.element_show():
        if symbols:
            g.element_configure(curvename, symbol='diamond')
        else:
            g.element_configure(curvename, symbol='')


def smooth():
    global smoothing

    if smoothing == 'linear':
        smoothing = 'quadratic'
    elif smoothing == 'quadratic':
        smoothing = 'natural'
    elif smoothing == 'natural':
        smoothing = 'step'
    else:
        smoothing = 'linear'

    for curvename in g.element_show():
        g.element_configure(curvename, smooth=smoothing)


master = Tk()  # build Tk-environment
ncurves = 1
npoints = 100
smoothing = 'linear'
symbols = 0

vector_x = Pmw.Blt.Vector()
vector_y = []

for y in range(ncurves):
    vector_y.append(Pmw.Blt.Vector())

for x in range(npoints):  # for each point...
    vector_x.append(x * 0.1)  # make an x-value

    # fill vectors with cool graphs
    for c in range(ncurves):  # for each curve...
        vector_y[c].append(math.sin(c * x * 0.5))  # make an y-value

g = Pmw.Blt.Graph(master)  # make a new graph area
g.pack(expand=1, fill='both')

color = ['red', '#ff9900', 'blue', '#00cc00', 'black', 'grey']

for c in range(ncurves):
    curvename = 'h(t)'
    g.line_create(curvename,
                  xdata=vector_x,
                  ydata=vector_y[c],
                  color=color[c],
                  dashes=0,
                  linewidth=2,
                  symbol='')

g.configure(title='VIZZ... Tool')

# make s row of buttons
buttons = Pmw.ButtonBox(master, labelpos='n', label_text='Options')
buttons.pack(fill='both', expand=1, padx=10, pady=10)

buttons.add('Start', command=animate)
buttons.add('Grid', command=g.grid_toggle)
buttons.add('Points', command=symbolsOnOff)
buttons.add('Smooth', command=smooth)
buttons.add('Quit', command=master.quit)



master.mainloop()  # ...and wait for input

#source
#Copyright 1997,1998 by Telstra Corporation Limited, Australia (ACN 051 775 556)
#https://www.slac.stanford.edu/grp/cd/soft/pmw/

