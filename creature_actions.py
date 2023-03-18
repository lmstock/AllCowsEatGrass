import random

import logger2
import mongotest



def sleep(x):
    logger2.logger.debug("sleep")

    # increment current active_task
    x['active_task'][2] = x['active_task'][2] + 1

    # increase current_rest
    x['rest'][0] = round(x['rest'][0] + x['rest_gain'], 2)

    # do not exceed max_rest remove from active task if full
    if x['rest'][0] >= x['rest'][1]:
        x['rest'][0] = x['rest'][1]

        x['active_task'][2] = x['active_task'][3]


    return x

def eat(x):
    logger2.logger.debug("eat")

    # increment current turn in task list
    x['active_task'][2] = x['active_task'][2] + 1

    # increase satiety
    x['satiety'][0] = round(x['satiety'][0] + 15, 2)  # 10 is just a guess food input

    # do not exceed max_rest remove from active task if full
    if x['satiety'][0] >= x['satiety'][2]:

        x['satiety'][0] = x['satiety'][2]

        #instead of this, remove from active task
        x['active_task'] = []
    
    return x

def wander(x):
    logger2.logger.debug("wander")
    x['active_task'][2] = x['active_task'][2] + 1
    speed = x['speed']

    #cover_old_sprite(x)

    dirs = ["w", "nw", "ne", "e","se", "s", "sw"]
    c = random.choice(dirs)
    
    if c == "w": x['x'] = x['x'] - speed

    elif c == "nw": 
        x['x'] = x['x'] - speed
        x['y'] = x['y'] + speed
        
    elif c == "n": x['y'] = x['y'] + speed
    
    elif c == "ne":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] + speed

    elif c == "e": x['x'] = x['x'] + speed
    
    elif c == "se":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] - speed

    elif c == "s": x['y'] = x['y'] - speed  # s

    else:   #sw
        x['x'] = x['x'] - speed
        x['y'] = x['y'] - speed
    
    # game_conf.g.game_display.blit(x.img, x.world_coords)
    # pygame.display.update()

    return x

def nothing(x):
    # doing nothing brings you down :(
    logger2.logger.debug("nothing")

    #update task
    x['active_task'][2] = x['active_task'][2] + 1

    return x

def observe(x):
    logger2.logger.info("observe")
    print(x['active_task'])
    # observing serves to update the knowledge base, reaction code

    #update task count
    x['active_task'][2] = x['active_task'][2] + 1

    #creature we are interacting with is passed in through active_task
    cret = x["active_task"][4]
    cret_id = cret[0]
    cret_species_type = cret[1]
    cret_active_task = cret[2]

    # add if not in kb
    if cret_species_type not in x['knowledge_base']:
        x['knowledge_base'][cret_species_type] = [0,0,1]

    # if creature is currently attacking set reaction code to flee
    def set_reaction_code():
        logger2.logger.info("set_reaction_code")

        # set reaction code
        if cret_active_task == "attack":
            reaction_code = 3

        else: 
            reaction_code = 1

        return reaction_code
    
    r = set_reaction_code()
    
    # update observation count
    x["knowledge_base"][cret_species_type][0] = x["knowledge_base"][cret_species_type][0] + 1

    # set reaction code
    if x["knowledge_base"][cret_species_type][2] == 3:
        pass
    else:
        x["knowledge_base"][cret_species_type][2] = r
    
    # if observation count = 10? add key {"hostility" : cret_hostility} (pass in with other 3 data)
    # for now observation data can grow

    return x
        
def investigate(x):
    # knowledge gathering
    logger2.logger.debug("investigate")

    #update task
    x['active_task'][2] = x['active_task'][2] + 1

    return x

def play(x):
    logger2.logger.debug("play")
    x['active_task'][2] = x['active_task'][2] + 1

    speed = x['speed'] * 1.5

    #cover_old_sprite(x)

    dirs = ["w", "nw", "ne", "e","se", "s", "sw"]
    c = random.choice(dirs)
    
    if c == "w": x['x'] = x['x'] - speed

    elif c == "nw": 
        x['x'] = x['x'] - speed
        x['y'] = x['y'] + speed
        
    elif c == "n": x['y'] = x['y'] + speed
    
    elif c == "ne":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] + speed

    elif c == "e": x['x'] = x['x'] + speed
    
    elif c == "se":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] - speed

    elif c == "s": x['y'] = x['y'] - speed  

    else:   #sw
        x['x'] = x['x'] - speed
        x['y'] = x['y'] - speed
    

    return x

def die(x):
    # health runs out
    logger2.logger.info("die")
    msg = " \033[31ma creature " + str(x['_id']) + " has passed from this mortal plane\033[0m"
    logger2.logger.info(msg)

    x['is_alive'] = False
    mongotest.remove_individual_byid(x["_id"])
    mongotest.add_to_mortuary(x)
    

    