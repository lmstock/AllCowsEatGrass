from pymongo import MongoClient
import log_this

c = MongoClient()

db = c['gladeData']

def add_species(sp):
    log_this.logger.info("add_species")

    species = db.species
    post_id = species.insert_one(sp).inserted_id

    x = db.list_collection_names()
    print(x)