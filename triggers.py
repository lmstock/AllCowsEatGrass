
import random

import logger2 
import mongotest


def trigger_tasks(s):
    logger2.logger.debug("trigger_tasks")

    interrupt = s['interrupt']
    active_task = s['active_task']
    rest = s['rest']
    task_q = s['task_q']
    satiety = s['satiety']
    sleep_dur = s['sleep_dur']
    x = s['x']
    y = s['y']
    fov = s['fov']
    kb = s['knowledge_base']

    
    interrupt_update = check_for_interrupt(interrupt)
    interrupt = interrupt_update


    sleep_update = check_current_rest(active_task, rest, task_q, sleep_dur)
    active_task = sleep_update[0]
    rest = sleep_update[1]
    task_q = sleep_update[2]
    sleep_dur = sleep_update[3]


    eat_update = check_current_satiety(active_task, satiety, task_q)
    active_task = eat_update[0]
    satiety = eat_update[1]
    task_q = eat_update[2]

    local_crets = check_fov(x,y,fov) # returns a list of creatures in fov by creature_id
    env_update = check_kb(local_crets, kb, interrupt, task_q)
    kb = env_update[1]
    interrupt = env_update[2]
    task_q = env_update[3]
    
    return s


# INTERRUPT - not yet implemented
def check_for_interrupt(interrupt):
    logger2.logger.debug("check_for_interrupt")

    if interrupt == True:
        pass


# SLEEP TRIGGER
def check_current_rest(active_task, rest, task_q, sleep_dur):
    logger2.logger.debug("check_current_rest")

    if active_task == []:
        logger2.logger.debug("active task is empty")

    elif active_task[0] == "sleep":
        var_list = [active_task, rest, task_q, sleep_dur]
        return var_list


    # less than 40% 
    if rest[0] < rest[1] * .4:
    
        # remove old sleep tasks from task_q if present
        def remove_old_sleeps():
            logger2.logger.debug("remove_old_sleeps")

            if task_q == []:
                return

            else:
                for i in task_q:
                    if i[0] == "sleep":
                        task_q.remove(i)

        remove_old_sleeps()

        # add sleep task - [task, priority, current turn, max turn]
        if rest[0] < rest[1] * .1:   # <10%
            sleep = ["sleep", 1, 0, sleep_dur]

        elif rest[0] < rest[1] * .3:   # <30%
            sleep = ["sleep", 2, 0, sleep_dur]

        elif rest[0] < rest[1] * .4:   # <40%
            sleep = ["sleep", 3, 0, sleep_dur]

        task_q.append(sleep)  
    var_list = [active_task, rest, task_q, sleep_dur]
    
    return var_list

# EAT TRIGGER
def check_current_satiety(active_task, satiety, task_q):
    logger2.logger.debug("check_current_satiety")

    if active_task == []:
        logger2.logger.debug("active task is empty")
    

    elif active_task[0] == "eat":
        var_list = [active_task, satiety, task_q]
        return var_list


    # if satiety less than 40%
    if satiety[0] < satiety[2] * .4:
        
        # remove old eat tasks from task_q if present
        def remove_old_eats():
            logger2.logger.debug("remove_old_eats")

            if task_q == []:
                pass

            else:
                for i in task_q:
                    if i[0] == "eat":
                        task_q.remove(i)

        remove_old_eats()

        # add eat task - [task, priority, current turn, max turn]
        if satiety[0] < satiety[2] * .1:   # <10%
            eat = ["eat", 1, 0, 6]

        elif satiety[0] < satiety[2] * .3:   # <30%
            eat = ["eat", 2, 0, 6]

        elif satiety[0] < satiety[2] * .4:   # <40%
            eat = ["eat", 3, 0, 6]

        task_q.append(eat) 
    
    var_list = [active_task, satiety, task_q]
    return var_list



# ENVIRONMENT AWARENESS CHECK - OBSERVATION, INVESTIGATION, REACTION TRIGGERS
def check_fov(x,y,fov):
    logger2.logger.debug("check_fov")

    # chance to check fov, because we arent always paying attention
    #if s.salt[0] < 5:

    # locals list
    local_crets = mongotest.get_locals(x,y,fov)
    return local_crets


# do i know you ? - check knowledge base for species id, return response code
# in the form of a list. 
# [response code, any necessary details (retreat direction for ex)]
def check_kb(local_crets, kb, interrupt, task_q):
    logger2.logger.debug("check_kb")

    if local_crets == False:
        pass

    elif len(local_crets) == 1:        
        for i in local_crets:
            if i in kb:
                response_code = kb[i][2]
                if response_code == 1:
                    pass
                if response_code == 2:
                    pass # observe = ["observe", 1, 0, 1]
                if response_code == 3:
                    pass # retreat
                if response_code == 4:
                    pass # attack
                if response_code == 5:
                    pass # investigate
                if response_code == 6:
                    pass # hide sneak
            else:
                pass    # set observe trigger for that species type

    elif len(local_crets) > 1:
        i = random.choice(local_crets)

        if i in kb:
            response_code = kb[i][2]
            if response_code == 1:
                pass
            if response_code == 2:
                pass # observe = ["observe", 1, 0, 1]
            if response_code == 3:
                pass # retreat
            if response_code == 4:
                pass # attack
            if response_code == 5:
                pass # investigate
            if response_code == 6:
                pass # hide sneak
        else:
            pass    # set observe trigger for that species type

    ret_values = [local_crets, kb, interrupt, task_q]
    return ret_values


