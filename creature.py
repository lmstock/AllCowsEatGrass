import pygame
import random

import mongotest
import logger2
import inc_turn
import triggers
import chk_active_task
import inc_active_task
import game_conf

import game_imgs.cret_imgs as cret_imgs


def creature_action(s):
    logger2.logger.debug("creature_action")

    s = inc_turn.increment_turn(s)
    s = triggers.trigger_tasks(s)

    s = chk_active_task.check_active_task(s)
    w = inc_active_task.increment_active_task(s)

    if w == None:
        return
    
    else:
        hist_tracking(w, 20)
        update_viewport(w)
        mongotest.update_cret_byid(w['_id'], w)



# OTHER
def update_viewport(w):
    logger2.logger.debug("update_viewport")
    
    coords = (w['x'],w['y'])
    img_index = int(w['img'])

    x = cret_imgs.crets_list[img_index]
    
    game_conf.w.game_display.blit(x, coords)
    pygame.display.update()

    # hist_tracking(x, 'rest_track', x['rest'][0], 20)


def hist_tracking(x, hist_duration):
    logger2.logger.debug("hist_tracking")

    x['rest_hist'].append(x['rest'][0])
    if len(x['rest_hist']) > hist_duration:
        x['rest_hist'].pop(0)

    x['satiety_hist'].append(x['satiety'][0])
    if len(x['satiety_hist']) > hist_duration:
        x['satiety_hist'].pop(0)

    x['energy_hist'].append(x['energy'][0])
    if len(x['energy_hist']) > hist_duration:
        x['energy_hist'].pop(0)
    
    x['hostility_hist'].append(x['hostility'][0])
    if len(x['hostility_hist']) > hist_duration:
        x['hostility_hist'].pop(0)

    x['health_hist'].append(x['health'][0])
    if len(x['health_hist']) > hist_duration:
        x['health_hist'].pop(0)

    return x

# creates a creature from a species in db.bestiary
def generate_creature(creature_type):
    logger2.logger.debug("generate_creature")

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
    
    "interrupt": [],
    "is_alive": True,
    "rest_hist": [],
    "satiety_hist": [],
    "energy_hist": [],
    "hostility_hist": [],
    "health_hist": []
    }
    

    mongotest.add_creature(new_creature)


def get_random_creature_type():
    logger2.logger.debug("get_random_creature_type")
    return random.choice(mongotest.list_beasts())
    

