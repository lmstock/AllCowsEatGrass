import archive_tests.logthis as logthis
import random
import mongotest
import creature
import flora



# scheduler runs once a turn and sets each actor to their tasks
def scheduler_run():
    logthis.logger.debug("scheduler_run")
    hist_data_update = []

    # pull list of population -id from db
    p = mongotest.get_population()

    for i in p:

        x = mongotest.read_individual_byid(i)   # x = cursor object
        for j in x:

            # returns dict of historical data for each cret
            hist_data = creature.creature_action(j)

            # add hist_data to list
            hist_data_update.append(hist_data)


        


    # pull list of population -id from db
    f = mongotest.get_flora_population()

    for k in f:

        ind = mongotest.read_flora_ind_byid(k)   # ind = cursor object
        for l in ind:
            flora.flora_action(l)


    # add hist data to collection
    mongotest.add_historical_data(hist_data_update)