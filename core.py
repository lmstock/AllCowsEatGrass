import random
import game_setup





# d = dice, s = sides
def roll(d,s):
    total = 0
    for i in range(1,d):    
        n = random.randint(1,s)
        total = total + n
    return total

def random_coords():
    x = roll(2, game_setup.world_tiles_width)
    y = roll(2, game_setup.world_tiles_height)
    tile_coords = (x,y)
    display_coords = (x*30, y*30)
    return tile_coords, display_coords
    # x = random_coord()
    # print(x[0][0])

# takes tile coords as tuple and returns display coords
def calculate_display_coords(coords):
    x = coords[0]
    y = coords[1]
    tile_size = 30
    x_display = int(game_setup.display_width/2) + (x * tile_size)
    y_display = int(game_setup.display_height/2) + (y * tile_size)
    display_tuple = x_display, y_display
    return display_tuple

def turn():
    game_setup.turn = game_setup.turn + 1
    print(game_setup.turn)




# return a list of tiles surrounding a coord
def get_surrounding_tiles(x, y, distance_away):
    
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

