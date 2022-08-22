from turtle import *
from utils import set_theme

import random

def euler_curve(step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        right(angle)
        forward(step_size)
        angle += angle_step

def draw_euler_curves():
    set_theme(thickness=2)

    euler_curve(step_size = 7, angle_step = 0.6, n_steps = 10000)

    # Toggle tracer to get last line
    tracer(True)
    # Exit image on click
    exitonclick()

draw_euler_curves()
