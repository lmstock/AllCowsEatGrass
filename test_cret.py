import random
import pygame

from dataclasses import dataclass, field
from itertools import count

import logthis
import scheduler
import species
import game_setup
import game_imgs.imgs as imgs

# energy related to sleep is now called current_rest and max_rest


@dataclass
class Creature:
    type: str
    img: str 
    bg_img: str
    size: str

    # sleep attributes
    sleep_dur: float
    rest_gain: float
    base_fatigue: float

    rest: list # (current rest, max rest)
    satiety: list   # (current satiety, max satiety)
    energy: list   # (current, max)   

    hostility: list  # (current hostility, max hostility)  # to help define behavior toward other creatures
    health: list  # (current, max) # sickness introduced by prolonged hunger or fatigue or injury
    speed: float  # movement attributes

    creature_id: int = field(default_factory=count().__next__)
    world_coords: list[int] = field(default_factory=lambda: [250,250])
    task_q: list = field(default_factory=lambda: [])
    active_task: list = field(default_factory=lambda: ["wander", 3, 0, 7])
    age: int = 0
    knowledge_base = {}

    satiety_lost_per_turn = 1

    # checks on what the individual is doing each turn
    def action(self):

        def increment_turn(self):
            logthis.logger.debug("increment_turn")
                
            # update attributes that change each turn
            if self.active_task[0] != "sleep":
                self.rest[0] = round(self.rest[0] + self.base_fatigue, 2)

            if self.active_task[0] != "eat":
                self.satiety[0] = round(self.satiety[0] - self.satiety_lost_per_turn, 2)
            
            self.age = round(self.age + .0000025, 7)


        def trigger_tasks(self):
            logthis.logger.debug("trigger_tasks")

            # SLEEP TRIGGER
            def check_current_rest():
                if self.active_task == "sleep":
                    return

                # less than 40%
                if self.rest[0] < self.rest[1] * .4:
                    
                    # remove old sleep tasks from queue
                    def remove_old_sleeps():
                        logthis.logger.debug("remove_old_sleeps")
                        if self.task_q == []:
                            return

                        else:
                            for i in self.task_q:
                                if i[0] == "sleep":
                                    self.task_q.remove(i)

                    remove_old_sleeps()

                    # add sleep task - [task, priority, current turn, max turn]
                    if self.rest[0] < self.rest[1] * .1:   # <10%
                        sleep = ["sleep", 1, 0, self.sleep_dur]

                    elif self.rest[0] < self.rest[1] * .3:   # <30%
                        sleep = ["sleep", 2, 0, self.sleep_dur]

                    elif self.rest[0] < self.rest[1] * .4:   # <40%
                        sleep = ["sleep", 3, 0, self.sleep_dur]

                    self.task_q.append(sleep)   

            check_current_rest()

            def check_current_satiety():
                if self.active_task == "eat":
                    pass

                else:
                    # if satiety less than 40%
                    if self.satiety[0] < self.satiety[1] * .4:
                        
                        # remove old eat tasks from task_q if present
                        def remove_old_eats():
                            logthis.logger.debug("remove_old_eats")

                            if self.task_q == []:
                                pass

                            else:
                                for i in self.task_q:
                                    if i[0] == "eat":
                                        self.task_q.remove(i)

                        remove_old_eats()

                        # add eat task - [task, priority, current turn, max turn]
                        if self.satiety[0] < self.satiety[1] * .1:   # <10%
                            eat = ["eat", 1, 0, 6]

                        elif self.satiety[0] < self.satiety[1] * .3:   # <30%
                            eat = ["eat", 2, 0, 6]

                        elif self.satiety[0] < self.satiety[1] * .4:   # <40%
                            eat = ["eat", 3, 0, 6]

                        self.task_q.append(eat) 

                    # if satiety is not less than 40%    
                    else: pass

            check_current_satiety()


        # checks active task for existence or completion
        def check_active_task(self):
            logthis.logger.debug("check_active_task")

            # clear task from q if completed
            if self.active_task[2] >= self.active_task[3]:
                self.active_task.clear()
            
            if self.active_task == []:

                # if no active task, get one
                def get_new_task(self):
                    logthis.logger.debug("get_new_task")

                    #if task_q is empty, pass
                    x = bool(self.task_q)
                    if x == False:
                        pass
                    else:
                        duration = random.randint(1,8)

                        p1,p2,p3 = [],[],[]

                        for i in self.task_q:
                            if i[1] == 1: p1.append(i)
                            elif i[1] == 2: p2.append(i)
                            else: p3.append(i)

                        if p1 != []: x = random.choice(p1)
                        elif p2 != []: x = random.choice(p2)
                        elif p3 != []: x = random.choice(p3)
                        else: x = ["wander", 3, 0, duration]

                        try:
                            self.task_q.remove(x)
                        except Exception as e:
                            pass

                        return x

                self.active_task = get_new_task(self)
                       

        def increment_active_task(self):
            logthis.logger.debug("increment_active_task")

            #if active_task is empty, pass
            x = bool(self.task_q)
            if x == False:
                pass

            else:

                if self.active_task[0] == "sleep":
                    sleep(self)

                elif self.active_task[0] == "wander":
                    wander(self)

                elif self.active_task[0] == "nothing":
                    nothing(self)

                elif self.active_task[0] == "eat":
                    eat(self)
                

        # CREATURE ACTIVITIES
        def sleep(self):
            logthis.logger.debug("sleep")
            print("sleep")

            # increment current turn
            self.active_task[2] = self.active_task[2] + 1

            # increase current_rest
            self.rest[0] = round(self.rest[0] + self.rest_gain, 2)

            # do not exceed max_rest remove from active task if full
            if self.rest[0] >= self.rest[1]:
                self.rest[0] = self.rest[1]

                self.active_task[2] = self.active_task[3]

        def eat(self):
            logthis.logger.debug("eat")

            # increment current turn in task list
            self.active_task[2] = self.active_task[2] + 1

            # increase satiety
            self.satiety[0] = round(self.satiety[0] + 15, 2)  # 10 is just a guess food input

            # do not exceed max_rest remove from active task if full
            if self.satiety[0] >= self.satiety[1]:

                self.satiety[0] = self.satiety[1]

                #instead of this, remove from active task
                self.active_task[2] = self.active_task[3]

        def cover_old_sprite(self):
            logthis.logger.debug("cover_old_sprite")
            
            game_setup.game_display.blit(self.bg_img, self.world_coords)
            pygame.display.update()

        def wander(self):
            logthis.logger.debug("wander")
            self.active_task[2] = self.active_task[2] + 1
            speed = self.speed

            cover_old_sprite(self)

            dirs = ["w", "nw", "ne", "e","se", "s", "sw"]
            c = random.choice(dirs)
            
            if c == "w": self.world_coords[0] = self.world_coords[0] - speed

            elif c == "nw": 
                self.world_coords[0] = self.world_coords[0] - speed
                self.world_coords[1] = self.world_coords[1] + speed
                
            elif c == "n": self.world_coords[1] = self.world_coords[1] + speed
            
            elif c == "ne":
                self.world_coords[0] = self.world_coords[0] + speed
                self.world_coords[1] = self.world_coords[1] + speed

            elif c == "e": self.world_coords[0] = self.world_coords[0] + speed
            
            elif c == "se":
                self.world_coords[0] = self.world_coords[0] + speed
                self.world_coords[1] = self.world_coords[1] - speed

            elif c == "s": self.world_coords[1] = self.world_coords[1] - speed  # s

            else:   #sw
                self.world_coords[0] = self.world_coords[0] - speed
                self.world_coords[1] = self.world_coords[1] - speed
            
            game_setup.game_display.blit(self.img, self.world_coords)
            pygame.display.update()

        def nothing(self):
            # doing nothing brings you down :(
            logthis.logger.debug("nothing")
            self.active_task[2] = self.active_task[2] + 1
    

        # OTHER
        # def update_viewport(self):
        #     logthis.logger.debug("update_viewport")
        #     game_setup.game_display.blit(self.img, self.world_coords)
        #     pygame.display.update()

        increment_turn(self)
        trigger_tasks(self)
        check_active_task(self)
        increment_active_task(self)

        # update_viewport(self)








# requires a string from bestiary_names list
def generate_creature(creature_type):
    logthis.logger.debug("generate_creature")
    
    my_img = species.bestiary[creature_type]["img"]
    my_bg_img = species.bestiary[creature_type]["img_bg"]
    my_size = species.bestiary[creature_type]["size"]

    sleep_dur = species.bestiary[creature_type]["sleep_duration"]
    max_rest = species.bestiary[creature_type]["max_rest"]  # fully rested
    rest_gain = species.bestiary[creature_type]["rest_gain"]
    base_fatigue = species.bestiary[creature_type]["base_fatigue"]

    rest = [max_rest, max_rest]
    
    speed = species.bestiary[creature_type]["speed"]
    
    satiety_mx = species.bestiary[creature_type]["satiety"]
    satiety = [satiety_mx, satiety_mx]

    hostility_mx = species.bestiary[creature_type]["hostility"]   
    hostility = [hostility_mx, hostility_mx]
    
    health_mx = species.bestiary[creature_type]["health"]
    health = [health_mx, health_mx]

    energy_mx = species.bestiary[creature_type]["energy"]
    energy = [energy_mx, energy_mx]

    new_creature = Creature(
        creature_type,
        my_img,
        my_bg_img,
        my_size,

        sleep_dur,
        rest_gain,
        base_fatigue,

        rest,
        satiety,
        energy,

        hostility,
        health,
        speed
        )

    logthis.logger.info(new_creature)

    # add to waiting room
    new_creature_data = new_creature.__dict__
    scheduler.population[new_creature.creature_id] = new_creature_data
    scheduler.waiting_room.append(new_creature)


def get_random_creature_type():
    logthis.logger.debug("get_random_creature_type")
    f = random.choice(species.bestiary_names)
    return f


x =species.generate_species()
generate_creature(x)
