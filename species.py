import random

from dataclasses import dataclass, field
from itertools import count

import mongotest
import names
import logthis
import game_conf
import game_imgs.imgs as imgs
import core

# vague idea of sort of random metrics that belong to species, a sort of unit of heredity, a gene.
# They can be tied to attributes somehow and have the ability to change so that the gene and its 
# consequence can descend from the ancestor. (ex.  A123=100, rT49=73)

'''species class creates species instances,
   species instances are added to dict bestiary,
   creatures are built from those templates'''

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

    # basic
    name: str 
    head: str
    size: str
    body_type: str
    img: str

    # sleep info
    rest: list  # fully rested
    sleep_duration: float
    rest_gain: float  # rest gained per turn sleeping
    base_fatigue: float  # rest lost per turn awake
    
    # gen health
    satiety: list # (current satiety, loss per turn, max satiety)
    energy: list # (current, max)  
    hostility: list
    health: list

    # physical
    speed: list
    fov: int = 1000
    species_id: int = field(default_factory=count().__next__)






def generate_species():
    logthis.logger.info("generate_species")

    name = names.generate_name()
    head = random.choice(head_pool)
    size = random.choice(body_size_pool)
    body_type = random.choice(body_type_pool)

    # select image
    species_img = imgs.choose_img(size)
    

    def gen_sleep_habits():
        logthis.logger.debug("gen_sleep_habits")
        #sleep_roll    10d9 for % sleep vs awake in a day
        
        sleep_roll = core.roll(10,9)

        sleep_duration = round((sleep_roll/100) * game_conf.g.ticks_per_day, 2)
        awake_duration = round(1000 - sleep_duration, 2)

        fully_rested = core.roll(5,15) * 10   # 5d20 * 10 for full energy (5, 500)
        rest_gain = round(fully_rested/sleep_duration, 2)
        base_fatigue = round((fully_rested/awake_duration) * -1, 2)
        return sleep_duration, fully_rested, rest_gain, base_fatigue


    s = gen_sleep_habits()

    rest = [s[1], s[1]]
    sleep_duration = s[0]
    rest_gain = s[2]
    base_fatigue = s[3]

    # use this to specify sleep metrics
    # rest = [100, 280]
    # sleep_duration = 430
    # rest_gain = .65
    # base_fatigue = -10

    satiety = [100, -1, 100]  # (current satiety, loss per turn, max satiety)
    hostility = [100, 100]
    health = [100, 100]
    energy = [100, 100]

    speed_base = core.roll(15,10)

    # this all doesnt need to be in db, just base. calculate the rest as needed
    speed = [round(speed_base*.5,2),speed_base,speed_base*3,speed_base*6]
    fov = 1000
    species_id: int = field(default_factory=count().__next__)



    # generate new species object
    new_species = Species(
        
        name,
        head, 
        size,
        body_type, 
        species_img,

        rest,
        sleep_duration,
        rest_gain,
        base_fatigue,
        
        satiety,
        energy,
        hostility,
        health,
        
        speed,
        fov,
        species_id
        )


    # add species data to bestiary
    # remove this if we keep db
    species_data = new_species.__dict__
    bestiary[name] = species_data
    print(species_data)

    # add name to bestiary list
    bestiary_names.append(new_species.name)
    
    # write a function for this
    # this is a document
    # # add to db
    new_species.species_id = {
        "species_id": str(new_species.species_id),
        "name": name,
        "head": head,
        "size": size,
        "body_type": body_type,
        "species_img": str(species_img),
        "rest": rest,
        "sleep_duration": sleep_duration,
        "rest_gain": rest_gain,
        "base_fatigue": base_fatigue,
        "satiety": satiety,
        "hostility": hostility,
        "health": health,
        "energy": energy,
        "speed": speed,
        "fov": fov

    }


    mongotest.add_species(new_species.species_id)





        

