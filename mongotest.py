from pymongo import MongoClient
from bson.objectid import ObjectId
import logger2


c = MongoClient()

#db = c['testkows']
db = c['alkows']

def add_creature_species(sp):
    logger2.logger.info("add_creature_species")
    db.bestiary.insert_one(sp)

def add_flora_species(fsp):
    logger2.logger.info("add_flora_species")
    db.herbarium.insert_one(fsp)

def add_creature(cret):
    logger2.logger.info("add_creature")
    db.population.insert_one(cret)

def add_flora(flora):
    logger2.logger.info("add_flora")
    db.flora_pop.insert_one(flora)

def clear_db():
    logger2.logger.info("clear_db")
    db.bestiary.drop()
    db.population.drop()
    db.herbarium.drop()
    db.flora_pop.drop()


def list_beasts():
    logger2.logger.info("list_beasts")
    beasts = db.bestiary.find()
    beast_list = []
    for i in beasts:
        beast_list.append(i['species_type'])
    return beast_list

def list_flora():
    logger2.logger.info("list_flora")
    flora = db.herbarium.find()
    flora_list = []
    for i in flora:
        flora_list.append(i['flora_type'])
    return flora_list

def get_population():
    logger2.logger.info("get_population")
    # get _ids
    population = db.population.find()
    actors_list = []
    for i in population:
        actors_list.append(i['_id'])
    return actors_list

def get_flora_population():
    logger2.logger.info("get_flora_population")
    # get _ids
    flora_pop = db.flora_pop.find()
    flora_list = []
    for i in flora_pop:
        flora_list.append(i['_id'])
    return flora_list

def read_creature_species(a , b):
    logger2.logger.info("read_species")
    cursor = db.bestiary.find({ a : b })
    return cursor

def read_flora_species(a,b):
    logger2.logger.info("read flor species")
    cursor = db.herbarium.find({a:b})
    return cursor

def read_population(a,b):
    logger2.logger.info("read_population")
    cursor = db.population.find({ a : b })
    return cursor

def read_individual_byid(id):
    logger2.logger.info("read_individual_byid")
    cursor = db.population.find({"_id" : ObjectId(id)})
    return cursor

def read_flora_ind_byid(id):
    logger2.logger.info("read_flora_ind_byid")
    cursor = db.flora_pop.find({"_id" : ObjectId(id)})
    return cursor


# returns a list of species _ids
def get_locals(x,y,fov):
    logger2.logger.info("get_locals")

    # compass equivalent {"and": [{"x": {"$gt": 200}}, {"x": {"$lt": 300}}]}
    x = db.population.find({"$and": [{"x": {"$gt": x - fov}},
                                     {"x": {"$lt": x + fov}},
                                     {"y": {"$gt": y - fov}},
                                      {"y": {"$lt": y + fov}}
                                    ]})

    local_crets = []
    for i in x:
        local_crets.append(i['species_type'])

    # list of _ids
    return local_crets


# update = {"x": 500, "y": 590}
# update_cret_byid("6400b0b89089706e43621b46", update)
def update_cret_byid(id, update):
    logger2.logger.info("update_cret_byid")

    id = {"_id" : ObjectId(id)}
    new_vals = { "$set" : update }
    db.population.update_one(id, new_vals)


    # ===== TESTING =====

