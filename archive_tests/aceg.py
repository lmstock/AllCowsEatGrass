import pygame
import pprint

import species
import creature
import scheduler
import game_conf
import logthis
import core

from dataclasses import dataclass, field
from time import sleep
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    K_b,
    K_p,
    K_a,
    K_w,
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




def main(turn, running):
    logthis.logger.debug("main")

    while running == True:
        event = pygame.event.wait()
            
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                logthis.logger.debug("escape key")
                running = False
                return

            if event.key == K_DOWN:
                logthis.logger.debug("down")
                core.turn()

            if event.key == K_b:
                logthis.logger.debug("b = bestiary")
                pprint.pprint(species.bestiary)

            if event.key == K_p:
                logthis.logger.debug("p = population")
                pprint.pprint(scheduler.population)

            if event.key == K_a:
                logthis.logger.debug("a = actors list")
                pprint.pprint(scheduler.actors)

            if event.key == K_w:
                logthis.logger.debug("w = waiting room")
                pprint.pprint(scheduler.waiting_room )

            # a skip turn
            if event.key == K_SPACE:
                logthis.logger.debug("spacebar")

                core.turn()
                scheduler.scheduler_run()
                pygame.display.update()

            
             
            
            

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

            

main(game_conf.turn, game_conf.running)

