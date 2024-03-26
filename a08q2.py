#!/usr/bin/env python
# coding: utf-8

# In[3]:


from typing import *
import check
import math
import ipycanvas
import random

def mondrian(canvas: ipycanvas.Canvas,
             x0: float, y0: float, width: float, depth: int) -> None:
    """Draw the Mondrian fractal on the canvas with points x0,y0, width of the rectangle and depth"""
    
    canvas.fill_rect(x0, y0, width*0.47)
    canvas.fill_rect(x0+0.53*width, y0+0.53*width, width*0.47)
    
    if depth > 0:
        mondrian(canvas, x0+0.53*width, y0, 0.47*width, depth-1)
        mondrian(canvas, x0, y0 + 0.53*width, 0.47*width, depth-1)


def randomcolour(canvas: ipycanvas.Canvas) -> None:
    """Randomly change the colour to be used in subsequent fills on canvas."""
    canvas.fill_style = random.choice(('gold', 'crimson', 
                                       'mediumblue', 'seashell', 'seashell'))


canvas = ipycanvas.Canvas(width=320, height=200)

check.expect("RC0", randomcolour(ipycanvas.Canvas(width=10, height=10)), None)
check.expect("RC1", randomcolour(canvas), None)


canvas.fill_style='black'
canvas.fill_rect(0, 50, 150)
canvas.fill_style='crimson'
check.expect("", mondrian(canvas, 0, 50, 150, 4), None)

canvas.fill_style='black'
canvas.fill_rect(220, 0, 100)
canvas.fill_style='crimson'
check.expect("", mondrian(canvas, 220, 0, 100, 1), None)

canvas.fill_style='black'
canvas.fill_rect(185, 120, 50)
canvas.fill_style='crimson'
check.expect("", mondrian(canvas, 185, 120, 50, 0), None)

display(canvas)

