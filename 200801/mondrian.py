from turtle import *


def rect (x,y,w,h,c):
    penup()
    fillcolor (c)
    goto(x,y)
    pendown()
    begin_fill ()
    count = 2
    while count > 0:
        forward (w)
        left (90)
        forward (h)
        left (90)
        count -= 1
    end_fill()

rect (-50, 0, 50, 60, "red")
rect (0, 40, 15, 20, "yellow")
rect (-50, -30, 50, 30, "white")
rect (0, -30, 15, 30, "blue")
rect (0, 0, 15, 40, "white")

done ()
