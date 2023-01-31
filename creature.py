import random

from dataclasses import dataclass, field
from itertools import count


import logthis
import scheduler
import species

@dataclass
class Creature:
    type: str
    creature_id: int = field(default_factory=count().__next__)

# requires a string from bestiary_names list
def generate_creature(creature_type):
    logthis.logger.info("generate_creature")
    new_creature = Creature(creature_type)

    # add to actors
    new_creature_data = new_creature.__dict__
    scheduler.population[new_creature.creature_id] = new_creature_data


def get_random_creature_type():
    logthis.logger.info("get_random_creature_type")
    f = random.choice(species.bestiary_names)
    return f

