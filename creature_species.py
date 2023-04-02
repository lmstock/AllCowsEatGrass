import random

import mongotest
import names
import logger2
import game_conf
import core
import species_pools

# vague idea of sort of random metrics that belong to species, a sort of unit of heredity, a gene.
# They can be tied to attributes somehow and have the ability to change so that the gene and its 
# consequence can descend from the ancestor. (ex.  A123=100, rT49=73)

'''species is a template of a creature'''

def generate_creature_species():
    logger2.logger.info("generate_species")

    species_type = names.generate_name()
    head = random.choice(species_pools.head_pool)
    size = random.choice(species_pools.body_size_pool)
    body_type = random.choice(species_pools.body_type_pool)

    # select image
    species_img = "cret_imgs.choose_cret_img(size)"
    

    def gen_sleep_habits():
        logger2.logger.debug("gen_sleep_habits")
        #sleep_roll    10d9 for % sleep vs awake in a day
        
        sleep_roll = core.roll(10,9)
        sleep_duration = round((sleep_roll/100) * int(game_conf.w.ticks_per_day), 2)
        awake_duration = round(1000 - sleep_duration, 2)

        fully_rested = core.roll(5,15) * 10   # 5d20 * 10 for full energy (5, 500)
        rest_gain = round(fully_rested/sleep_duration, 2)
        base_fatigue = round((fully_rested/awake_duration) * -1, 2)
        return sleep_duration, fully_rested, rest_gain, base_fatigue


    s = gen_sleep_habits()

    rest = [s[1], s[3], s[1]]  # (current rest, base fatique, max rest)
    sleep_duration = s[0]
    rest_gain = s[2]


    satiety = [100, -1, 100]  # (current satiety, loss per turn, max satiety)
    hostility = [100, 100]
    health = [100, 100]
    energy = [100, 100]

    speed = core.roll(15,10)
    fov = 1000

    
    # bestiary is collection in mongo
    new_creature_species = {
        
        "species_type": species_type,
        "head": head,
        "size": size,
        "body_type": body_type,

        # this need to be str?
        "species_img": str(species_img),

        "rest": rest,
        "sleep_duration": sleep_duration,
        "rest_gain": rest_gain,

        "satiety": satiety,
        "hostility": hostility,
        "health": health,
        "energy": energy,

        "speed": speed,
        "fov": fov
        }

    # add to bestiary
    mongotest.add_creature_species(new_creature_species)





        

