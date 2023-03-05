import random

import mongotest

import archive_tests.logthis as logthis
import inc_turn as it
import triggers
import chk_active_task
import inc_active_task
import game_conf
import pygame
import game_imgs.cret_imgs as cret_imgs




def creature_action(s):

    t = it.increment_turn(s)
    u = triggers.trigger_tasks(t)
    v = chk_active_task.check_active_task(u)
    w = inc_active_task.increment_active_task(v)

    mongotest.update_cret_byid(w['_id'], w)

    update_viewport(w)



# OTHER
def update_viewport(w):
    logthis.logger.debug("update_viewport")
    coords = (w['x'],w['y'])
    img_index = int(w['img'])

    x = cret_imgs.crets_list[img_index]
    
    game_conf.g.game_display.blit(x, coords)
    pygame.display.update()


# creates a creature from a species in db.bestiary
def generate_creature(creature_type):
    logthis.logger.debug("generate_creature")

    # this will return cursor object
    s = mongotest.read_creature_species("species_type", creature_type)
    
    # iterate through it with i
    for i in s:
        print(i)

    # add to db
    new_creature = {
    "species_type": i["species_type"],
    "img": i["species_img"],
    "size": i["size"],

    "sleep_dur": i["sleep_duration"],
    "rest_gain": i["rest_gain"],
    "base_fatigue": i["base_fatigue"],
    "rest": i["rest"],  # fully rested
    
    "satiety": i["satiety"],
    "energy": i["energy"],

    "hostility": i["hostility"],  
    "health": i["health"],

    "speed": i["speed"],
    "fov": i["fov"],

    "age": 0,

    "x": 250,
    "y": 250,
    "task_q": [],
    "active_task": [],
    
    # type: [observation count, investigation count, reaction code]  ## .5 knowledge indicates own species
    "knowledge_base": {creature_type: [.5, .5, 1]},
    
    "interrupt": []
    }
    

    mongotest.add_creature(new_creature)


def get_random_creature_type():
    logthis.logger.debug("get_random_creature_type")
    return random.choice(mongotest.list_beasts())
    

