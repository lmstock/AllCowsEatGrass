from time import sleep 
from dataclasses import dataclass
import logger2  

import mongotest


@dataclass
class World:
    world_name: str
    world_health: int

    current_tick: int
    ticks_per_day: int

        
    def start_game(self):
        self.running = True

    def stop_game(self):
        self.running = False
        


    def increment_tick(self):
        tick = int(self.current_tick) + 1
        msg = "Current Tick: " + str(tick) 
        #logger2.logger.info(msg)
        sleep(1)
        self.current_tick = tick

    def update_world(self):
        logger2.logger.debug("update_world")
        update = {"current_tick" : self.current_tick}
        mongotest.update_world(self.world_name, update)



def build_world(world_name):
    logger2.logger.info("build_world")
    
    w = mongotest.get_world_data(world_name)
    
    for i in w:

        world_name = i["world_name"]
        world_health = i["world_health"]
        display_width = i["display_width"]
        display_height = i["display_height"]
        current_tick = i["current_tick"]
        ticks_per_day = i["ticks_per_day"]

    world = World(
        world_name,
        world_health,

        current_tick,
        ticks_per_day
    )

    print (world)

    return world


def setup_world(world_name):

    w = build_world(world_name)
    w.start_game()
    return w
    

world_name = "alkows"
w = setup_world(world_name)







