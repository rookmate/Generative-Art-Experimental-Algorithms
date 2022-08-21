from turtle import *
from utils import set_theme

import random

def draw_square(x, y, split):
    penup()
    goto(x - split/2, y - split/2)
    pendown()
    for i in range(4):
        forward(split)
        left(90)

def nested_squares():
    set_theme(thickness=3)

    square_size = 100
    noise = 5
    shrink = 15

    for x in range(-400 + square_size//2, 400, square_size):
        for y in range(-400 + square_size//2, 400, square_size):

            # Draw outer squares
            draw_square(x ,y , square_size)

            # Get offsets
            x_offset = random.uniform(-noise, noise)
            y_offset = random.uniform(-noise, noise)

            # Draw inner squares
            for i in range(6):
                draw_square(x + i * x_offset, y + i * y_offset, square_size - i * shrink)
    
    # Toggle tracer to get last line
    tracer(True)
    # Exit image on click
    exitonclick()

nested_squares()
