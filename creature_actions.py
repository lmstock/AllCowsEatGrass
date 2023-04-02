import random
import core
import logger2
import mongotest



def sleep(x):
    logger2.logger.debug("sleep")

    # increment active_task
    x = core.incr_active_task(x)

    # increase current_rest
    x['rest'][0] = round(x['rest'][0] + x['rest_gain'], 2)

    # do not exceed max_rest remove from active task if full
    if x['rest'][0] >= x['rest'][2]:
        x['rest'][0] = x['rest'][2]

        # clear active_task
        x['active_task'] = []

    return x


def eat(x):
    logger2.logger.debug("eat")

    # increment active_task
    x = core.incr_active_task(x)

    # increase satiety
    x['satiety'][0] = round(x['satiety'][0] + 33, 2)  

    # do not exceed max_rest remove from active task if full
    if x['satiety'][0] >= x['satiety'][2]:
        x['satiety'][0] = x['satiety'][2]

        # clear active task
        x['active_task'] = []
    
    return x


def wander(x):
    logger2.logger.debug("wander")

    # increment active_task
    x = core.incr_active_task(x)
    speed = x['speed']

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

    x = core.fence(x)
    
    return x
     

# NEEDS INVENTED, WRITTEN, AND TEST WRITTEN
def investigate(x):
    # knowledge gathering
    logger2.logger.debug("investigate")

    # increment active_task
    x = core.incr_active_task(x)

    return x


# WANDER FASTER
def play(x):

    # increment active_task
    x = core.incr_active_task(x)

    speed = x['speed'] * 1.5

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

    x = core.fence(x)
    return x


def die(x):
    # health runs out
    logger2.logger.info("die")
    msg = " \033[31ma creature " + str(x['_id']) + " has passed from this mortal plane\033[0m"
    logger2.logger.info(msg)

    x['is_alive'] = False
    mongotest.remove_individual_byid(x["_id"])
    mongotest.add_to_mortuary(x)
    return x
    

    