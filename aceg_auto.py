import pygame
import pprint

import species
import creature
import scheduler
import game_setup
import logthis
import core
import to_file

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

# make display bigger and print text?

"""
phase1 -   
    movement
    sleep
    viewport

phase2 -  
    flora
    eating
"""

# generate species and creatures to work with

for i in range(1,7):
    species.generate_species()

for i in range(1,5):
    creature.generate_creature(creature.get_random_creature_type())




def main(running):
    logthis.logger.debug("main")

    while running == True:
        game_setup.clock.tick(.5)

        core.turn()
        scheduler.scheduler_run()
        pygame.display.update()

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
