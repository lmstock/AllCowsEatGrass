

my_coords = [0,0]


population = {
    1: {
        "p": 1,
        "type": "nonan",
        "coords": [-100, 50] },
    2: {
        "p": 2,
        "type": "geun",
        "coords": [2000, -3000]
        },
    3: {
        "p": 3,
        "type": "ut",
        "coords": [2000, -100]
    }
}



# FIELD OF VIEW CHECK
def get_fov(my_coords):

    # check fov
    x_range = my_coords[0] - 1000, my_coords[0] + 1000
    y_range = my_coords[1] - 1000, my_coords[1] + 1000
    fov = (x_range, y_range)
    return fov

y = get_fov(my_coords)

def check_fov(fov):
    print(fov)
    for i in population.items():
        if i[1]['coords'][0] in range(fov[0][0], fov[0][1]):
            if i[1]['coords'][1] in range(fov[1][0], fov[1][1]):
                print("yes")
        else: print("no")
        

check_fov(y)

# x = 10

# if x in range(2, 15):
#     print("yes")