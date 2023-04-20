from pymongo import MongoClient
from bson.objectid import ObjectId
import test_logger2 as logger2

c = MongoClient()
db = c['alkows']


def get_hist_data(x):
    logger2.logger.info("get_hist_data")
    cursor = db.history.find({"_id": x})
    return cursor

def update_history_byid(id, update):
    logger2.logger.debug("update_history_byid")

    id = {"_id" : ObjectId(id)}
    #logger2.logger.info(str(id))
    
    new_vals = { "$set" : update }
    #logger2.logger.info(str(new_vals))

# collect data for historical graphs
# at end of scheduler tick upload data to historical db
# probably dont need every tick, maybe every 10th tick for longer term data.
# at what point does this list length slow things down?

p = {
    "_id": 555,
    'rest_hist': [2],
    'sat_hist': [2],
    'energy_hist': [2],
    'host_hist': [2],
    'health_hist': [3]
    }

update_hist_data(p)


def hist_tracking(x):
    logger2.logger.debug("hist_tracking")

    duration = 10000
    my_id = x["_id"]

    # get doc from history.db
    p = get_hist_data(my_id)
    for i in p:

        # adding the data points
        if i == 'rest_hist':
            i['rest_hist'].append(x['rest'][0])

        if i == 'sat_hist':
            i['sat_hist'].append(x['satiety'][0])

        if i == 'energy_hist':
            i['energy_hist'].append(x['energy'][0])

        if i == 'host_hist':
            i['host_hist'].append(x['hostility'][0])

        if i == 'health_hist':
            i['health_hist'].append(x['health'][0])

    
        # removes earliest data point if > "history_duration"
        if len(i['rest_hist']) > duration:
            i['rest_hist'].pop(0)

        if len(i['sat_hist']) > duration:
            i['sat_hist'].pop(0)

        if len(i['energy_hist']) > duration:
            i['energy_hist'].pop(0)

        if len(i['host_hist']) > duration:
            i['host_hist'].pop(0)

        if len(i['health_hist']) > duration:
            i['health_hist'].pop(0)

        update = {
            
        }

    # update doc in history.db