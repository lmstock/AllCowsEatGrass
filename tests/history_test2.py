from pymongo import MongoClient
from bson.objectid import ObjectId
import test_logger2 as logger2

c = MongoClient()
db = c['alkows']


def get_hist_data(id):
    logger2.logger.info("get_hist_data")
    cursor = db.history.find({"_id" : ObjectId(id)})
    return cursor

def update_history_byid(id, update):
    logger2.logger.debug("update_cret_byid")

    id = {"_id" : ObjectId(id)}
    #logger2.logger.info(str(id))
    
    new_vals = { "$set" : update }
    #logger2.logger.info(str(new_vals))

    db.history.update_one(id, new_vals)

# collect data for historical graphs
# at end of scheduler tick upload data to historical db
# probably dont need every tick, maybe every 10th tick for longer term data.
# at what point does this list length slow things down?

px = {
    "_id": {"$oid": "642840c9a78cb5ad4e6bff40"},
    "health": 200,
    "hostility": 250,
    "energy": 650,
    "satiety": 320,
    "rest": 222
}

my_id = px['_id']["$oid"]

h = get_hist_data(my_id)
for i in h:
    i['health_hist'].append(px['health'])
    i['hostility_hist'].append(px['hostility'])
    i['energy_hist'].append(px['energy'])
    i['satiety_hist'].append(px['satiety'])
    i['rest_hist'].append(px['rest'])

    update_history_byid(my_id, i)
 




