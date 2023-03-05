
import pygame
import random


crets_list = [
    pygame.image.load('game_imgs\\cret1_tiny.png'),
    pygame.image.load('game_imgs\\cret1_small.png'),
    pygame.image.load('game_imgs\\cret1_medium.png'),
    pygame.image.load('game_imgs\\cret1_large.png'),
    pygame.image.load('game_imgs\\cret1_very_large.png'),
    pygame.image.load('game_imgs\\cret1_mega.png'),
    pygame.image.load('game_imgs\\cret2_tiny.png'),
    pygame.image.load('game_imgs\\cret2_small.png'),
    pygame.image.load('game_imgs\\cret2_medium.png'),
    pygame.image.load('game_imgs\\cret2_large.png'),
    pygame.image.load('game_imgs\\cret2_very_large.png'),
    pygame.image.load('game_imgs\\cret2_mega.png'),
    pygame.image.load('game_imgs\\cret3_tiny.png'),
    pygame.image.load('game_imgs\\cret3_small.png'),
    pygame.image.load('game_imgs\\cret3_medium.png'),
    pygame.image.load('game_imgs\\cret3_large.png'),
    pygame.image.load('game_imgs\\cret3_very_large.png'),
    pygame.image.load('game_imgs\\cret3_mega.png'),
    pygame.image.load('game_imgs\\cret4_tiny.png'),
    pygame.image.load('game_imgs\\cret4_small.png'),
    pygame.image.load('game_imgs\\cret4_medium.png'),
    pygame.image.load('game_imgs\\cret4_large.png'),
    pygame.image.load('game_imgs\\cret4_very_large.png'),
    pygame.image.load('game_imgs\\cret4_mega.png'),
    pygame.image.load('game_imgs\\cret5_tiny.png'),
    pygame.image.load('game_imgs\\cret5_small.png'),
    pygame.image.load('game_imgs\\cret5_medium.png'),
    pygame.image.load('game_imgs\\cret5_large.png'),
    pygame.image.load('game_imgs\\cret5_very_large.png'),
    pygame.image.load('game_imgs\\cret5_mega.png'),
    pygame.image.load('game_imgs\\cret6_tiny.png'),
    pygame.image.load('game_imgs\\cret6_small.png'),
    pygame.image.load('game_imgs\\cret6_medium.png'),
    pygame.image.load('game_imgs\\cret6_large.png'),
    pygame.image.load('game_imgs\\cret6_very_large.png'),
    pygame.image.load('game_imgs\\cret6_mega.png'),
    pygame.image.load('game_imgs\\cret7_tiny.png'),
    pygame.image.load('game_imgs\\cret7_small.png'),
    pygame.image.load('game_imgs\\cret7_medium.png'),
    pygame.image.load('game_imgs\\cret7_large.png'),
    pygame.image.load('game_imgs\\cret7_very_large.png'),
    pygame.image.load('game_imgs\\cret7_mega.png')
]

cret_pool_tiny = [0,6,12,18,24,30,36]

cret_pool_small = [1,7,13,19,25,31,37]

cret_pool_medium = [2,8,14,20,26,32,38]

cret_pool_large = [3,9,15,21,27,33,39]

cret_pool_very_large = [4,10,16,22,28,34,40]

cret_pool_mega = [5,11,17,23,29,35,41]


def choose_cret_img(size):
    match size:
        case "tiny":
            x = random.choice(cret_pool_tiny)
            cret_pool_tiny.remove(x)
            print(x)
            return x
        
        case "small":
            x = random.choice(cret_pool_small)
            cret_pool_small.remove(x)
            print(x)
            return x
        
        case "medium":
            x = random.choice(cret_pool_medium)
            cret_pool_medium.remove(x)
            print(x)
            return x
        
        case "large":
            x = random.choice(cret_pool_large)
            cret_pool_large.remove(x)
            print(x)
            return x
        
        case "very_large":
            x = random.choice(cret_pool_very_large)
            cret_pool_very_large.remove(x)
            print(x)            
            return x
        
        case "mega":
            x = random.choice(cret_pool_mega)
            cret_pool_mega.remove(x)
            print(x)            
            return x



