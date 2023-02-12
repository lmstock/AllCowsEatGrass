import species
import scheduler
import game_setup
import flora_species

import pprint

# write game info to file
    # game turn
    # bestiary
    # population


def get_game_info():
    with open('aceg_logs\\gamefile.txt', 'w') as game_info:

        turn = str(game_setup.turn)
        game_info.write(turn)
        game_info.write('\n\n')

        b = pprint.pformat(species.bestiary)
        game_info.write(str(b))
        game_info.write('\n\n')

        p = pprint.pformat(scheduler.population)
        game_info.write(str(p))

        p = pprint.pformat(flora_species.herbarium)
        game_info.write(str(p))




