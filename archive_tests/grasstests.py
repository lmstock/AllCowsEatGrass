# static grass for testing grass spread

import pygame

from dataclasses import dataclass, field
from itertools import count

from game_conf import *
from core import *

grass_img = pygame.image.load('grass.png')


@dataclass
class Grass():
    id_number: int = field(default_factory=count().__next__)
    name: str = "grass"
    coords: list[int] = field(default_factory=lambda: [0,0])
    width: int = 30

    def action(self):
        #print("grass action()")
        #print(self)
        game_display.blit(grass_img, self.coords)
        pygame.display.update()

def spawn_grass(x_coord, y_coord, actors):
    print("spawn_grass")
    grass = Grass(coords=[x_coord,y_coord])
    actors.insert(0,grass)
    game_display.blit(grass_img, grass.coords)
    print("spawn_grass(): new grass: ", grass.id_number, grass.coords)

def spawn_random_grass(actors):
    #print("spawn_random_grass")
    new_location = random_coords()
    spawn_grass(new_location[1][0], new_location[1][1], actors)

# actors list from scheduling
actors = []
new_actors = {}

# define grass locations
spawn_grass(0, 0, actors)
spawn_grass(0, 30, actors)


# grow grass function - pass in coords of grass to check, this is a grass action
def grow_grass(coords, actors):
    print("grow_grass")

    # select a coord 
    psc = [
        (coords[0]-30, coords[1]+30),
        (coords[0]-30, coords[1]),
        (coords[0]-30, coords[1]-30),

        (coords[0], coords[1]+30),
        (coords[0], coords[1]-30),

        (coords[0]+30, coords[1]+30),
        (coords[0]+30, coords[1]),
        (coords[0]+30, coords[1]-30),
    ]
    
    test_coord = random.choice(psc) 
    
    # check for existing grass
    locations = []

    # get all grass locations in actors list
    for i in actors:
        if i.name == "grass":
            new_location = (i.coords[0],i.coords[1])
            locations.append(new_location)

    print ("locations: ", locations)

    for i in locations:
        if i == test_coord:
            # cant spawn grass there
            print("space is occupied, grass will not grow here")
            return

        else:
            # spawn a grass there
            print("spawn grass at ", test_coord)
            spawn_grass(test_coord[0], test_coord[1], actors)
            return
    
            


       
    

grow_grass((0,0),actors)

for i in actors:
    print(i)


### probably need a 'check surrounding tiles' (cst) from which we can change the distance
### from entity, grass only needs to identify spawn points but mobile entities 
### need to sense things that are at a distance

