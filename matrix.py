


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

tiles = get_surrounding_tiles(0,0,2)
print(tiles)


