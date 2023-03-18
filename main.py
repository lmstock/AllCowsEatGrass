import pygame

import game_conf
import scheduler
import logger2
import mongotest
import creature
import creature_species
import flora
import flora_species


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    K_i,
    K_p,
    KEYDOWN, 
    QUIT, 
)

# for i in range(1,5):
#     creature_species.generate_creature_species()

# GENERATE FLORA SPECIES
# for i in range(1,5):
#     flora_species.generate_flora_species()

#GENERATE FLORA POPULATION
# for i in range(2):
#     flora.generate_random_flora()

# ## GENERATE CREATURE POPULATION ##
# for i in range(1,15):
#     creature.generate_creature(creature.get_random_creature_type())

## run model 
def main (running):
    logger2.logger.debug("main")

    while game_conf.w.running == True:

        # Game Loop
        game_conf.w.increment_tick()
        game_conf.w.game_display.fill(game_conf.w.get_bg_color()) 
        scheduler.scheduler_run()
        pygame.display.update()
        mongotest.manage_hist()
        game_conf.w.update_world()
        

        # Event Handler
        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    logger2.logger.debug("escape key")
                    running = False
                    return
                
                if event.key == K_p:
                    logger2.logger.info("pause")

                if event.key == K_i:
                    logger2.logger.debug("i = get_game_info")


            # close window button
            elif event.type == QUIT:
                running = False


main(game_conf.w.running)

