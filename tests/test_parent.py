
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import test_logger2 as logger2



c = MongoClient()
db = c['alkows']

my_id = "6429d63b6b622ae569287d91"



def read_creature_parent(id):
    logger2.logger.info("read_creature_parent")
    parent_dict = db.population.find_one({"_id" : ObjectId(my_id)}) #remove ObjectId part for main
    return parent_dict

# creates a creature from parent through "creature division"
def divide_creature(parent_id):
    logger2.logger.info("divide_creature")

    # parent dictionary
    p = read_creature_parent(parent_id)
    print(p)

    new_creature = {
        "species_type": str(p["species_type"]+ ".a"),
        "size": p["size"],
        
        # mutables
        "sleep_dur": p["sleep_dur"],  # set these [0]s to max on new creature creation
        "rest_gain": p["rest_gain"],
        "rest": p["rest"],  
        "satiety": p["satiety"],
        "energy": p["energy"],
        "hostility": p["hostility"],  
        "health": p["health"],
        "speed": p["speed"],
        "fov": p["fov"],

        # non mutable
        "age": 0,
        "x": p['x'],
        "y": p['y'],
        "task_q": [],
        "active_task": []
    }

    # roll for mutation chance



    # gen mutation - overwrite parent setting above
    # mutation 5-20% more or less
    mutables = ['sleep_dur', 'rest_gain', 'rest', 'satiety', 'energy', 'hostility', 'health', 'speed', 'fov']
    direction = ['loss', 'gain']
    amount = random.randrange(5,20)
    m = random.choice(mutables)
    d = random.choice(direction)
    print(m, d, amount)
    
    # APPLY THIS MUTATION TO NEW CREATURE




    print(new_creature)

x = divide_creature(my_id)
