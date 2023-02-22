import pygame

import game_conf
import creature
import flora
import scheduler
import logthis
import to_file
import reporter
import species
import flora_species
import test_cret


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


"""
phase1 -   
    movement
    sleep
    viewport

    flora
    eating
"""



def generate_random_populus():
    for i in range(1,5):
        flora_species.generate_flora_species()

    for i in range(1,25):
        flora.generate_flora(flora.get_random_flora_type())

    for i in range(1,4):
        species.generate_species()

    for i in range(1,25):
        creature.generate_creature(creature.get_random_creature_type())

generate_random_populus()
#test_cret.gen_test_crets()


# game 
def main (running):
    logthis.logger.debug("main")

    while game_conf.g.running == True:

        # Game Loop
        game_conf.g.increment_tick()
        game_conf.g.game_display.fill(game_conf.g.get_bg_color()) 
        scheduler.scheduler_run()
        pygame.display.update()
        reporter.write_html()

        # Event Handler
        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    logthis.logger.debug("escape key")
                    running = False
                    return
                
                if event.key == K_p:
                    logthis.logger.info("pause")

                if event.key == K_i:
                    logthis.logger.debug("i = get_game_info")
                    to_file.get_game_info()

            # close window button
            elif event.type == QUIT:
                running = False

main(game_conf.g.running)
