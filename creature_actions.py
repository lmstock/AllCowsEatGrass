import random
import core
import logger2
import bartokmongo




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

    # do not exceed max_satiety remove from active task if full
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
def run(x):

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
    logger2.logger.debug("die")
    msg = " \033[31ma creature " + str(x['_id']) + " has passed from this mortal plane\033[0m"
    logger2.logger.info(msg)

    x['is_alive'] = False
    bartokmongo.remove_individual_byid(x["_id"])
    bartokmongo.add_to_mortuary(x)
    return x
    

# ATTACK
def attack(x):
    # attack another creature
    logger2.logger.debug("attack")

    # retreat if low health
    if x['health'][0] <= x['health'][1] * .2:
        logger2.logger.info("the attacker is retreating!")
        x['active_task'] = ['run', 1, 0, 3]  # this needs a direction
        x['target'] = None
        return x

    if x['target'] == 0 or x['target'] == None:
        logger2.logger.error("an attack was triggered but there was no target")
        return x

    # identify target set in trigger and get info
    target = bartokmongo.read_ind_by_id(x['target'])

    # check for proximity before attacking
    if abs(target['x'] - x['x']) > 2 or abs(target['y'] - x['y']) > 2:
        logger2.logger.info("target not in range")

        # go to location function
        pass

    else:

        # announce attack
        msg = " \033[31ma creature " + str(x['_id']) + " is attacking another " + str(target['_id']) + " !\033[0m"
        logger2.logger.info(msg)

        # determine damage        # check for full parry
        attack_dmg = 10           # this will vary in the future
    
        target_health = target['health']  # [current, max]
        total = target_health[0] - attack_dmg
        health = [total, target_health[1]]
        update = {'health': health}


        # defense damage
        x['health'][0] = x['health'][0] - target['defend']

        # update opponent
        bartokmongo.update_cret_byid(target['_id'], update)



    return x




    