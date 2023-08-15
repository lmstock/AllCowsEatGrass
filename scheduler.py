import logger2
import bartokmongo
import creature
import flora





# scheduler runs once a turn and sets each actor to their tasks
def scheduler_run():
    logger2.logger.debug("scheduler_run")

    # pull list of population -id from db
    p = bartokmongo.get_population()
    pop_count = len(p)
    print("population count: ", pop_count)

    for i in p:
        
        x = bartokmongo.read_ind_by_id(i)   # x = dict
        creature.creature_action(x)




    # pull list of population -id from db
    f = bartokmongo.get_flora_population()

    for k in f:

        ind = bartokmongo.read_flora_ind_byid(k)   # cursor still?
        for l in ind:

            flora.flora_action(l)





