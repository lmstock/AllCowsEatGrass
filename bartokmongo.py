from pymongo import MongoClient
from bson.objectid import ObjectId
import logger2
import random


c = MongoClient()
db = c['alkows']

# === ADDING === #
def add_creature_species(sp):
    logger2.logger.debug("add_creature_species")
    db.bestiary.insert_one(sp)

def add_flora_species(fsp):
    logger2.logger.debug("add_flora_species")
    db.herbarium.insert_one(fsp)

def add_creature(cret):
    logger2.logger.debug("add_creature")
    db.population.insert_one(cret)

def add_test_creature(cret):
    logger2.logger.debug("add_creature")
    x = db.population.insert_one(cret)
    return x

def add_flora(flora):
    logger2.logger.debug("add_flora")
    db.flora_pop.insert_one(flora)

# === REMOVING === #
def remove_test_crets():
    logger2.logger.error("remove_test_crets")
    query = { "species_type" : {'$regex':'^testcreature'}}
    db.population.delete_many(query)

def remove_test_species():
    query = { "species_type" : {'$regex':'^testcreature'}}
    db.bestiary.delete_many(query)

def remove_individual_byid(id):
    logger2.logger.info("remove_individual_byid")
    db.population.delete_one( { "_id" : id } )

def clear_db():
    logger2.logger.debug("clear_db")
    db.bestiary.drop()
    db.population.drop()
    db.herbarium.drop()
    db.flora_pop.drop()
    db.history.drop()

def full_extinction_event(collection):
    msg = collection, "full extinction event has been implemented"
    logger2.logger.info(msg)
    if collection == "bestiary":
        db.bestiary.drop()
    elif collection == "population":
        db.population.drop()
    elif collection == "herbarium":
        db.herbarium.drop()
    elif collection == "flora_pop":
        db.flora_pop.drop()

# percent is very approximate, random choice from list may choose the same unit twice.
# actual percentage may be lower
def mass_extinction_event(collection, percent):
    msg = collection, "mass extinction event has been implemented"
    logger2.logger.info(msg)

    if collection == "bestiary":
        all = db.bestiary.find()

        all_lst = []
        for i in all:
            all_lst.append(i['species_type'])

        lenlist = len(all_lst)
        ct_for_removal = round(lenlist * percent/100)
        print(ct_for_removal)
        for j in range(1, ct_for_removal+1):
            x = random.choice(all_lst)
            db.bestiary.delete_one( { "species_type": x})

    if collection == "population":
        all = db.population.find()

        all_lst = []
        for i in all:
            all_lst.append(i['_id'])

        lenlist = len(all_lst)
        ct_for_removal = round(lenlist * percent/100)
        print(ct_for_removal)
        for j in range(1, ct_for_removal+1):
            x = random.choice(all_lst)
            db.population.delete_one( { "_id" : x } )

    if collection == "herbarium":
        all = db.herbarium.find()

        all_lst = []
        for i in all:
            all_lst.append(i['flora_species_type'])

        lenlist = len(all_lst)
        ct_for_removal = round(lenlist * percent/100)
        print(ct_for_removal)
        for j in range(1, ct_for_removal+1):
            x = random.choice(all_lst)
            db.herbarium.delete_one( { 'flora_species_type' : x } )

    if collection == "flora_pop":
        all = db.flora_pop.find()

        all_lst = []
        for i in all:
            all_lst.append(i['_id'])

        lenlist = len(all_lst)
        ct_for_removal = round(lenlist * percent/100)
        print("should be 75%", ct_for_removal)
        for j in range(1, ct_for_removal+1):
            x = random.choice(all_lst)
            db.flora_pop.delete_one( { "_id" : x } )



# === READING === #

def get_rand_pop():
    logger2.logger.info("get_rand_pop")
    cursor = db.population.aggregate([{"$sample" : {'size': 4}}])
    return cursor

def find_latest_addition():
    logger2.logger.debug("find_latest_addition")
    x = db.population.find().sort("_id",-1).limit(1)
    return x

def list_beasts():
    logger2.logger.debug("list_beasts")
    beasts = db.bestiary.find()
    beast_list = []
    for i in beasts:
        beast_list.append(i['species_type'])
    return beast_list

def list_flora():
    logger2.logger.debug("list_flora")
    flora = db.herbarium.find()
    flora_list = []
    for i in flora:
        flora_list.append(i['flora_species_type'])
    return flora_list

def get_bestiary():
    logger2.logger.debug("get_bestiary")
    beasts = db.bestiary.find()
    bestiary = {}
    for i in beasts:
        bestiary.update({i['species_type']:i})
    logger2.logger.debug(bestiary)
    return bestiary

def get_herbarium():
    logger2.logger.debug("get_herbarium")
    flora = db.herbarium.find()
    herbarium = {}
    for i in flora:
        herbarium.update({i['flora_species_type']:i})
    logger2.logger.debug(herbarium)
    return herbarium

def get_cret_census():
    logger2.logger.debug("get_census")
    cret_collection = db.population.find()
    cret_dict = {}
    for i in cret_collection:
        cret_dict.update({i['_id']:i})
    return cret_dict


def get_flora_census():
    logger2.logger.debug("get_flora_census")
    flora_collection = db.flora_pop.find()
    flora_dict = {}
    for i in flora_collection:
        flora_dict.update({i['_id']:i})
    return flora_dict

def get_collection(collection_name):
    cursor = db.collection_name.find()
    census_dict = {}
    for i in cursor:
        census_dict.update({i['_id']:i})
    return census_dict

def get_population():
    logger2.logger.debug("get_population")
    # get _ids
    population = db.population.find()
    actors_list = []
    for i in population:
        actors_list.append(i['_id'])
    return actors_list

def get_flora_population():
    logger2.logger.debug("get_flora_population")
    # get _ids
    flora_pop = db.flora_pop.find()
    flora_list = []
    for i in flora_pop:
        flora_list.append(i['_id'])
    return flora_list

def read_creature_species(a , b):
    logger2.logger.debug("read_species")
    cursor = db.bestiary.find({ a : b })
    return cursor

def read_creature_species_du(a , b):
    logger2.logger.debug("read_species")
    species_dict = db.bestiary.find_one({ a : b })
    return species_dict

def read_flora_species(a,b):
    logger2.logger.debug("read flora species")
    cursor = db.herbarium.find({a:b})
    return cursor

def read_flora_species_du(a,b):
    logger2.logger.info("read flora species")
    cursor = db.herbarium.find_one({a:b})
    return cursor

def read_population(a,b):
    logger2.logger.debug("read_population")
    cursor = db.population.find({ a : b })
    return cursor


def read_creature_parent(id):    # REPLACE THIS WITH 3RD
    logger2.logger.debug("read_creature_parent")
    parent_dict = db.population.find_one({"_id" : id})
    return parent_dict

# findone returns a dict rather than a cursor
def read_ind_by_id(id):    # REPLACE OTHER TWO WITH THIS ONE
    logger2.logger.debug("read_creature_parent")
    ind_dict = db.population.find_one({"_id" : ObjectId(id)})
    return ind_dict

# used in testing - see test_division
def read_ind_by_name(name):
    logger2.logger.info("read_ind_by_name")
    ind_dict = db.population.find_one({"species_type" : name})
    return ind_dict

##############################################################

def read_flora_ind_byid(id):
    logger2.logger.debug("read_flora_ind_byid")
    cursor = db.flora_pop.find({"_id" : ObjectId(id)})
    return cursor


# returns a list of tuples (creature id, species type, active_task)
def get_locals(x,y,fov):
    logger2.logger.debug("get_locals")

    # compass equivalent {"and": [{"x": {"$gt": 200}}, {"x": {"$lt": 300}}]}
    x = db.population.find({"$and": [{"x": {"$gt": x - fov}},
                                     {"x": {"$lt": x + fov}},
                                     {"y": {"$gt": y - fov}},
                                      {"y": {"$lt": y + fov}}
                                    ]})

    local_crets = []
    for i in x:
        local_crets.append((i['_id'], i['species_type'], i['active_task']))

    # list of tuples (cret id, species type, active_task)
    return local_crets


# update = {"x": 500, "y": 590}
# update_cret_byid("6400b0b89089706e43621b46", update)
def update_cret_byid(id, update):
    logger2.logger.debug("update_cret_byid")

    id = {"_id" : ObjectId(id)}
    #logger2.logger.info(str(id))
    
    new_vals = { "$set" : update }
    #logger2.logger.info(str(new_vals))

    db.population.update_one(id, new_vals)




def update_flora_byid(id, update):
    logger2.logger.debug("update_flora_byid")

    id = {"_id" : ObjectId(id)}
    #logger2.logger.debug(str(id))
    
    new_vals = { "$set" : update }
    #logger2.logger.debug(str(new_vals))

    db.flora_pop.update_one(id, new_vals)




def update_species_by_name(name, update):
    logger2.logger.debug("update_species_by_name")
    by_name = {"species_type": name}
    x = db.bestiary.update_one(by_name, update)
    print(x.modified_count)

def add_to_mortuary(unit):
    logger2.logger.debug("add_to_mortuary")
    try:
        db.mortuary.insert_one(unit)
    except Exception as e:
        msg = "send to log file: ", e

def check_for_dup(species,x,y):
    logger2.logger.debug("check_for_dup")
    cursor = db.flora_pop.find({ "flora_species_type" : species })
    return cursor

# ===== WORLD =====
def get_world_data(world_name):
    logger2.logger.debug("get_world_data")
    cursor = db.world.find({ "world_name" : world_name })
    return cursor

def update_world(world_name, update):
    logger2.logger.debug("update_world_data")
    
    name = {"world_name" : world_name }
    new_vals = { "$set" : update }
    db.world.update_one(name, new_vals)



# === HISTORICAL === #
def get_hist_data(id):
    logger2.logger.debug("get_hist_data")
    cursor = db.history.find_one({"_id" : id })
    return cursor

def add_history(h):
    logger2.logger.debug("add_history_byid")
    db.history.insert_one(h)

def update_history_byid(id, update):
    logger2.logger.debug("update_cret_byid")

    id = {"_id" : ObjectId(id)}
    #logger2.logger.info(str(id))
    
    new_vals = { "$set" : update }
    #logger2.logger.info(str(new_vals))

    db.history.update_one(id, new_vals)


