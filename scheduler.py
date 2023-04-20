import logger2
import bartokmongo
import creature
import flora
import compendiums
import census_data




# scheduler runs once a turn and sets each actor to their tasks
def scheduler_run():
    logger2.logger.debug("scheduler_run")

    # pull list of population -id from db
    p = bartokmongo.get_population()

    for i in p:

        x = bartokmongo.read_ind_by_id(i)   # x = cursor object
        creature.creature_action(x)



    # pull list of population -id from db
    f = bartokmongo.get_flora_population()

    for k in f:

        ind = bartokmongo.read_flora_ind_byid(k)   # ind = cursor object
        for l in ind:

            flora.flora_action(l)





