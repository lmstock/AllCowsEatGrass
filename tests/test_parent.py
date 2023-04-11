
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
        "sleep_dur": p["sleep_dur"],  # creature division brings parent currents to child
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

    # APPLY  MUTATION TO NEW CREATURE
    if m == 'rest':
        a = (p['rest'][2] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a

    elif m == 'satiety':
        a = (p['satiety'][2] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a

    elif m == 'energy':
        a = (p['energy'][1] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a

    elif m == 'satiety':
        a = (p['satiety'][2] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a
    
    elif m == 'health':
        a = (p['health'][1] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a

    elif m == 'speed':
        a = (p['speed'] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a

    elif m == 'fov':
        a = (p['fov'] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a

    elif m == 'sleep_dur':
        a = (p['sleep_dur'] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a
    
    elif m == 'rest_gain':
        a = (p['rest_gain'] * amount * .01)
        if d == 'loss':
            new_creature[m][2] = new_creature[m][2] - a
        else:
            new_creature[m][2] = new_creature[m][2] + a
    
    print("a: ", a)


    print(new_creature)

x = divide_creature(my_id)
