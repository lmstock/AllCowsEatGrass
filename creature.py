
import random
import historical
import bartokmongo
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
        bartokmongo.update_cret_byid(s['_id'], s)



# creates a creature from a species in db.bestiary
def generate_creature(creature_type):
    logger2.logger.debug("generate_creature")

    # this will return cursor object
    s = bartokmongo.read_creature_species_du("species_type", creature_type)
    new_creature = {}
    # iterate through it with i
    for k,v in s.items():
        new_creature[k] = v

    # remove id
    new_creature.pop("_id")
    # remove mutation count

    new_creature["task_q"] = []
    new_creature["active_task"] = []
    new_creature["age"] = .0000025
    new_creature["x"] = 250
    new_creature["y"] = 250
    new_creature["offspring"] = 0
    new_creature["attack"] = 10
    new_creature["defend"]= 10
    new_creature["target"]= 0  # cret id
    
    # creatures within fov
    new_creature["local_crets"] = []

    # type: [observation count, investigation count, reaction code]  ## .5 knowledge indicates own species
    species_type = new_creature["species_type"]
    new_creature["knowledge_base"] = {species_type: [.5, .5, 1]}
    
    new_creature["is_alive"] = True
    
    

    bartokmongo.add_creature(new_creature)


def get_random_creature_type():
    logger2.logger.debug("get_random_creature_type")
    return random.choice(bartokmongo.list_beasts())
    

