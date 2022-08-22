from turtle import *

def set_theme(canvas_width = 1000,
        canvas_height = 1000,
        canvas_color = (228/255, 227/255, 224/255),
        pen_color = (74/255, 61/255, 55/255),
        thickness = 1,
        _speed = 0,
        tracer_bool = False,
        hide_turtle = True
        ):
    setup (canvas_width, canvas_height)
    bgcolor(canvas_color)
    color(pen_color)
    width(thickness)
    speed(_speed)
    tracer(tracer_bool)
    if hide_turtle:
        hideturtle()
