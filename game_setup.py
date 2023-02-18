import pygame
from world import World


# game display
display_width = 1200
display_height = 600



pygame.init()

w = World()
running = True

bg_color = w.get_bg_color()

# creating a clock object
clock=pygame.time.Clock()

game_display = pygame.display.set_mode((display_width, display_height))

game_display.fill(bg_color) 
pygame.display.set_caption("clockmaker")

pygame.display.update()