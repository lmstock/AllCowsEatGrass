import pygame

import game_conf
import scheduler
import logger2
import mongotest


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

