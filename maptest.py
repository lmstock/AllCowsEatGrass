import pygame

from dataclasses import dataclass,field

import game_setup

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    K_b,
    K_p,
    KEYDOWN,
    QUIT, 
)

clock = pygame.time.Clock()

dirt_img = pygame.image.load('dirt.png')
tile_size = 30

@dataclass
class Locations():

    coords: list[int]
    width: int = 30
    type: str = "dirt"
    sprite: str = "dirt.png"

x = 20
y = 42

locoord = (x,y)
place = Locations(locoord)
print (place)

game_setup.game_display.fill(game_setup.white)
game_setup.game_display.blit(dirt_img, place.coords)
turn = 0
running = True

while running == True:

    if pygame.event.type == KEYDOWN:

        
        if pygame.event.key == K_ESCAPE:
            running = False
            

    



    pygame.display.update()
    clock.tick(.5)
    turn = turn + 1
    print(turn)

    
def build_world(x,y):
    for i in range(0,x):
        for j in range(0,y):
            print(i,j)

    # create a location instance for each coord

    # how to display img ?

