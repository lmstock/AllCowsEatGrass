import random
import game_setup
import logthis





# d = dice, s = sides
def roll(d,s):
    logthis.logger.debug("roll")
    total = 0
    for i in range(1,d):    
        n = random.randint(1,s)
        total = total + n
    return total

def random_coords():
    logthis.logger.debug("random_coords")
    x = roll(2, game_setup.world_tiles_width)
    y = roll(2, game_setup.world_tiles_height)
    tile_coords = (x,y)
    display_coords = (x*30, y*30)
    return tile_coords, display_coords
    # x = random_coord()
    # print(x[0][0])



def turn():
    logthis.logger.debug("turn")
    game_setup.turn = game_setup.turn + 1
    print(game_setup.turn)

def coords_world_to_display(x,y):
    logthis.logger.debug("coords_world_to_display")
    x = x * 30
    y = y * 30
    return x,y


# return a list of tiles surrounding a coord
def get_surrounding_tiles(x, y, distance_away):
    logthis.logger.debug("get_surrounding_tiles")
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

