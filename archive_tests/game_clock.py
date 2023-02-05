# importing the pygame module
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    K_b,
    K_p,
    K_a,
    K_w,
    KEYDOWN, 
    QUIT, 
)

bg = (27, 59, 87)

# initialising the pygame
pygame.init()
game_display = pygame.display.set_mode((200, 200))
game_display.fill(bg) 
pygame.display.set_caption("clockmaker")
pygame.display.update()

running = True
	
turn = 0


# creating a clock object
clock=pygame.time.Clock()



while running:

	clock.tick(.25)
	turn = turn + 1 
	print(turn)
	
	for event in pygame.event.get():
		if event.type == KEYDOWN:

			if event.key == K_ESCAPE:
				running = False
	
			if event.key == K_a:
				print("hi")




	
