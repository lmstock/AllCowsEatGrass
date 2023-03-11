import random

import logger2




        





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
    # observing fov and gathering knowledge
    logger2.logger.debug("observe")
    pass
    
    # #update task
    # x['active_task'][2] = x['active_task'][2] + 1

    # cret_type = scheduler.population[x]["type"]
    # cret_action = scheduler.population[x]["active_task"]
    
    # # if x in kb update observation
    # if n in x.knowledge_base.keys():
    #     x.knowledge_base[cret_type][0][0] = x.knowledge_base[cret_type][0][0] +1
    # else:
    #     # add species to knowledge base
    #     x.knowledge_base[cret_type] = [1,0,1]

    # if cret_action == "attack":
    #     x.knowledge_base[cret_type][0][2] = 3   # retreat
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



    