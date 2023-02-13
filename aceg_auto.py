import pygame

import species
import flora_species
import creature
import flora
import scheduler
import game_setup
import logthis
import core
import to_file
import reporter

from dataclasses import dataclass, field
from time import sleep
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    K_i,
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

# generate species and creatures to work with

for i in range(1,5):
    flora_species.generate_flora_species()

for i in range(1,5):
    flora.generate_flora(flora.get_random_flora_type())

for i in range(1,4):
    species.generate_species()

for i in range(1,10):
    creature.generate_creature(creature.get_random_creature_type())




def main(running):
    logthis.logger.debug("main")

    while running == True:
        game_setup.clock.tick(.5)

        core.turn()
        scheduler.scheduler_run()
        pygame.display.update()
        reporter.write_html()

        for event in pygame.event.get():


            
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    logthis.logger.debug("escape key")
                    running = False
                    return

                if event.key == K_i:
                    logthis.logger.debug("i = get_game_info")
                    to_file.get_game_info()

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

            

main(game_setup.running)

