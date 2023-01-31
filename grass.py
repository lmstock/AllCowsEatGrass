import pygame
import random

from dataclasses import dataclass, field
from itertools import count

from game_setup import *
from core import *


grass_img = pygame.image.load('grass.png')


@dataclass
class Grass():
    id_number: int = field(default_factory=count().__next__)
    name: str = "grass"
    coords: list[int] = field(default_factory=lambda: [0,0])

    def action(self):
        print("grass action()")
        print(self)
        game_display.blit(grass_img, self.coords)
        pygame.display.update()






def spawn_grass(x_coord, y_coord, new_actors):
    print("spawn_grass")
    grass = Grass(coords=[x_coord,y_coord])
    new_actors.insert(0,grass)
    game_display.blit(grass_img, grass.coords)

def spawn_random_grass(new_actors):
    print("spawn_random_grass")
    new_location = random_coords()
    spawn_grass(new_location[1][0], new_location[1][1], new_actors)
    



