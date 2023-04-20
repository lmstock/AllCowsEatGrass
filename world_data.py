
# #clear old data from db
# bartokmongo.clear_db()

# for i in range(1,5):
#     creature_species.generate_creature_species()

# for i in range(1,5):
#     flora_species.generate_flora_species()

# for i in range(1,5):
#     flora.generate_flora(flora.get_random_flora_type())

# for i in range(1,5):
#     creature.generate_creature(creature.get_random_creature_type())


# === TEST PASSING OBJECT THROUGH FUNCTIONS ===#
# testdict = {
#     'sleep_dur': 440.0, 'rest_gain': 0.73, 'base_fatigue': -0.57, 'rest': [0, 320], 'satiety': [60, -1, 100], 'energy': [100, 100], 'hostility': [100, 100], 'health': [0, 100], 'speed': 70, 'fov': 1000, 'age': 0.00585, 'x': 845.0, 'y': -13085.0, 'task_q': [], 'active_task': ['play', 3, 1, 1], 'knowledge_base': {'utlo': [0.5, 0.5, 1]}, 'interrupt': []
#     }

# def func_1(x):
#     x['rest'][0] = x['rest'][0] + 1
#     return x

# def func_2(x):
#     x['energy'][0] = x['energy'][0] + 2
#     return x

# def func_3(x):
#     x['active_task'] = ['die', 1, 1, 5]
#     return x

# x = func_1(testdict)
# x = func_2(x)
# x = func_3(x)

# print(x)


#=== TEST DICTIONARY UPDATE VS KEY ADDITION ===#
# testdict = {"info": 1, "fish":2, "tiger":{1:5}, "tup": (2,2,2,), "ls":[44,44,44]}

# # update key
# testdict["fish"] = 3
# print(testdict)

# # add key same way?
# testdict['gator'] = (5,5,5)
# print(testdict)

#=== TESTING RANGE ===#
# import random

# # d = dice, s = sides
# def roll(d,s):

#     total = 0
#     for i in range(d):    
#         n = random.randint(1,s)
#         print(n)
#         total = total + n
#     return total

# t = roll(2,6)
# print(t)

# for i in range(1,7):
#     x = roll(1,6)
#     print(x)

#=== TESTING NESTED FUNCTIONS RETURN ===#

# f = "frog"

# def top(f):
#     print("top function")
#     print(f)

#     def middle(f):
#         print("middle function")
#         f = "frogs"
#         print(f)
#         return f
    
#     f = middle(f)
#     if f == "frogs":
#         return f

#     def inner(f):
#         print("inner function")
#         print(f)

#     inner(f)

# top(f)
# print(f)

# === TESTING CURSOR === #
from pymongo import MongoClient
from bson.objectid import ObjectId
import logger2
c = MongoClient()

#db = c['testkows']
db = c['alkows']

def check_for_dup(species,x,y):
    logger2.logger.info("check_for_dup")
    cursor = db.flora_pop.find({ "flora_species_type" : species })
    return cursor

# check for duplicate species at that location
def check_for_duplicate(species,x,y):
    msg = str(x), " ", str(y), " check for duplicate"
    logger2.logger.info(msg)

    # db function
    cursor = check_for_dup(species, x, y)
    for i in cursor:
        if i['x'] == x and i['y'] == y:
            logger2.logger.info("duplicate true")
            return True
        else:
            logger2.logger.info("duplicate false")
            return False

x =check_for_duplicate("buet", 457, 2700)
print(x)

## check this for false and true!