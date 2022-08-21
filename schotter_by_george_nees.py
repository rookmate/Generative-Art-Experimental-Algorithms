from turtle import *
from utils import set_theme

import random


def schotter():
    set_theme(canvas_width=600, thickness=2)

    square_size = 50
    noise = 0.0

    for y in range(400, -400, -square_size):
        for x in range(-250, 250, square_size):
            # Move to location
            penup()
            goto(x, y)
            pendown()

            # Rotate
            angle = random.uniform(-noise, noise)
            left(angle)

            # Draw Square
            for i in range(4):
                forward(square_size)
                left(90)

            right(angle)

        noise += 3.5

    # Toggle tracer to get last line
    tracer(True)
    # Exit image on click
    exitonclick()

schotter()
