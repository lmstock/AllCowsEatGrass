import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from pymongo import MongoClient
from bson.objectid import ObjectId

c = MongoClient()
db = c['alkows']



def read_individual_byid(id):
    cursor = db.population.find({"_id" : ObjectId(id)})
    return cursor

# Graphs we want for observation panels

# MAP DATA

# map of creature locations
# map of flora locations
# map of both

'''
get historical data once every 5 or 10 turns for longer data set
'''


# HISTORICAL DATA
# line graph of metrics over time for crets historical data

# rest history
# satiety history
# energy history
# hostility history
# health history



#provide _id
cret = "64260b6cfe54c2e96fcba659"

# mongo call for data sets
x = read_individual_byid(cret)

#set data into graph function
for i in x:
    rest_hist = i['rest_hist']
    satiety_hist = i['satiety_hist']

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(rest_hist)  # Plot some data on the axes.

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(satiety_hist)  # Plot some data on the axes.
plt.show()