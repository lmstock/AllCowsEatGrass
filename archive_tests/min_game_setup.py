import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT, 
)


white = (255,255,255)

display_width = 800
display_height = 600

running = True
turn = 0

pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
game_display.fill(white) 
pygame.display.set_caption("all cows eat grass")
pygame.display.update()



def main(turn, running):
    print("main")

    while running == True:
        event = pygame.event.wait()

        if event.type == KEYDOWN:
            turn = turn + 1
            print (turn)

            if event.key == K_ESCAPE:
                print("escape key")
                running = False

            if event.key == K_DOWN:
                print("down")

            if event.key == K_SPACE:
                print("turn:  = ", turn)

main(turn, running)