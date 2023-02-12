import random
import pprint

from dataclasses import dataclass, field
from itertools import count

import names
import logthis
import scheduler
import game_imgs.imgs as imgs
import core
import world
import game_imgs.flora.plant_imgs

herbarium = {}
herbarium_names = []

# fungus
type_pool = [
    "algea", # colonies
    "bryo",  # non vascular land plants
    "pterido", # vascular and disperses spores
    "spermatophytes" # seed bearing plants
]

plant_size_pool = [
    "tiny",
    "small",
    "medium",
    "large",
    "very_large",
    "mega"
]

body_parts = [
    "leaves",
    "seeds"
    "thallus",
    "roots",
    "stem",
    "fruit",
    "flower",
    "bark"
]

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "brown",
    "black"

]


@dataclass
class FloraSpecies:

    name: str
    img: str
    #img_bg: str
    type: str
    size: str
    energy: float
    growth_data: list # growth speed, max growth, growth stages

    species_id: int = field(default_factory=count().__next__)


def generate_flora_species():
    logthis.logger.info("generate_flora_species")

    name = names.generate_name()
    type = random.choice(type_pool)
    size = random.choice(plant_size_pool)
    img = game_imgs.flora.plant_imgs.plant1

    # generate new flora species object
    new_flora_species = FloraSpecies(
        name,
        img,
        type,
        size,
        energy = 100,
        growth_data = [1,1,1])


    # add to herbarium
    flora_species_data = new_flora_species.__dict__
    herbarium[name] = flora_species_data

    # add to herbarium names list
    herbarium_names.append(new_flora_species.name)
    print(herbarium)