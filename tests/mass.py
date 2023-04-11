# get 75%

from pymongo import MongoClient
from bson.objectid import ObjectId

import random


c = MongoClient()
db = c['alkows']




def mass_extinction_event(collection, percent):
    msg = collection, "mass extinction event has been implemented"

    if collection == "bestiary":
        all = db.bestiary.find()

        all_lst = []
        print("all_lst", all_lst)
        for i in all:
            all_lst.append(i['species_type'])
            print("i", i)

        ct_for_removal = round(len(all_lst) * percent/100)
        print("ct for removal", ct_for_removal)
        for j in range(1, ct_for_removal+1):
            print("j", j)
            x = random.choice(all_lst)
            print("x", x)
            db.bestiary.delete_one( { "species_type": x})

mass_extinction_event("bestiary", 75)