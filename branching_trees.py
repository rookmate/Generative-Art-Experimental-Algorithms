from turtle import *
from utils import set_theme

import random

def grow_tree(length, dec_factor, branch_angle, noise=0):
    if length > 10:
        width(length / 10)
        forward(length)
        new_len = length * dec_factor
        if noise > 0:
            new_len *= random.uniform(0.9, 1.1)

        angle_left = branch_angle + random.gauss(0, noise)
        angle_right = branch_angle + random.gauss(0, noise)

        left(angle_left)
        grow_tree(new_len, dec_factor, branch_angle, noise)
        right(angle_left)

        right(angle_right)
        grow_tree(new_len, dec_factor, branch_angle, noise)
        left(angle_right)

        backward(length)


def tree():
    set_theme(thickness=2)

    penup()
    goto(0, -400)
    left(90) # face cursor upwards
    pendown()
    grow_tree(150, 0.8, 25, 10)

    # Toggle tracer to get last line
    tracer(True)
    # Exit image on click
    exitonclick()

tree()
