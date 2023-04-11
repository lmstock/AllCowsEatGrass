from pymongo import MongoClient
from bson.objectid import ObjectId
import test_logger2 as logger2
import random

c = MongoClient()
db = c['alkows']


# === REQUIRED DB CALLS === #
# def read_creature_parent(id):
#     logger2.logger.info("read_creature_parent")
#     parent_dict = db.population.find_one({"_id" : id})
#     return parent_dict

def add_creature(cret):
    logger2.logger.debug("add_creature")
    db.population.insert_one(cret)


# === TEST CASES === #
a = {
  "_id": {
    "$oid": "6429d63b6b622ae569287d91"},
  "species_type": "as",
  "img": "cret_imgs.choose_cret_img(size)",
  "size": "small",
  "sleep_dur": 430,
  "rest_gain": 0.79,
  "rest": [
    330.4,
    -0.6,
    340
  ],
  "satiety": [
    99,
    -1,
    100
  ],
  "energy": [
    100,
    100
  ],
  "hostility": [
    100,
    100
  ],
  "health": [
    100,
    100
  ],
  "speed": 81,
  "fov": 1000,
  "age": 0.00004,
  "x": 169,
  "y": 169,
  "task_q": [
    [
      "divide",
      2,
      0,
      1
    ],
    [
      "divide",
      2,
      0,
      1
    ],
    [
      "divide",
      2,
      0,
      1
    ],
    [
      "divide",
      2,
      0,
      1
    ],
    [
      "divide",
      2,
      0,
      1
    ]
  ],
  "active_task": [
    "divide",
    2,
    0,
    1
  ],
  "knowledge_base": {
    "as": [
      0.5,
      0.5,
      1
    ],
    "ruilek": [
      52,
      0,
      1
    ],
    "yauvyeab": [
      16,
      0,
      1
    ],
    "tu": [
      20,
      0,
      1
    ],
    "ip": [
      10,
      0,
      1
    ],
    "atluaw": [
      10,
      0,
      1
    ],
    "as.a": [
      10,
      0,
      1
    ],
    "ruilek.a": [
      20,
      0,
      1
    ],
    "yauvyeab.a": [
      10,
      0,
      1
    ],
    "as.a.a": [
      1,
      0,
      1
    ],
    "ruilek.a.a": [
      2,
      0,
      1
    ],
    "yauvyeab.a.a": [
      1,
      0,
      1
    ]
  },
  "is_alive": True,
  "offspring": 5
}



# creates a creature from parent through "creature division"
def divide(x):
    logger2.logger.info("divide")
    print(x)
    # parent dictionary
    p = x
    old_species_type = p['species_type']
    new_species_type = str(p['species_type'] + ".a")

    # new_creature
    nc = {
        "species_type": new_species_type,
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
        "active_task": [],
        "knowledge_base": {new_species_type: [.5, .5, 1], old_species_type: [5,5,1]},
        "is_alive": True
    }

    # roll for mutation chance


    # gen mutation - overwrite parent setting above

    def gen_mutation(nc):
        logger2.logger.info("gen_mutation")

        # mutation 5-20% more or less of some attr
        mutables = ['sleep_dur', 'rest_gain', 'rest', 'satiety', 'energy', 'hostility', 'health', 'speed', 'fov']
        direction = ['loss', 'gain']
        amount = random.randrange(5,20)

        m = random.choice(mutables)
        d = random.choice(direction)

        print(m,d,amount)

        # APPLY  MUTATION TO NEW CREATURE
        if m == 'rest':
            a = (p['rest'][2] * amount * .01)
            if d == 'loss':
                nc[m][2] = nc[m][2] - a
            else:
                nc[m][2] = nc[m][2] + a

        elif m == 'satiety':
            a = (p['satiety'][2] * amount * .01)
            if d == 'loss':
                nc[m][2] = nc[m][2] - a
            else:
                nc[m][2] = nc[m][2] + a

        elif m == 'energy':
            a = (p['energy'][1] * amount * .01)
            if d == 'loss':
                nc[m][1] = nc[m][1] - a
            else:
                nc[m][1] = nc[m][1] + a

        elif m == 'hostility':
            a = (p['hostility'][1] * amount * .01)
            if d == 'loss':
                nc[m][1] = nc[m][1] - a
            else:
                nc[m][1] = nc[m][1] + a
        
        elif m == 'health':
            a = (p['health'][1] * amount * .01)
            if d == 'loss':
                nc[m][1] = nc[m][1] - a
            else:
                nc[m][1] = nc[m][1] + a

        elif m == 'speed':
            a = (p['speed'] * amount * .01)
            if d == 'loss':
                nc[m] = nc[m] - a
            else:
                nc[m] = nc[m] + a

        elif m == 'fov':
            a = (p['fov'] * amount * .01)
            if d == 'loss':
                nc[m] = nc[m] - a
            else:
                nc[m] = nc[m] + a

        elif m == 'sleep_dur':
            a = (p['sleep_dur'] * amount * .01)
            if d == 'loss':
                nc[m] = nc[m] - a
            else:
                nc[m] = nc[m] + a
        
        elif m == 'rest_gain':
            a = (p['rest_gain'] * amount * .01)
            if d == 'loss':
                nc[m] = nc[m] - a
            else:
                nc[m] = nc[m] + a

        return nc
    
    new_creature = gen_mutation(nc)
    
    # add_creature(new_creature)  # dont need to add to db for testing

    # count offspring
    if 'offspring' not in x: 
        x['offspring'] = 1

    else:
        x['offspring'] = x['offspring'] + 1

    print(new_creature)
    return x

divide(a)