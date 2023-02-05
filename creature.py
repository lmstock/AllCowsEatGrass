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
    creature_id: int = field(default_factory=count().__next__)
    world_coords: list[int] = field(default_factory=lambda: [250,250])
    task_q: list = field(default_factory=lambda: [])
    active_task: list = field(default_factory=lambda: ["wander", 3, 0, 7])
    
    age: int = 0
    energy: int = 47



    # checks on what the individual is doing each turn
    def action(self):

        def increment_turn(self):
            logthis.logger.debug("increment_turn")
                
            # update attributes that change each turn
            self.energy = self.energy - 1
            self.age = self.age + .01
            self.age = round(self.age,2)

        def trigger_tasks(self):
            logthis.logger.debug("trigger_tasks")
            def check_energy():
                if self.active_task == "sleep":
                    return

                if self.energy < 40:
                    
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
                    if self.energy < 10:
                        sleep = ["sleep", 1, 0, 7]

                    elif self.energy < 30:
                        sleep = ["sleep", 2, 0, 7]

                    elif self.energy < 40:
                        sleep = ["sleep", 3, 0, 7]

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
            self.active_task[2] = self.active_task[2] + 1
            self.energy = self.energy + 11

        # cover old sprite
        def cover_old_sprite():
            logthis.logger.debug("cover_old_sprite")
            game_setup.game_display.blit(imgs.bg_sprite, self.world_coords)
            pygame.display.update()

        def wander(self):
            logthis.logger.debug("wander")
            self.active_task[2] = self.active_task[2] + 1

            cover_old_sprite()

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
    my_pic = species.bestiary[creature_type]["img"]
    new_creature = Creature(creature_type, my_pic)
    logthis.logger.info(new_creature)

    # add to waiting room
    new_creature_data = new_creature.__dict__
    scheduler.population[new_creature.creature_id] = new_creature_data
    scheduler.waiting_room.append(new_creature)


def get_random_creature_type():
    logthis.logger.debug("get_random_creature_type")
    f = random.choice(species.bestiary_names)
    return f

