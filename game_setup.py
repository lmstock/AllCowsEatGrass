import pygame


# game display
display_width = 1200
display_height = 600


# vars
black = (0,0,0)
white = (255,255,255)
bg = (27, 59, 87)


pygame.init()

# creating a clock object
clock=pygame.time.Clock()

game_display = pygame.display.set_mode((display_width, display_height))

game_display.fill(bg) 
pygame.display.set_caption("clockmaker")

pygame.display.update()

turn = 0
running = True