import random

import mongotest
import names
import logger2

import game_imgs.flor_imgs



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
    
    # select image
    flora_img = game_imgs.flor_imgs.choose_flor_img(size)

    # will be generated
    energy = 100

    # will be generated
    growth_data = [1,1,1]
    
    # herbarium is collection in mongo
    new_flora_species = {

        "flora_species_type": flora_species_type,
        "size": size,
        "flora_type": flora_type,
        "energy" : energy,
        "growth_data" : growth_data,
        "img": flora_img
        }

    # add to herbarium
    mongotest.add_flora_species(new_flora_species)