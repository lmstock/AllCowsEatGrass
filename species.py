import random
import pprint

from dataclasses import dataclass, field
from itertools import count

import names
import logthis
import game_imgs.imgs as imgs
import core




# vague idea of sort of random metrics that belong to species, a sort of unit of heredity, a gene.
# They can be tied to attributes somehow and have the ability to change so that the gene and its 
# consequence can descend from the ancestor. (ex.  A123=100, rT49=73)


bestiary = {}
bestiary_names = []
#actors = {}


head_pool = [
    "large",
    "long",
    "sagging",
    "small",
    "pointy",
    "angular",
    "medium sized",
    "drooping",
    "bald",
    "hairy",
    "round",
    "oval",
    "square",
    "segmented"
    
]

body_size_pool = [
    "tiny",
    "small",
    "medium",
    "large",
    "very_large",
    "mega"
]

body_type_pool = [
    "segmented with a head, thorax, and abdomen",
    "consisting of a head, torso, and limbs",
    "soft tissued",
    "soft tissued with a shell"
]


@dataclass
class Species:

    name: str 
    img: str
    img_bg: str
    head: str
    size: str
    body_type: str
    
    # sleep info
    sleep_duration: float
    max_rest: float  # fully rested
    rest_gain: float  # rest gained per turn sleeping
    base_fatigue: float  # rest lost per turn awake

    satiety: tuple
    hostility: tuple
    health: tuple
    energy: tuple

    # movement info
    speed: float = 1

    species_id: int = field(default_factory=count().__next__)
    

def generate_species():
    logthis.logger.info("generate_species")

    name = names.generate_name()
    head = random.choice(head_pool)
    size = random.choice(body_size_pool)
    body_type = random.choice(body_type_pool)

    # select image
    species_images = imgs.choose_img(size)
    species_img = species_images[0]
    species_img_bg = species_images[1]

    s = gen_sleep_habits()

    sleep_duration = s[0]
    max_rest = s[1]
    rest_gain = s[2]
    base_fatigue = s[3]

    satiety_max = 100
    hostility_max = 100
    health_max = 100
    energy_max = 100

    speed = core.roll(15,10)



    # generate new species object
    new_species = Species(
        name,
        species_img,
        species_img_bg,
        head, 
        size,
        body_type, 
        sleep_duration,

        max_rest,
        rest_gain,
        base_fatigue,
        
        satiety_max,
        hostility_max,
        health_max,
        energy_max,
        speed)

    # add to bestiary
    species_data = new_species.__dict__
    print(species_data)
    bestiary[name] = species_data

    # add name to bestiary list
    bestiary_names.append(new_species.name)
    
    # write a function for this
    # # add to db
    # new_species.species_id = {
    #     "name": name,
    #     "head": head,
    #     "size": size,
    #     "body_type": body_type,
    #     "sleep_duration": sleep_duration,
    #     "fully_rested": fully_rested,
    #     "rest_gain": rest_gain,
    #     "base_fatigue": base_fatigue,
    #     "speed": speed
    # } 

    #mongotest.add_species(new_species.species_id)

def gen_sleep_habits():
    logthis.logger.info("gen_sleep_habits")

    ticks_in_day = 1000

    sleep_roll = core.roll(10,9)  # 10d9 for % sleep vs awake in a day
    
    sleep_duration = round((sleep_roll/100) * ticks_in_day, 2)
    awake_duration = round(1000 - sleep_duration, 2)

    fully_rested = core.roll(5,15) * 10   # 5d20 * 10 for full energy (5, 500)
    rest_gain = round(fully_rested/sleep_duration, 2)
    base_fatigue = round((fully_rested/awake_duration) * -1, 2)

    return sleep_duration, fully_rested, rest_gain, base_fatigue

    

