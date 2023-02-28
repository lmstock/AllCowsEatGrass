import pygame
import random


cret1_tiny=pygame.image.load('game_imgs\\cret1_tiny.png')
cret1_small=pygame.image.load('game_imgs\\cret1_small.png')
cret1_medium=pygame.image.load('game_imgs\\cret1_medium.png')
cret1_large=pygame.image.load('game_imgs\\cret1_large.png')
cret1_very_large=pygame.image.load('game_imgs\\cret1_very_large.png')
cret1_mega=pygame.image.load('game_imgs\\cret1_mega.png')
cret2_tiny=pygame.image.load('game_imgs\\cret2_tiny.png')
cret2_small=pygame.image.load('game_imgs\\cret2_small.png')
cret2_medium=pygame.image.load('game_imgs\\cret2_medium.png')
cret2_large=pygame.image.load('game_imgs\\cret2_large.png')
cret2_very_large=pygame.image.load('game_imgs\\cret2_very_large.png')
cret2_mega=pygame.image.load('game_imgs\\cret2_mega.png')
cret3_tiny=pygame.image.load('game_imgs\\cret3_tiny.png')
cret3_small=pygame.image.load('game_imgs\\cret3_small.png')
cret3_medium=pygame.image.load('game_imgs\\cret3_medium.png')
cret3_large=pygame.image.load('game_imgs\\cret3_large.png')
cret3_very_large=pygame.image.load('game_imgs\\cret3_very_large.png')
cret3_mega=pygame.image.load('game_imgs\\cret3_mega.png')
cret4_tiny=pygame.image.load('game_imgs\\cret4_tiny.png')
cret4_small=pygame.image.load('game_imgs\\cret4_small.png')
cret4_medium=pygame.image.load('game_imgs\\cret4_medium.png')
cret4_large=pygame.image.load('game_imgs\\cret4_large.png')
cret4_very_large=pygame.image.load('game_imgs\\cret4_very_large.png')
cret4_mega=pygame.image.load('game_imgs\\cret4_mega.png')
cret5_tiny=pygame.image.load('game_imgs\\cret5_tiny.png')
cret5_small=pygame.image.load('game_imgs\\cret5_small.png')
cret5_medium=pygame.image.load('game_imgs\\cret5_medium.png')
cret5_large=pygame.image.load('game_imgs\\cret5_large.png')
cret5_very_large=pygame.image.load('game_imgs\\cret5_very_large.png')
cret5_mega=pygame.image.load('game_imgs\\cret5_mega.png')
cret6_tiny=pygame.image.load('game_imgs\\cret6_tiny.png')
cret6_small=pygame.image.load('game_imgs\\cret6_small.png')
cret6_medium=pygame.image.load('game_imgs\\cret6_medium.png')
cret6_large=pygame.image.load('game_imgs\\cret6_large.png')
cret6_very_large=pygame.image.load('game_imgs\\cret6_very_large.png')
cret6_mega=pygame.image.load('game_imgs\\cret6_mega.png')
cret7_tiny=pygame.image.load('game_imgs\\cret7_tiny.png')
cret7_small=pygame.image.load('game_imgs\\cret7_small.png')
cret7_medium=pygame.image.load('game_imgs\\cret7_medium.png')
cret7_large=pygame.image.load('game_imgs\\cret7_large.png')
cret7_very_large=pygame.image.load('game_imgs\\cret7_very_large.png')
cret7_mega=pygame.image.load('game_imgs\\cret7_mega.png')

# bg_sprite_tiny = pygame.image.load('game_imgs\\bg_sprite_tiny.png')
# bg_sprite_small = pygame.image.load('game_imgs\\bg_sprite_small.png')
# bg_sprite_medium = pygame.image.load('game_imgs\\bg_sprite_medium.png')
# bg_sprite_large = pygame.image.load('game_imgs\\bg_sprite_large.png')
# bg_sprite_very_large = pygame.image.load('game_imgs\\bg_sprite_very_large.png')
# bg_sprite_mega = pygame.image.load('game_imgs\\bg_sprite_mega.png')




cret_pool_tiny = [
    cret1_tiny,
    cret2_tiny,
    cret3_tiny,
    cret4_tiny,
    cret5_tiny,
    cret6_tiny,
    cret7_tiny
]

cret_pool_small = [
    cret1_small,
    cret2_small,
    cret3_small,
    cret4_small,
    cret5_small,
    cret6_small,
    cret7_small
]

cret_pool_medium = [
    cret1_medium,
    cret2_medium,
    cret3_medium,
    cret4_medium,
    cret5_medium,
    cret6_medium,
    cret7_medium
]

cret_pool_large = [
    cret1_large,
    cret2_large,
    cret3_large,
    cret4_large,
    cret5_large,
    cret6_large,
    cret7_large
]

cret_pool_very_large = [
    cret1_very_large,
    cret2_very_large,
    cret3_very_large,
    cret4_very_large,
    cret5_very_large,
    cret6_very_large,
    cret7_very_large
]

cret_pool_mega = [
    cret1_mega,
    cret2_mega,
    cret3_mega,
    cret4_mega,
    cret5_mega,
    cret6_mega,
    cret7_mega
]


def choose_img(size):
    match size:
        case "tiny":
            x = random.choice(cret_pool_tiny)
            cret_pool_tiny.remove(x)
            return x
        
        case "small":
            x = random.choice(cret_pool_small)
            cret_pool_small.remove(x)
            return x
        
        case "medium":
            x = random.choice(cret_pool_medium)
            cret_pool_medium.remove(x)
            return x
        
        case "large":
            x = random.choice(cret_pool_large)
            cret_pool_large.remove(x)
            return x
        
        case "very_large":
            x = random.choice(cret_pool_very_large)
            cret_pool_very_large.remove(x)
            return x
        
        case "mega":
            x = random.choice(cret_pool_mega)
            cret_pool_mega.remove(x)
            return x



