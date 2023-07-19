import logger2
import bartokmongo
from bson.objectid import ObjectId


def history_tracking(x):
    logger2.logger.debug("hist_tracking")

    hist_duration = 200

    # get doc from history.db
    my_id = x['_id']
    h = bartokmongo.get_hist_data(my_id)

    # add id if id not present
    if h == None:
        i = {
            "_id" : my_id,
            "health_hist": [],
            "energy_hist": [],
            "hostility_hist": [],
            "satiety_hist": [],
            "rest_hist": [],          
        }

        i['health_hist'].append(x['health'][0])
        i['hostility_hist'].append(x['hostility'][0])
        i['energy_hist'].append(x['energy'][0])
        i['satiety_hist'].append(x['satiety'][0])
        i['rest_hist'].append(x['rest'][0])

        bartokmongo.add_history(i)

    else:

        h['health_hist'].append(x['health'][0])
        h['hostility_hist'].append(x['hostility'][0])
        h['energy_hist'].append(x['energy'][0])
        h['satiety_hist'].append(x['satiety'][0])
        h['rest_hist'].append(x['rest'][0])

        # update doc in history.db
        bartokmongo.update_history_byid(my_id, h)

    # removes earliest data point if > "history_duration"
    # if len(x['health_hist']) > hist_duration:
    #     i['health_hist'].pop(0)
    # if len(x['hostility_hist']) > hist_duration:
    #     i['hostility_hist'].pop(0)
    # if len(x['energy_hist']) > hist_duration:
    #     i['energy_hist'].pop(0)
    # if len(x['satiety_hist']) > hist_duration:
    #     i['satiety_hist'].pop(0)
    # if len(x['rest_hist']) > hist_duration:
    #     i['rest_hist'].pop(0)



