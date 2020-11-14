import pygame as PG

#list = [800,600]
#tuple = (800,600)

color_salmon = (250, 200, 114)

window_height = 600
window_width = 800

img_o = PG.transform.scale(  PG.image.load('download.jpeg'), (100,100))

gameDisplay = PG.display.set_mode((window_width, window_height))

playing = True

while playing:
    user_event = PG.event.get()
    events = len(user_event)

    while events > 0:
        print(user_event)
        if(user_event[events - 1].type == PG.QUIT):
            playing = False
        events = events - 1

    gameDisplay.fill(color_salmon)
    gameDisplay.blit(img_o, (100, 100))

    PG.display.update()
