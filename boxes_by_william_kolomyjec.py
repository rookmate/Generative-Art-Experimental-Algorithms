from turtle import *
from utils import set_theme

import random
import math

def boxes():
    set_theme(canvas_width=1500, thickness=2)

    square_size = 25
    noise = 0.0

    for y in range(400, -400, -square_size):
        for x in range(-600, 600, square_size):
            # Move to location
            penup()
            goto(x, y)
            pendown()

            # Calculate Noise based on distance from the center
            max_distance = math.sqrt(600**2 + 400**2)
            # Distance is scaled based on the initial max width height defined
            distance = math.sqrt(x**2 + (600/400)**2 * y**2)
            # Noise adjusted from distance to center
            noise = (max_distance - distance) / 20 
            noise = noise if noise > 10 else 0
            # Rotate
            angle = random.uniform(-noise, noise)
            left(angle)
            # Draw Square
            for i in range(4):
                forward(square_size)
                left(90)

            right(angle)

        noise += 3.0

    # Toggle tracer to get last line
    tracer(True)
    # Exit image on click
    exitonclick()

boxes()
