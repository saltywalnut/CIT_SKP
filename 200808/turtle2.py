from turtle import *
#
# count = 4
#
# while count > 0:
#     forward (200)
#     left (90)
#     count -= 1
#
# done()

# def blue_screen():
#     write(" good day ", True, "center", ("Times New Roman", 80, "normal"))
#     bgcolor (0.7, 1.0, 1.0)
#
# def white_screen():
#     bgcolor (1.0, 1.0, 1.0)
#
# listen()
# onkey(blue_screen, 'a')
# onscreenclick(white_screen)
# done()

def up():
    setheading(90)
    forward(100)

def down():
    setheading(270)
    forward(100)

def left():
    setheading(180)
    forward(100)

def right():
    setheading(0)
    forward(100)

listen()

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

onkey(up, 'w')
onkey(down, 's')
onkey(left, 'a')
onkey(right, 'd')

done()
