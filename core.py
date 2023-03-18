import random

import game_conf
import logger2







# d = dice, s = sides
def roll(d,s):
    logger2.logger.debug("roll")
    total = 0
    for i in range(d):    
        n = random.randint(1,s)
        total = total + n
    return total

def random_coords():
    logger2.logger.debug("random_coords")
    x = roll(2, game_conf.g.display_width / 2)
    y = roll(2, game_conf.g.display_height / 2)
    coord = (x,y)
    return coord



    

##you are going to want this...
# marked for removal 2/11/23
def coords_world_to_display(x,y):
    logger2.logger.debug("coords_world_to_display")
    x = x * 30
    y = y * 30
    return x,y


# return a list of tiles surrounding a coord
def get_surrounding_tiles(x, y, distance_away):
    logger2.logger.debug("get_surrounding_tiles")
    distance = distance_away
    surrounding_tiles = []

    lower_x = x - distance
    upper_x = x + distance + 1

    lower_y = y - distance
    upper_y = y + distance + 1

    for i in range(lower_x, upper_x):
        for j in range(lower_y, upper_y):
            tup = (i,j)
            surrounding_tiles.append(tup)

    return surrounding_tiles

