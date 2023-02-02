import random
import pygame

from dataclasses import dataclass, field
from itertools import count

import logthis
import scheduler
import species

cret_img = pygame.image.load('cret.png')


@dataclass
class Creature:
    type: str
    creature_id: int = field(default_factory=count().__next__)
    world_coords: list[int] = field(default_factory=lambda: [0,0])
    task_queue: list = field(default_factory=lambda: [])
    active_task: list = field(default_factory=lambda: [])

    age: int = 0
    energy: int = 45


    # checks on what the individual is doing each turn
    def action(self):

        def increment_turn(self):
            print(self.creature_id, "increment_turn()")
                
            # update attributes that change each turn
            self.energy = self.energy - 1
            self.age = self.age + 1

        def trigger_tasks(self):
            print("trigger_tasks()")
            print("task queue = ", self.task_queue)
            
            def check_energy():
                if self.energy < 40:
                    
                    # remove old sleep tasks from queue
                    def remove_old_sleeps():
                        print("remove_old_sleeps()")
                    
                        if self.task_queue == []:
                            return

                        else:
                            for i in self.task_queue:
                                if i[0] == "sleep":
                                    self.task_queue.remove(i)

                    remove_old_sleeps()

                    if self.energy < 10:
                        sleep = ["sleep", 1, 0, 7]

                    elif self.energy < 30:
                        sleep = ["sleep", 2, 0, 7]

                    elif self.energy < 40:
                        sleep = ["sleep", 3, 0, 7]

                    self.task_queue.append(sleep)             
            check_energy()

            print("task queue = ", self.task_queue)
            # check_satiety()  > very similar to check_energy


        def sleep(self):
            print("sleep")

        def wander(self):
            print("wander")

        increment_turn(self)
        trigger_tasks(self)







# requires a string from bestiary_names list
def generate_creature(creature_type):
    logthis.logger.info("generate_creature")
    new_creature = Creature(creature_type)

    # add to waiting room
    new_creature_data = new_creature.__dict__
    scheduler.population[new_creature.creature_id] = new_creature_data
    scheduler.waiting_room.append(new_creature)


def get_random_creature_type():
    logthis.logger.info("get_random_creature_type")
    f = random.choice(species.bestiary_names)
    return f

