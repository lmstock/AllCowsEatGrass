import random
import pprint

from dataclasses import dataclass, field
from itertools import count

import names
import logthis
import imgs


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
    "very large",
    "mega large"
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
    head: str
    size: str
    body_type: str
    energy: int
    species_id: int = field(default_factory=count().__next__)
    

def generate_species():
    logthis.logger.info("generate_species")

    name = names.generate_name()
    x_img = str
    x_head = random.choice(head)
    x_size = random.choice(body_size)
    x_body_type = random.choice(body_type)
    x_energy = 100 # modify based on x_size

    # select image
    species_img = random.choice(imgs.cret_pool)
    imgs.cret_pool.remove(species_img)

    # generate new species object
    new_species = Species(name, species_img, x_head, x_size, x_body_type, 100)

    # add to bestiary
    species_data = new_species.__dict__
    bestiary[name] = species_data

    # add name to bestiary list
    bestiary_names.append(new_species.name)

# generate_species()

# print(bestiary)









# there is a lot of fleshing out to do from here now.

# vague idea of sort of random metrics that belong to species, a sort of unit of heredity, a gene.
# They can be tied to attributes somehow and have the ability to change so that the gene and its 
# consequence can descend from the ancestor. (ex.  A123=100, rT49=73)