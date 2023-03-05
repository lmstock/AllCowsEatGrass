
import pygame
import random


flors_list = [
    pygame.image.load('game_imgs\\flor1_tiny.png'),
    pygame.image.load('game_imgs\\flor1_small.png'),
    pygame.image.load('game_imgs\\flor1_medium.png'),
    pygame.image.load('game_imgs\\flor1_large.png'),
    pygame.image.load('game_imgs\\flor1_very_large.png'),
    pygame.image.load('game_imgs\\flor1_mega.png'),
    pygame.image.load('game_imgs\\flor2_tiny.png'),
    pygame.image.load('game_imgs\\flor2_small.png'),
    pygame.image.load('game_imgs\\flor2_medium.png'),
    pygame.image.load('game_imgs\\flor2_large.png'),
    pygame.image.load('game_imgs\\flor2_very_large.png'),
    pygame.image.load('game_imgs\\flor2_mega.png'),
    pygame.image.load('game_imgs\\flor3_tiny.png'),
    pygame.image.load('game_imgs\\flor3_small.png'),
    pygame.image.load('game_imgs\\flor3_medium.png'),
    pygame.image.load('game_imgs\\flor3_large.png'),
    pygame.image.load('game_imgs\\flor3_very_large.png'),
    pygame.image.load('game_imgs\\flor3_mega.png'),
    pygame.image.load('game_imgs\\flor4_tiny.png'),
    pygame.image.load('game_imgs\\flor4_small.png'),
    pygame.image.load('game_imgs\\flor4_medium.png'),
    pygame.image.load('game_imgs\\flor4_large.png'),
    pygame.image.load('game_imgs\\flor4_very_large.png'),
    pygame.image.load('game_imgs\\flor4_mega.png'),
    pygame.image.load('game_imgs\\flor5_tiny.png'),
    pygame.image.load('game_imgs\\flor5_small.png'),
    pygame.image.load('game_imgs\\flor5_medium.png'),
    pygame.image.load('game_imgs\\flor5_large.png'),
    pygame.image.load('game_imgs\\flor5_very_large.png'),
    pygame.image.load('game_imgs\\flor5_mega.png'),
    pygame.image.load('game_imgs\\flor6_tiny.png'),
    pygame.image.load('game_imgs\\flor6_small.png'),
    pygame.image.load('game_imgs\\flor6_medium.png'),
    pygame.image.load('game_imgs\\flor6_large.png'),
    pygame.image.load('game_imgs\\flor6_very_large.png'),
    pygame.image.load('game_imgs\\flor6_mega.png'),
    pygame.image.load('game_imgs\\flor7_tiny.png'),
    pygame.image.load('game_imgs\\flor7_small.png'),
    pygame.image.load('game_imgs\\flor7_medium.png'),
    pygame.image.load('game_imgs\\flor7_large.png'),
    pygame.image.load('game_imgs\\flor7_very_large.png'),
    pygame.image.load('game_imgs\\flor7_mega.png')
]

flor_pool_tiny = [0,6,12,18,24,30,36]

flor_pool_small = [1,7,13,19,25,31,37]

flor_pool_medium = [2,8,14,20,26,32,38]

flor_pool_large = [3,9,15,21,27,33,39]

flor_pool_very_large = [4,10,16,22,28,34,40]

flor_pool_mega = [5,11,17,23,29,35,41]


def choose_flor_img(size):
    match size:
        case "tiny":
            x = random.choice(flor_pool_tiny)
            flor_pool_tiny.remove(x)
            print(x)
            return x
        
        case "small":
            x = random.choice(flor_pool_small)
            flor_pool_small.remove(x)
            print(x)
            return x
        
        case "medium":
            x = random.choice(flor_pool_medium)
            flor_pool_medium.remove(x)
            print(x)
            return x
        
        case "large":
            x = random.choice(flor_pool_large)
            flor_pool_large.remove(x)
            print(x)
            return x
        
        case "very_large":
            x = random.choice(flor_pool_very_large)
            flor_pool_very_large.remove(x)
            print(x)            
            return x
        
        case "mega":
            x = random.choice(flor_pool_mega)
            flor_pool_mega.remove(x)
            print(x)            
            return x



