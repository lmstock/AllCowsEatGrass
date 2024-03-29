import random

import bartokmongo
import names
import logger2
import core





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
    "seeds",
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

'''species is a template of a creature'''

def generate_flora_species():
    logger2.logger.info("generate_flora_species")

    flora_species_type = names.generate_name()
    size = random.choice(plant_size_pool)
    flora_type = random.choice(type_pool)

    # will be generated
    energy = 100

    # will be generated (spread distance 0-10, chance for spread 10 - 100%, counter, cooldown)
    spread_distance = core.roll(1,10)
    spread_chance = core.roll(1,50)
    cooldown = core.roll(10,100)
    growth_data = (spread_distance, spread_chance, 0, cooldown)
    
    # herbarium is collection in mongo
    new_flora_species = {

        "flora_species_type": flora_species_type,
        "size": size,
        "flora_type": flora_type,
        "energy" : energy,
        "growth_data" : growth_data
        }

    # add to herbarium
    bartokmongo.add_flora_species(new_flora_species)