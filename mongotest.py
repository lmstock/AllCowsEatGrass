from pymongo import MongoClient
import archive_tests.archiveLogger as archiveLogger

c = MongoClient()


db = c['alkows']

def add_species(sp):
    archiveLogger.logger.info("add_species")
    db.species.insert_one(sp)


def add_creature(cret):
    archiveLogger.logger.info("add_creature")
    db.population.insert_one(cret)

def clear_db():
    archiveLogger.logger.info("clear_db")
    db.species.drop()
    db.population.drop()


# ===== TESTING =====
def read_species():
    archiveLogger.logger.info("read_species")
    
    x = db.species.find({ "head" : "small" })

    for i in x:
        print(i['_id'])
        print(i['name'])
#read_species()


def read_population():
    archiveLogger.logger.info("read_population")
    
    x = db.population.find({ "size" : "small" })

    for i in x:
        print(i['_id'])
        print(i['type'])
        
read_population()
