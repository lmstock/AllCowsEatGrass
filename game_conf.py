from dataclasses import dataclass
import logger2  
import pygame
import mongotest


@dataclass
class World:
    world_name: str
    world_health: int
    display_width: int
    display_height: int
    current_tick: int
    ticks_per_day: int

    bg_color: tuple = (255,255,255)

    clock=pygame.time.Clock()
    clock.tick(.5)
    game_display = pygame.display.set_mode((1200, 600))


    def get_bg_color(self):

        def get_hund(m):
            n = str(m)

            if len(n) <= 2:
                h = 0
            else:
                h = n[-3]
            return h
        
        n = int(get_hund(self.current_tick))

        def wtf(n):

            if n == 0:  return (25,60,90)
            elif n == 1 or n == 9: return (70,94,104)
            elif n == 2 or n == 8: return (115,128,118)
            elif n == 3 or n == 7: return (160,162,132)
            elif n == 4 or n == 6: return (205,196,146)
            elif n == 5: return (250,230,160)
                
        return wtf(n)
        
    def start_game(self):
        self.running = True
        
        
        pygame.display.set_caption(world_name)
        pygame.init()

    def increment_tick(self):
        tick = int(self.current_tick) + 1
        msg = "Current Tick: " + str(tick)
        logger2.logger.info(msg)
        self.clock.tick(.5)
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
        display_width,
        display_height,
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







