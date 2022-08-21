from turtle import *

from utils import set_theme

import random

def tiling(x, y, split, level, mode="diagonal"):
    # Reached final level of recursion. Start drawing image
    if level == 0:
        if mode == "straight":
            # vertical line
            if random.random() < 0.5:
                penup()
                goto(x, y - split)
                pendown()
                goto(x, y + split)
            else: # Horizontal line
                penup()
                goto(x - split, y)
                pendown()
                goto(x + split, y)
        elif mode == "diagonal":
            # Top left to bottom right
            if random.random() < 0.5:
                penup()
                goto(x - split, y + split)
                pendown()
                goto(x + split, y - split)
            else: # bottom left to top right
                penup()
                goto(x - split, y - split)
                pendown()
                goto(x + split, y + split)

    else:
        split /= 2
        level -= 1
        tiling(x - split, y + split, split, level, mode)
        tiling(x - split, y - split, split, level, mode)
        tiling(x + split, y + split, split, level, mode)
        tiling(x + split, y - split, split, level, mode)

def recursive_tiling(): 
    set_theme(thickness=3)

    tiling(0, 0, 400, 5, "diagonal")
    # Toggle tracer to get last line
    tracer(True)
    # Exit image on click
    exitonclick()

recursive_tiling()
