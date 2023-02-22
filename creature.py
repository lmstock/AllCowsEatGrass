import random
import pygame

from dataclasses import dataclass, field
from itertools import count


import logthis
import scheduler
import species
import game_conf
import game_imgs.imgs as imgs

from game_conf import Game_config
from creature_actions import sleep, eat, wander, nothing, play, observe


# being mindful of class size
# https://softwareengineering.stackexchange.com/questions/11846/how-large-is-ok-for-a-class

# moving Creature methods outside of class to keep size down.


@dataclass
class Creature:
    type: str
    img: str 
    size: str

    # sleep attributes
    rest: list # (current rest, max rest)
    sleep_dur: float
    rest_gain: float
    base_fatigue: float
    
    satiety: list   # (current satiety, loss per turn, max satiety)
    energy: list   # (current, max)   

    hostility: list  # (current hostility, max hostility)  # to help define behavior toward other creatures
    health: list  # (current, max) # sickness introduced by prolonged hunger or fatigue or injury
    speed: list  # movement attributes
    fov: int # field of "vision"
    age: float

    creature_id: int = field(default_factory=count().__next__)
    world_coords: list[int] = field(default_factory=lambda: [250,250])
    task_q: list = field(default_factory=lambda: [])
    active_task: list = field(default_factory=lambda: ["wander", 3, 0, 7])
    knowledge_base: dict = field(default_factory=lambda:{})
    

    # checks on what the individual is doing each turn
    def action(self):

        # UPDATE ATTRIBUTES THAT CHANGE EACH TURN
        def increment_turn(self):
            logthis.logger.debug("increment_turn")
            print(self.__dict__)
            if self.active_task == []:
                pass
            
            else:
                if self.active_task[0] != "sleep":
                    self.rest[0] = round(self.rest[0] + self.base_fatigue, 2)

                if self.active_task[0] != "eat":
                    self.satiety[0] = round(self.satiety[0] - self.satiety[1], 2)
                
                self.age = round(self.age + .0000025, 7)


        def trigger_tasks(self):
            logthis.logger.debug("trigger_tasks")

            # SLEEP TRIGGER
            def check_current_rest():

                if self.active_task == []:
                    pass

                else:
                    if self.active_task == "sleep":
                        pass

                    else:
                        # less than 40% 
                        if self.rest[0] < self.rest[1] * .4:
                        
                            # remove old sleep tasks from task_q if present
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

            # EAT TRIGGER
            def check_current_satiety():

                if self.active_task == []:
                    pass
                
                else:
                    if self.active_task[0] == "eat":
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

            # FIELD OF VIEW CHECK
            def check_fov():
                print("\n")
                logthis.logger.info("check_fov")

                # chance to check fov
                #if self.salt[0] < 5:

                # locals list
                local_crets = []

                # get fov   
                x_range = self.world_coords[0] - 1000, self.world_coords[0] + 1000
                y_range = self.world_coords[1] - 1000, self.world_coords[1] + 1000
                fov = (x_range, y_range)

                # check for local_crets
                for i in scheduler.population.items():

                    # is creature in population x coord in x range of active entity?
                    if i[1]['world_coords'][0] in range(fov[0][0], fov[0][1]):
                        msg = (i[1]['creature_id'], " - ", i[1]['world_coords'][0], " is in range ", fov[0][0], " - ", fov[0][1])
                        logthis.logger.debug(msg)

                        # is creature in population y coord in y range of active entity?
                        if i[1]['world_coords'][1] in range(fov[1][0], fov[1][1]):
                            msg = i[1]['creature_id'], " - ", i[1]['world_coords'][1], "is in range ", fov[1][0], " - ", fov[1][1]
                            logthis.logger.debug(msg)

                            local_crets.append(i[1]['creature_id'])

                        else: msg = i[1]['creature_id'], " - ", i[1]['world_coords'][1], "NOT in range ", fov[1][0], " - ", fov[1][1]
                        logthis.logger.debug(msg)

                    else: msg = i[1]['creature_id'], " - ", i[1]['world_coords'][0], " NOT in range ", fov[0][0], " - ", fov[0][1]
                    logthis.logger.debug(msg)

                print(self.creature_id ,":  LOCALS: ", local_crets)
                return local_crets
            local_crets = check_fov() # returns a list of creatures in fov by creature_id

            # check knowledge base - returns a creature from fov
            def check_kb(local_crets):
                print("\n")
                logthis.logger.info("check_kb")

                if local_crets == False:
                    pass
                else:
                    x = random.choice(local_crets)
                    return x

            x = check_kb(local_crets)
            #self.active_task = "observe"



        # checks active task for empty or completion
        def check_active_task(self):
            logthis.logger.debug("check_active_task")
            
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
                    else: 
                        if game_conf.g.current_tick % 2 == 0:
                            x = ["wander", 3, 0, duration]
                        else: x = ["play", 3, 0, duration]
                    try:
                        self.task_q.remove(x)
                    except Exception as e:
                        pass

                    return x

                self.active_task = get_new_task(self)

            elif self.active_task[2] == self.active_task[3]:
                self.active_task = []
                       

        def increment_active_task(self):
            logthis.logger.debug("increment_active_task")

            #if active_task is empty, pass
            if self.active_task == []:
                pass

            else:

                if self.active_task[0] == "sleep":
                    #sleep(self)
                    sleep(self)

                elif self.active_task[0] == "wander":
                    wander(self)

                elif self.active_task[0] == "nothing":
                    nothing(self)

                elif self.active_task[0] == "eat":
                    eat(self)
                
                elif self.active_task[0] == "play":
                    play(self)

                elif self.active_task[0] == "observe":
                    observe(self)







        # OTHER
        def update_viewport(self):
            logthis.logger.debug("update_viewport")
            game_conf.g.game_display.blit(self.img, self.world_coords)
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
        creature_type,
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
        knowledge_base={creature_type: [.5, .5, 1]}  # type: [observation count, investigation count, reaction code]  ## .5 knowledge indicates own species
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



