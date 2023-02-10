import random
import pygame

from dataclasses import dataclass, field
from itertools import count

import logthis
import scheduler
import species
import game_setup
import game_imgs.imgs as imgs




@dataclass
class Creature:
    type: str
    img: str 
    bg_img: str
    size: str

    sleep_dur: float
    max_energy: float  # fully rested
    rest_gain: float
    base_fatigue: float
    energy: float

    creature_id: int = field(default_factory=count().__next__)
    world_coords: list[int] = field(default_factory=lambda: [250,250])
    task_q: list = field(default_factory=lambda: [])
    active_task: list = field(default_factory=lambda: ["wander", 3, 0, 7])
    age: int = 0


    # checks on what the individual is doing each turn
    def action(self):

        def increment_turn(self):
            logthis.logger.debug("increment_turn")
                
            # update attributes that change each turn
            if self.active_task[0] != "sleep":
                self.energy = round(self.energy + self.base_fatigue, 2)
            
            self.age = round(self.age + .01, 2)

        def trigger_tasks(self):
            logthis.logger.debug("trigger_tasks")

            def check_energy():
                if self.active_task == "sleep":
                    return

                # less than 40%
                if self.energy < self.max_energy * .4:
                    
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
                    
                    if self.energy < self.max_energy * .1:   # <10%
                        sleep = ["sleep", 1, 0, self.sleep_dur]

                    elif self.energy < self.max_energy * .3:   # <30%
                        sleep = ["sleep", 2, 0, self.sleep_dur]

                    elif self.energy < self.max_energy * .4:   # <40%
                        sleep = ["sleep", 3, 0, self.sleep_dur]

                    self.task_q.append(sleep)   

            check_energy()


            # check_satiety()  > very similar to check_energy

        def check_active_task(self):
            logthis.logger.debug("check_active_task")

            # clear task from q if completed
            if self.active_task[2] >= self.active_task[3]:
                self.active_task.clear()
            
            if self.active_task == []:

                # if no active task, get one
                def get_new_task(self):
                    logthis.logger.debug("get_new_task")

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

            if self.active_task[0] == "sleep":
                sleep(self)

            elif self.active_task[0] == "wander":
                wander(self)

            elif self.active_task[0] == "nothing":
                nothing(self)
                
        # creature activities
        def sleep(self):
            logthis.logger.debug("sleep")

            # increment current turn
            self.active_task[2] = self.active_task[2] + 1

            # increase energy
            self.energy = round(self.energy + self.rest_gain, 2)

            # do not exceed max_energy remove from active task if full
            if self.energy >= self.max_energy:
                self.energy = self.max_energy

                self.active_task[2] = self.active_task[3]

        # cover old sprite
        def cover_old_sprite(self):
            logthis.logger.debug("cover_old_sprite")
            
            game_setup.game_display.blit(self.bg_img, self.world_coords)
            pygame.display.update()

        def wander(self):
            logthis.logger.debug("wander")
            self.active_task[2] = self.active_task[2] + 1

            cover_old_sprite(self)

            dirs = ["e", "w", "n", "s"]
            c = random.choice(dirs)
            if c == "e": self.world_coords[0] = self.world_coords[0] + 30
            elif c == "w": self.world_coords[0] = self.world_coords[0] - 30
            elif c == "n": self.world_coords[1] = self.world_coords[1] + 30
            else: self.world_coords[1] = self.world_coords[1] - 30
            
            game_setup.game_display.blit(self.img, self.world_coords)
            pygame.display.update()

        def nothing(self):
            logthis.logger.debug("nothing")
            self.active_task[2] = self.active_task[2] + 1
    

        def update_viewport(self):
            logthis.logger.debug("update_viewport")
            game_setup.game_display.blit(self.img, self.world_coords)
            pygame.display.update()

        increment_turn(self)
        trigger_tasks(self)
        check_active_task(self)
        increment_active_task(self)

        update_viewport(self)








# requires a string from bestiary_names list
def generate_creature(creature_type):
    logthis.logger.debug("generate_creature")
    my_img = species.bestiary[creature_type]["img"]
    my_bg_img = species.bestiary[creature_type]["img_bg"]
    my_size = species.bestiary[creature_type]["size"]

    sleep_dur = species.bestiary[creature_type]["sleep_duration"]
    max_energy = species.bestiary[creature_type]["full_energy"]  # fully rested
    rest_gain = species.bestiary[creature_type]["rest_gain"]
    base_fatigue = species.bestiary[creature_type]["base_fatigue"]

    energy = species.bestiary[creature_type]["full_energy"]

    new_creature = Creature(
        creature_type,
        my_img,
        my_bg_img,
        my_size,
        sleep_dur,
        max_energy,
        rest_gain,
        base_fatigue,
        energy
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



