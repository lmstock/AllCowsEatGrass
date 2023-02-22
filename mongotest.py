from pymongo import MongoClient
import archive_tests.archiveLogger as archiveLogger

c = MongoClient()

db = c['gladeData']

def add_species(sp):
    archiveLogger.logger.info("add_species")

    species = db.species
    post_id = species.insert_one(sp).inserted_id

    x = db.list_collection_names()
    print(x)