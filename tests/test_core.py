import random
import test_logger2 as logger2







# d = dice, s = sides
def roll(d,s):
    logger2.logger.debug("roll")
    total = 0
    for i in range(d):    
        n = random.randint(1,s)
        total = total + n
    return total


def incr_active_task(x):
    x['active_task'][2] = x['active_task'][2] + 1
    return x

def fence(x):
    if x['x'] > 999:
        x['x'] = 999

    if x['x'] < -999:
        x['x'] = -999

    if x['y'] > 999:
        x['y'] = 999

    if x['y'] < -999:
        x['y'] = -999

    return x

    

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

