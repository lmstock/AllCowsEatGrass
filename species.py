import random
import pprint

from dataclasses import dataclass, field
from itertools import count

import names
import logthis
import game_imgs.imgs as imgs
from core import roll
from world import turns_in_day_night_cycle

bestiary = {}
bestiary_names = []
actors = {}


head = [
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

body_size = [
    "tiny",
    "small",
    "medium",
    "large",
    "very_large",
    "mega"
]

body_type = [
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
    
    sleep_duration: float
    awake_duration: float
    full_energy: float  # fully rested
    rest_gain: float  # energy gained per turn sleeping
    base_fatigue: float  # energy lost per turn awake

    species_id: int = field(default_factory=count().__next__)
    

def generate_species():
    logthis.logger.info("generate_species")

    name = names.generate_name()
    x_head = random.choice(head)
    x_size = random.choice(body_size)
    x_body_type = random.choice(body_type)

    # select image
    species_images = imgs.choose_img(x_size)
    species_img = species_images[0]
    species_img_bg = species_images[1]

    s = gen_sleep_habits()

    sleep_duration = s[0]
    awake_duration = s[1]
    fully_rested = s[2]
    rest_gain = s[3]
    base_fatigue = s[4]


    # generate new species object
    new_species = Species(
        name,
        species_img,
        species_img_bg,
        x_head, 
        x_size,
        x_body_type, 
        sleep_duration,
        awake_duration,
        fully_rested,
        rest_gain,
        base_fatigue)

    # add to bestiary
    species_data = new_species.__dict__
    bestiary[name] = species_data

    # add name to bestiary list
    bestiary_names.append(new_species.name)
    

def gen_sleep_habits():
    logthis.logger.info("gen_sleep_habits")

    sleep_roll = roll(10,9)  # 10d9 for % sleep vs awake in a day
    
    sleep_duration = round((sleep_roll/100) * turns_in_day_night_cycle, 2)
    awake_duration = round(100 - sleep_duration, 2)

    fully_rested = roll(5,15) * 10   # 5d20 * 10 for full energy (5, 500)
    rest_gain = round(fully_rested/sleep_duration, 2)
    base_fatigue = round((fully_rested/awake_duration) * -1, 2)

    return sleep_duration, awake_duration, fully_rested, rest_gain, base_fatigue

    











# there is a lot of fleshing out to do from here now.

# vague idea of sort of random metrics that belong to species, a sort of unit of heredity, a gene.
# They can be tied to attributes somehow and have the ability to change so that the gene and its 
# consequence can descend from the ancestor. (ex.  A123=100, rT49=73)