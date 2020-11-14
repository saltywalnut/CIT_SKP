import pygame as PG

#list = [800,600]
#tuple = (800,600)

window_height = int ( input ("Type height : "))
window_width = 800

PG.display.set_mode((window_width, window_height))

clock = PG.time.Clock()

crashed = False

while not crashed:

    for event in PG.event.get():
        if event.type == PG.QUIT:
            crashed = True

        print(event)

    PG.display.update()
    clock.tick(60)
