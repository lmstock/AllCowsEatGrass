import random
import game_conf
import bartokmongo
import names
import logger2

import core
import species_pools
from beast_builder import random_creature_gen

# vague idea of sort of random metrics that belong to species, a sort of unit of heredity, a gene.
# They can be tied to attributes somehow and have the ability to change so that the gene and its 
# consequence can descend from the ancestor. (ex.  A123=100, rT49=73)

'''
Species is a template of a creature

Creatures are only created from species on special occasions. otherwise it is expected that they will reproduce.
Generate_creature_species is only run to populate bestiary for creation of vivarium (or, in the future, special events)

Random species are generated here.
'''

def generate_creature_species():
    logger2.logger.info("generate_species")

    species_type = names.generate_name()

    new_additions = random_creature_gen()
    

    def gen_sleep_habits():
        logger2.logger.debug("gen_sleep_habits")
        #sleep_roll    10d9 for % sleep vs awake in a day

        tpd = int(game_conf.w.ticks_per_day)
        
        sleep_roll = core.roll(10,9)    # how long a creature sleeps in ticks
        sleep_duration = round((sleep_roll/100) * tpd, 2)
        awake_duration = round(tpd - sleep_duration, 2)

        fully_rested = core.roll(5,15) * 10   # 5d20 * 10 for full energy (5, 500)
        rest_gain =  round(fully_rested/sleep_duration, 2)
        base_fatigue = round((fully_rested/awake_duration) * -1, 2)
        return sleep_duration, fully_rested, rest_gain, base_fatigue

    s = gen_sleep_habits()



    rest = [s[1], s[3], s[1]]  # (current rest, base fatique, max rest)
    sleep_duration = s[0]
    rest_gain = s[2]

    sat_loss = core.roll(1,5) * -1
    satiety = [100, sat_loss, 100]  # (current satiety, loss per turn, max satiety)
    
    """ TROPHIC LEVELS (expand on this)
    
    0 - decomposers - eat dead things
    1 - primary consumers - eats only flora
    2 - secondary comsumers - eats primary consumers
    3 - tertiary consumers - eats secondary, primary
    4 - apex predator - eats anyone, has no predators except other apex predators 

    * while the existence of a megafauna that is a decomposer is unlikely
    * we will let them play out, they will probably extinct quickly if they dont
    * evolve to eat something thats available
    """
    
    trophic_level = random.randint(0,4)
    hostility = [0,core.roll(3,33)]
    health = [100, 100]
    energy = [100, 100]

    speed = core.roll(15,10)
    fov = 1000
    repr = core.roll(10, 50)

    
    # bestiary is collection in mongo
    new_creature_species = {
        
        "species_type": species_type,

        "rest": rest,
        "sleep_duration": sleep_duration,
        "rest_gain": rest_gain,

        "satiety": satiety,
        "trophic_level": trophic_level,
        "hostility": hostility,
        "health": health,
        "energy": energy,

        "speed": speed,
        "fov": fov,
        'mutation_count': 0,
        "repr_cooldown": [0, repr]
        }
    
    for k,v in new_additions.items():
        new_creature_species[k] = v

    print(new_creature_species)

    # add to bestiary
    bartokmongo.add_creature_species(new_creature_species)







        

