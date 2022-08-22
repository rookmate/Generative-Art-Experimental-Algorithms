from turtle import *
from utils import set_theme

import random

colors = [ (74/255, 61/255, 55/255),
        (130/255, 111/255, 94/255),
        (171/255, 166/255, 163/255),
        (213/255, 154/255, 113/255)
        ]

def scribbles():
    set_theme(thickness=2)

    size = 50
    points = 1
    for y in range(300, -300, -size):
        if points % 2 == 0:
            pencolor(colors[0][0], colors[0][2], colors[0][2])
        elif points % 3 == 0:
            pencolor(colors[1][0], colors[1][2], colors[1][2])
        elif points % 4 == 0:
            pencolor(colors[2][0], colors[2][2], colors[2][2])
        else:
            pencolor(colors[3][0], colors[3][2], colors[3][2])


        for x in range(-400, 400, size):
            # Starting point
            xorigin = px = x + random.uniform(-size / 4, size / 4)
            yorigin = py = y + random.uniform(-size / 4, size / 4)
            penup()
            goto(px, py)
            pendown()
            # Traversing edges and drawing line
            for i in range(points):
                px_next = x + random.uniform(-size / 4, size / 4)
                py_next = y + random.uniform(-size / 4, size / 4)
                goto(px_next, py_next)
                # setting next point
                px = px_next
                py = py_next

            # Go to orign
            goto(xorigin, yorigin)

        points += 1


    # Toggle tracer to get last line
    tracer(True)
    # Exit image on click
    exitonclick()

scribbles()
