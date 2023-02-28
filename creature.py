import random
import pygame

from dataclasses import dataclass, field
from itertools import count

import chk_active_task as cat
import inc_active_task as iac
import inc_turn as it
import logthis
import scheduler
import species
import game_conf
import triggers
import game_imgs.imgs as imgs
import mongotest

from game_conf import Game_config
from creature_actions import sleep, eat, wander, nothing, play, observe


# being mindful of class size
# https://softwareengineering.stackexchange.com/questions/11846/how-large-is-ok-for-a-class

# moving Creature methods outside of class to keep size down.
# not finding much cons in doing so.


@dataclass
class Creature:

    #basic
    type: str
    img: str 
    size: str

    # sleep attributes
    rest: list # (current rest, max rest)
    sleep_dur: float
    rest_gain: float
    base_fatigue: float
    
    # gen health
    satiety: list   # (current satiety, loss per turn, max satiety)
    energy: list   # (current, max)   
    hostility: list  # (current hostility, max hostility)  # to help define behavior toward other creatures
    health: list  # (current, max) # sickness introduced by prolonged hunger or fatigue or injury
    
    speed: list  # movement attributes
    fov: int # field of "vision"
    age: float = 0

    creature_id: int = field(default_factory=count().__next__)
    world_coords: list[int] = field(default_factory=lambda: [250,250])
    task_q: list = field(default_factory=lambda: [])
    active_task: list = field(default_factory=lambda: ["wander", 3, 0, 7])
    knowledge_base: dict = field(default_factory=lambda:{})
    interrupt: list = field(default_factory=lambda: [False, "no interrupt"])
    

    # checks on what the individual is doing each turn
    # the functions have been moved out due to size

    def action(self):

        

        # OTHER
        def update_viewport(self):
            logthis.logger.debug("update_viewport")
            game_conf.g.game_display.blit(self.img, self.world_coords)
            pygame.display.update()

        it.increment_turn(self)
        triggers.trigger_tasks(self)
        cat.check_active_task(self)
        iac.increment_active_task(self)
        update_viewport(self)





# requires a string from bestiary_names list
def generate_creature(creature_type):
    logthis.logger.debug("generate_creature")
    
    my_type = species.bestiary[creature_type]["name"]
    my_img = species.bestiary[creature_type]["img"]
    my_size = species.bestiary[creature_type]["size"]

    sleep_dur = species.bestiary[creature_type]["sleep_duration"]
    rest_gain = species.bestiary[creature_type]["rest_gain"]
    base_fatigue = species.bestiary[creature_type]["base_fatigue"]
    rest = species.bestiary[creature_type]["rest"]  # fully rested
    
    satiety = species.bestiary[creature_type]["satiety"]
    energy = species.bestiary[creature_type]["energy"]

    hostility = species.bestiary[creature_type]["hostility"]   
    health = species.bestiary[creature_type]["health"]

    speed = species.bestiary[creature_type]["speed"]
    fov = species.bestiary[creature_type]["fov"]


    new_creature = Creature(
        my_type,
        my_img,
        my_size,

        rest,
        sleep_dur,
        rest_gain,
        base_fatigue,

        satiety,
        energy,
        hostility,
        health,
        
        speed,
        fov,
        age = 0,

        # type: [observation count, investigation count, reaction code]  ## .5 knowledge indicates own species
        knowledge_base={creature_type: [.5, .5, 1]}  
    )

    logthis.logger.info(new_creature)

    # add to waiting room
    new_creature_data = new_creature.__dict__
    scheduler.population[new_creature.creature_id] = new_creature_data
    scheduler.waiting_room.append(new_creature)


    # # add to db
    new_creature = {
        "creature_id": new_creature.creature_id,
        "type": my_type,
        "img": str(my_img),
        "size": my_size,
        "rest": rest,
        "sleep_duration": sleep_dur,
        "rest_gain": rest_gain,
        "base_fatigue": base_fatigue,
        "satiety": satiety,
        "energy": energy,
        "hostility": hostility,
        "health": health,
        "speed": speed,
        "fov": fov,
        "age": new_creature.age,
        "knowledge_base": new_creature.knowledge_base
    }


    mongotest.add_creature(new_creature)


def get_random_creature_type():
    logthis.logger.debug("get_random_creature_type")
    f = random.choice(species.bestiary_names)
    return f



