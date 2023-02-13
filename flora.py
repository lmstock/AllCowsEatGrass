import random
import pygame

from dataclasses import dataclass, field
from itertools import count

import logthis
import scheduler
import game_setup
import flora_species
import core


@dataclass
class Flora:
    type: str
    img: str
    #bg_img: str
    size: str
    energy: int
    growth_data: list
    coords: list[int] 

    flora_id: int = field(default_factory=count().__next__)
    
    age: int = 0


    # checks on what the individual is doing each turn
    def action(self):
        logthis.logger.debug("action")

        def increment_turn(self):
            logthis.logger.debug("increment_turn")

            # update attributes that change each turn
            self.age = round(self.age + .01, 2)

        def grow(self):
            logthis.logger.debug("grow")

        def update_viewport(self):
            logthis.logger.debug("update_viewport")
            game_setup.game_display.blit(self.img, self.coords)
            pygame.display.update()

        increment_turn(self)
        grow(self)
        update_viewport(self)
        

def generate_flora(flora_type):
    logthis.logger.debug("generate flora")

    my_img = flora_species.herbarium[flora_type]["img"]
    my_size = flora_species.herbarium[flora_type]["size"]
    
    get_coords = core.random_coords()

    
    new_flora = Flora (
        flora_type,
        my_img,
        my_size,
        energy = 100,
        growth_data = [],
        coords = get_coords
)

    logthis.logger.info(new_flora)

    # add to green room
    new_flora_data = new_flora.__dict__
    scheduler.flora_population[new_flora.flora_id] = new_flora_data
    scheduler.green_room.append(new_flora)

def get_random_flora_type():
    logthis.logger.debug("get_random_flora_type")
    f = random.choice(flora_species.herbarium_names)
    return f

