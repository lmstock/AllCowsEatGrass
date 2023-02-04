import pygame


# game display
world_tiles_width = 40
world_tiles_height = 30

display_width = world_tiles_width * 30
display_height = world_tiles_height * 30


# vars
black = (0,0,0)
white = (255,255,255)
bg = (27, 59, 87)


pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
game_display.fill(bg) 
pygame.display.set_caption("all cows eat grass")
pygame.display.update()


#clock = pygame.time.Clock()
turn = 0
running = True