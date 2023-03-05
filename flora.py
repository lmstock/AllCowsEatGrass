import random
import pygame

from dataclasses import dataclass, field
from itertools import count

import archive_tests.logthis as logthis
import mongotest
import scheduler
import game_conf
import flora_species
import core
import game_imgs.flor_imgs as flor_imgs



# checks on what the individual is doing each turn
def flora_action(self):
    logthis.logger.debug("action")

    def increment_turn(f):
        logthis.logger.debug("increment_turn")

        # update attributes that change each turn
        f['age'] = round(f['age'] + .01, 2)
        return f

    def grow(f):
        logthis.logger.debug("grow")
        return f

    def update_viewport(f):
        logthis.logger.info("update_viewport")
        coords = (f['x'],f['y'])
        img_index = int(f['img'])

        x = flor_imgs.flors_list[img_index]
        game_conf.g.game_display.blit(x, coords)
        pygame.display.update()

    a = increment_turn(self)
    b = grow(a)
    update_viewport(b)
        

def generate_flora(flora_type):
    logthis.logger.info("generate flora")

    s = mongotest.read_flora_species("flora_type", flora_type)
    x = random.randint(0,250)
    y = random.randint(0,250)

    # iterate through with i
    for i in s:
        print(i)

    # add to db
    new_flora = {
        "flora_species_type": i["flora_species_type"],
        "size": i["size"],
        "flora_type": i["flora_type"],
        "energy": i["energy"],
        "growth_data": i["growth_data"],   
        "x": x,
        "y": y,
        "age": 0,
        "img": i['img']

    }


    mongotest.add_flora(new_flora)


def get_random_flora_type():
    logthis.logger.debug("get_random_flora_type")
    return random.choice(mongotest.list_flora())


