
import random
import logger2 
import bartokmongo

### TASK_Q = [action string, priority, current turn, max turn]

def trigger_tasks(s):
    logger2.logger.debug("trigger_tasks")

    x = check_current_rest(s)
    x = check_current_satiety(x)
    x = check_health(x)
    x = check_division(x)
    x = wellness_check(x)
    x = check_hostility(x)

    return x

# HEALTH IMPROVES IF SAT AND REST ARE >90%
def wellness_check(x):
    logger2.logger.debug("wellness_check")

    if x['rest'][0] >= x['rest'][1] * .75 and x['satiety'][0] >= x['satiety'][1] * .75:
        x['health'][0] = x['health'][0] + 1

    if x['health'][0] > x['health'][1]:
        x['health'][0] = x['health'][1]

    return x


# DIVISION TRIGGER
def check_division(x):

    def check_cooldown(f):
        logger2.logger.debug("check_cooldown")
        if f['repr_cooldown'][0] >= f['repr_cooldown'][1]:
            logger2.logger.debug("passed cool down")
            return True
        else: 
            logger2.logger.debug("failed cool down")

            # increment cool down
            f['repr_cooldown'][0] = f['repr_cooldown'][0] + 1
            return False
        
    pass_cooldown = check_cooldown(x)
    if pass_cooldown == False:
        return x
    
    else:
        divide = ["divide", 2, 0, 1]
        if divide not in x['task_q']:
            x['task_q'].append(divide)
            x['repr_cooldown'][0] = 0
            
        return x

# SLEEP TRIGGER
def check_current_rest(x):
    logger2.logger.debug("check_current_rest")

    if x['active_task'] == []:
        logger2.logger.debug("active task is empty")

    elif x['active_task'][0] == "sleep":
        return x
    
    elif x['is_alive'] == False:
        return x

    # less than 40% 
    if x['rest'][0] < x['rest'][2] * .4:
    
        # remove old sleep tasks from task_q if present
        def remove_old_sleeps():
            logger2.logger.debug("remove_old_sleeps")

            if x['task_q'] == []:
                return

            else:
                for i in x['task_q']:
                    if i[0] == "sleep":
                        x['task_q'].remove(i)
                
                return x

        remove_old_sleeps()

        # add sleep task - [task, priority, current turn, max turn]
        if x['rest'][0] < x['rest'][2] * .1:   # <10%
            sleep = ["sleep", 1, 0, x['sleep_duration']]
            x['task_q'].append(sleep)  

        elif x['rest'][0] < x['rest'][2] * .3:   # <30%
            sleep = ["sleep", 2, 0, x['sleep_duration']]
            x['task_q'].append(sleep)  

        elif x['rest'][0] < x['rest'][2] * .4:   # <40%
            sleep = ["sleep", 3, 0, x['sleep_duration']]
            x['task_q'].append(sleep)  
        
    
    return x

# EAT TRIGGER
def check_current_satiety(x):
    logger2.logger.debug("check_current_satiety")

    if x['active_task'] == []:
        logger2.logger.debug("active task is empty")
    

    elif x['active_task'][0] == "eat":
        return x

    elif x['is_alive'] == False:
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
        logger2.logger.debug("health <= 0")
        x['health'][0] = 0
        x['is_alive'] = False
        x['task_q'] = []
        x['active_task'] = ["die", 1, 1, 5]

    return x

# CHECK HOSTILITY (triggers attack)
def check_hostility(x):
    logger2.logger.debug("check_hostility")

    if x['active_task'] == []:
        pass

    elif x['active_task'][0] == "attack":
        return x
    
    elif x['active_task'][0] == "die":
        return x

    if x['hostility'][0] >= x['hostility'][1] * .9:
        msg = " \033[31ma creature " + str(x['_id']) + " has become hostile !\033[0m"
        logger2.logger.info(msg)

        # returns if there are no local crets
        if len(x['local_crets']) <= 1 :
            return x

        else: 
            lc = x['local_crets']

            # create list of local cret ids
            local_cret_ids = []
            for i in lc:
                local_cret_ids.append(i[0])

            # remove self from local crets ids list
            if x['_id'] in local_cret_ids:
                local_cret_ids.remove(x['_id'])

            # choose and set target at random from local crets
            x['target'] = random.choice(local_cret_ids)

            # set active task to attack
            x['active_task'] = ["attack", 1, 0, 3]
                
            return x
    else:
        return x


