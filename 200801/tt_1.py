from turtle import *


def rect (x,y,w,h,c):
    pensize (10)
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

rect (200, 50, 200, 300, "red")
rect (-50, -300, 100, 80, "purple")
rect (70, -100, 30, 50, "blue")




# strokes = 4
# y = 50
# length = y*2
#
# while strokes > 0:
#     forward (length)
#     left (90)
#     forward (y)
#     left (90)
#     strokes -= 1

# sides = int ( input ("Type number of sides : ") )
# angle = 360/sides
# length = 300 / sides
#
# while sides > 0:
#     forward(length)
#     left(angle)
#     sides -= 1

done()
