
import random
import historical
import mongotest
import logger2
import inc_turn
import triggers

import inc_active_task



def creature_action(s):
    logger2.logger.debug("creature_action")

    s = inc_turn.increment_turn(s)
    s = triggers.trigger_tasks(s)
    s = inc_active_task.increment_active_task(s)


    if s == None:
        return
    
    else:
        historical.history_tracking(s) # save data in increments of x in order to capture longer term data
        mongotest.update_cret_byid(s['_id'], s)



# creates a creature from a species in db.bestiary
def generate_creature(creature_type):
    logger2.logger.debug("generate_creature")

    # this will return cursor object
    s = mongotest.read_creature_species("species_type", creature_type)
    
    # iterate through it with i
    for i in s:
        logger2.logger.debug(i)

    # add to db
    new_creature = {
    "species_type": i["species_type"],
    "size": i["size"],

    "sleep_dur": i["sleep_duration"],
    "rest_gain": i["rest_gain"],
    "rest": i["rest"],  # fully rested
    
    "satiety": i["satiety"],
    "energy": i["energy"],

    "hostility": i["hostility"],  
    "health": i["health"],

    "speed": i["speed"],
    "fov": i["fov"],

    "age": .0000025,

    "x": 250,
    "y": 250,
    "task_q": [],
    "active_task": [],
    "repr_cooldown": [0, 25],
    "offspring": 0,
    
    # type: [observation count, investigation count, reaction code]  ## .5 knowledge indicates own species
    "knowledge_base": {creature_type: [.5, .5, 1]},
    
    "is_alive": True
    
    }
    

    mongotest.add_creature(new_creature)


def get_random_creature_type():
    logger2.logger.debug("get_random_creature_type")
    return random.choice(mongotest.list_beasts())
    

