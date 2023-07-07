
import logger2
import bartokmongo




# ENVIRONMENT AWARENESS CHECK - OBSERVATION, INVESTIGATION, REACTION TRIGGERS
# This is a passive action and does not apply to task_q or active_task - sensing

def observe_fov(x):
    logger2.logger.debug("observe_fov")

    # list of tuples (cret id, species type, active task)
    local_crets = bartokmongo.get_locals(x['x'],x['y'],x['fov'])
    x['local_crets'] = local_crets

    # returns x without updating local crets in db
    return x


# Updates kb details of things observed in fov
def update_kb(x):
    logger2.logger.debug("update_kb")

    local_crets = x['local_crets']
    knowledge_base = x['knowledge_base']

    if local_crets == False:
        logger2.logger.info("no local crets")
        pass

    if knowledge_base == False:
        logger2.logger.info("no knowledge base")
        pass
      
    # local_crets is a list of tuples [(cret_id, species type, active_task)]
    for i in local_crets:
        species_type = i[1]



        # if species type already in kb
        if species_type in knowledge_base:    

            # increment observation count
            if knowledge_base[species_type][0] == .5:
                pass
            else:
                knowledge_base[species_type][0] = knowledge_base[species_type][0] + 1 

            # check if cret action is empty
            if i[2] == []:
                # if no current action
                knowledge_base[species_type][2] = 1
            
            # check if cret is attacking
            elif i[2][0] == "attack":
                # if yes, set response code to hide
                knowledge_base[species_type][2] = 3
                
            else:
                # if no, set response code to no response
                knowledge_base[species_type][2] = 1

        # if cret not in kb
        else:

            # add cret 
            knowledge_base[species_type] = [1, 0, 1]

            # check if cret action is na
            if i[2] == []:
                # if no current action
                knowledge_base[species_type][2] = 1

            # check if cret is attacking
            elif i[2][0] == "attack":
                # if yes, set response code to hide
                knowledge_base[species_type][2] = 3
                
            else:
                # if no, set response code to no response
                knowledge_base[species_type][2] = 1

    return x


# PASSIVE ACTION - in this function we run  observer_fov and update_kb()
def observe(x):
    logger2.logger.debug("observe")
    # observing serves to update the knowledge base, reaction code

    local_crets = observe_fov(x)
    x = update_kb(local_crets)
    return x
    


# UPDATE ATTRIBUTES THAT CHANGE EACH TURN, PERFORM ANY SENSING (Observe, detection checks, etc)
def increment_turn(x):
    logger2.logger.debug("increment_turn")

    # identify creature in logger
    msg = "\033[32m" + "i am: " + str(x['_id']) + " " + str(x['active_task']) + "\033[0m"
    logger2.logger.debug(msg)

    def inc_rest(x):
        x['rest'][0] = round(x['rest'][0] + x['rest'][1], 2)
        return x
    
    def inc_sat(x):
        x['satiety'][0] = round(x['satiety'][0] + x['satiety'][1], 2)
        return x

    if x['active_task'] == []:
        x = inc_rest(x)
        x = inc_sat(x)

    elif x['active_task'][0] != "sleep" and x['active_task'][0] != "eat":
        x = inc_rest(x)
        x = inc_sat(x)

    elif x['active_task'][0] != "sleep":
        x = inc_rest(x)

    elif x['active_task'][0] != "eat":
        x = inc_sat(x)
        
    # make sure rest and sat are not < 0
    if x['rest'][0] < 0: x['rest'][0] = 0
    if x['satiety'][0] < 0: x['satiety'][0] = 0

    # increment age
    x['age'] = round(x['age'] + .0000025, 7)


    x = observe(x)

    return x



