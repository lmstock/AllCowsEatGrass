import pygame
import random

from dataclasses import dataclass, field
from itertools import count


from core import *
from game_setup import game_display
from scheduler import *

fauna_img = pygame.image.load('cret.png')


@dataclass
class Fauna():

    name: str = "fauna"
    id_number: int = field(default_factory=count().__next__)
    world_coords: list[int] = field(default_factory=lambda: [0,0])
    display_coords: list[int] = field(default_factory=lambda: [0,0])
    task_queue: list = field(default_factory=lambda: [])
    active_task: list = field(default_factory=lambda: [])

    # Vitals
    age: int = 100
    energy: int = 42
    # satiety: int = 100
    # health: int = 100
    # hostility: int = 100

    
    

    # checks on what individual is doing each turn
    def action(self):
        print(self, " action()")
        

        def increment_turn(self):
            print("increment_turn()")
                
            # attrs that change each turn
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

            # check_satiety()  > very similar to check_energy


        increment_turn(self)
        trigger_tasks(self)





# define coords at spawn
def spawn_fauna(x, y):
    print("spawn_fauna")

    world_coords = [x,y]
    
    # spawn fauna
    fauna = Fauna(world_coords=world_coords)


    # set display 
    fauna.display_coords = calculate_display_coords([x,y])

    
    # add to waiting room to be inserted into actors
    waiting_room.insert(0,fauna)



    

