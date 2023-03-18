
import random

import logger2 
import mongotest

### TASK_Q = [action string, priority, current turn, max turn]

def trigger_tasks(s):
    logger2.logger.debug("trigger_tasks")

    x = check_current_rest(s)
    x = check_current_satiety(x)
    x = check_health(x)

    local_crets = check_fov(x)
    x = check_kb(x, local_crets)
    
    return x



# SLEEP TRIGGER
def check_current_rest(x):
    logger2.logger.debug("check_current_rest")

    if x['active_task'] == []:
        logger2.logger.debug("active task is empty")

    elif x['active_task'][0] == "sleep":
        return x

    # less than 40% 
    if x['rest'][0] < x['rest'][1] * .4:
    
        # remove old sleep tasks from task_q if present
        def remove_old_sleeps():
            logger2.logger.debug("remove_old_sleeps")

            if x['task_q'] == []:
                return

            else:
                for i in x['task_q']:
                    if i[0] == "sleep":
                        x['task_q'].remove(i)

        remove_old_sleeps()

        # add sleep task - [task, priority, current turn, max turn]
        if x['rest'][1] < x['rest'][1] * .1:   # <10%
            sleep = ["sleep", 1, 0, x['sleep_dur']]
            x['task_q'].append(sleep)  

        elif x['rest'][1] < x['rest'][1] * .3:   # <30%
            sleep = ["sleep", 2, 0, x['sleep_dur']]
            x['task_q'].append(sleep)  

        elif x['rest'][1] < x['rest'][1] * .4:   # <40%
            sleep = ["sleep", 3, 0, x['sleep_dur']]
            x['task_q'].append(sleep)  
        
    
    return x

# EAT TRIGGER
def check_current_satiety(x):
    logger2.logger.debug("check_current_satiety")

    if x['active_task'] == []:
        logger2.logger.debug("active task is empty")
    

    elif x['active_task'][0] == "eat":
        return x


    # if satiety less than 40%
    if x['satiety'][0] < x['satiety'][2] * .4:
        
        # remove old eat tasks from task_q if present
        def remove_old_eats():
            logger2.logger.debug("remove_old_eats")

            if x['task_q'] == []:
                pass

            else:
                for i in x['task_q']:
                    if i[0] == "eat":
                        x['task_q'].remove(i)

        remove_old_eats()

        # add eat task - [task, priority, current turn, max turn]
        if x['satiety'][0] < x['satiety'][2] * .1:   # <10%
            eat = ["eat", 1, 0, 6]

        elif x['satiety'][0] < x['satiety'][2] * .3:   # <30%
            eat = ["eat", 2, 0, 6]

        elif x['satiety'][0] < x['satiety'][2] * .4:   # <40%
            eat = ["eat", 3, 0, 6]

        x['task_q'].append(eat) 
    
    return x

# CHECK HEALTH (should I be dead?)
def check_health(x):
    logger2.logger.debug("check_health")

    if x['rest'][0] == 0:
        loss = x['health'][1] * .1
        x['health'][0] = x['health'][0] - loss

    if x['satiety'][0] ==0:
        loss = x['health'][1] * .1
        x['health'][0] = x['health'][0] - loss

    if x['health'][0] <= 0:
        logger2.logger.info("health <= 0")
        x['health'][0] = 0
        x['is_alive'] = False
        x['task_q'] = ["die", 1, 1, 5]
        x['active_task'] = ["die", 1, 1, 5]

    return x

# ENVIRONMENT AWARENESS CHECK - OBSERVATION, INVESTIGATION, REACTION TRIGGERS
def check_fov(x):
    logger2.logger.debug("check_fov")

    # chance to check fov, because we arent always paying attention
    #if s.salt[0] < 5:

    # list of tuples (cret id, species type)
    local_crets = mongotest.get_locals(x['x'],x['y'],x['fov'])
    return local_crets

# do i know you ? - check knowledge base for species type, return response code
# in the form of a list. 
# [response code, any necessary details ie. retreat direction)]
def check_kb(x, local_crets):

    # x is active creature dict, local_crets is a list of creature tuples on fov
    logger2.logger.debug("check_kb")

    if local_crets == False:
        pass
      
    # local_crets is a list of tuples (cret_id, species type, active_task)
    for i in local_crets:

        if i[1] in x['knowledge_base']:

            # some key/index confusion trying to access this so renaming to foo
            species_name = i[1]
            response_code = x['knowledge_base'][species_name][2]

            if response_code == 1:
                return x
            
            elif response_code == 2:
                x['active_task'] = ["observe", 1, 0, 1, i] # observe = ["observe", 1, 0, 1, "interact with creature _id"]; i is a tuple
                return x
            
            elif response_code == 3:
                pass # retreat
            
            elif response_code == 4:
                pass # attack
            
            elif response_code == 5:
                pass # investigate
            
            elif response_code == 6:
                pass # hide sneak
        
        else:
            x['active_task'] = ["observe", 1, 0, 1, i] # observe = ["observe", 1, 0, 1, "interact with creature _id"]; i is a tuple
            return x
  
        print(x)
        return x
    print(x)
    return x


