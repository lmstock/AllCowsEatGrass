import random
import pygame

import logthis
import game_conf
import scheduler





def sleep(x):
    logthis.logger.debug("sleep")

    # increment current active_task
    x.active_task[2] = x.active_task[2] + 1

    # increase current_rest
    x.rest[0] = round(x.rest[0] + x.rest_gain, 2)

    # do not exceed max_rest remove from active task if full
    if x.rest[0] >= x.rest[1]:
        x.rest[0] = x.rest[1]

        x.active_task[2] = x.active_task[3]


def eat(x):
    logthis.logger.debug("eat")

    # increment current turn in task list
    x.active_task[2] = x.active_task[2] + 1

    # increase satiety
    x.satiety[0] = round(x.satiety[0] + 15, 2)  # 10 is just a guess food input

    # do not exceed max_rest remove from active task if full
    if x.satiety[0] >= x.satiety[1]:

        x.satiety[0] = x.satiety[1]

        #instead of this, remove from active task
        x.active_task = []


def wander(x):
    logthis.logger.debug("wander")
    x.active_task[2] = x.active_task[2] + 1
    speed = x.speed[1]

    #cover_old_sprite(x)

    dirs = ["w", "nw", "ne", "e","se", "s", "sw"]
    c = random.choice(dirs)
    
    if c == "w": x.world_coords[0] = x.world_coords[0] - speed

    elif c == "nw": 
        x.world_coords[0] = x.world_coords[0] - speed
        x.world_coords[1] = x.world_coords[1] + speed
        
    elif c == "n": x.world_coords[1] = x.world_coords[1] + speed
    
    elif c == "ne":
        x.world_coords[0] = x.world_coords[0] + speed
        x.world_coords[1] = x.world_coords[1] + speed

    elif c == "e": x.world_coords[0] = x.world_coords[0] + speed
    
    elif c == "se":
        x.world_coords[0] = x.world_coords[0] + speed
        x.world_coords[1] = x.world_coords[1] - speed

    elif c == "s": x.world_coords[1] = x.world_coords[1] - speed  # s

    else:   #sw
        x.world_coords[0] = x.world_coords[0] - speed
        x.world_coords[1] = x.world_coords[1] - speed
    
    game_conf.g.game_display.blit(x.img, x.world_coords)
    pygame.display.update()

def nothing(x):
    # doing nothing brings you down :(
    logthis.logger.debug("nothing")

    #update task
    x.active_task[2] = x.active_task[2] + 1

def observe(x, n):
    # observing fov and gathering knowledge
    logthis.logger.debug("observe")

    #update task
    x.active_task[2] = x.active_task[2] + 1

    cret_type = scheduler.population[x]["type"]
    cret_action = scheduler.population[x]["active_task"]
    
    # if x in kb update observation
    if n in x.knowledge_base.keys():
        x.knowledge_base[cret_type][0][0] = x.knowledge_base[cret_type][0][0] +1
    else:
        # add species to knowledge base
        x.knowledge_base[cret_type] = [1,0,1]

    if cret_action == "attack":
        x.knowledge_base[cret_type][0][2] = 3   # retreat

        
def investigate(x):
    # knowledge gathering
    logthis.logger.debug("investigate")

    #update task
    x.active_task[2] = x.active_task[2] + 1

def play(x):
    logthis.logger.debug("play")
    x.active_task[2] = x.active_task[2] + 1

    speed = x.speed[2]

    #cover_old_sprite(x)

    dirs = ["w", "nw", "ne", "e","se", "s", "sw"]
    c = random.choice(dirs)
    
    if c == "w": x.world_coords[0] = x.world_coords[0] - speed

    elif c == "nw": 
        x.world_coords[0] = x.world_coords[0] - speed
        x.world_coords[1] = x.world_coords[1] + speed
        
    elif c == "n": x.world_coords[1] = x.world_coords[1] + speed
    
    elif c == "ne":
        x.world_coords[0] = x.world_coords[0] + speed
        x.world_coords[1] = x.world_coords[1] + speed

    elif c == "e": x.world_coords[0] = x.world_coords[0] + speed
    
    elif c == "se":
        x.world_coords[0] = x.world_coords[0] + speed
        x.world_coords[1] = x.world_coords[1] - speed

    elif c == "s": x.world_coords[1] = x.world_coords[1] - speed  # s

    else:   #sw
        x.world_coords[0] = x.world_coords[0] - speed
        x.world_coords[1] = x.world_coords[1] - speed
    
    game_conf.g.game_display.blit(x.img, x.world_coords)
    pygame.display.update()



    