import test_logger2 as logger2

### TESTING ###


min = {
     'sleep_dur': 460.0,
     'rest': [15.07, -1, 170],
     'task_q': [],
     'active_task': ['play', 3, 5, 6],
     'flag': 0
     }

a = {
     'sleep_dur': 460.0,
     'rest': [150.07, -1, 170], 
     'task_q': [],
     'active_task': [],
     'flag': 0
     }

b = {
     'sleep_dur': 460.0,
     'rest': [67.07, -1, 170],  
     'task_q': [],
     'active_task': ["sleep", 1, 0, 460],
     'flag': 0
     }

c = {
     'sleep_dur': 460.0,
     'rest': [67.07, -1, 170], # should generate a p3
     'task_q': [],
     'active_task': [],
     'flag': 0
     }

d = {
     'sleep_dur': 460.0,
     'rest': [15.07, -1, 170],
     'task_q': [["sleep", 1, 0, 460]],
     'active_task': ["play", 1, 0, 460],
     'flag': 0
     }

e = {
     'sleep_dur': 460.0,
     'rest': [15.07, -1, 170],
     'task_q': [["sleep", 3, 0, 460], ["eat", 2, 0, 460]],
     'active_task': ["play", 1, 0, 460],
     'flag': 0
     }


logger2.logger.info("SLEEP TRIGGER TEST")

# SLEEP TRIGGER
def check_current_rest(x):
    logger2.logger.debug("check_current_rest")

    if x['active_task'] == []:
        x['flag'] = 1

    elif x['active_task'][0] == "sleep":
        x['flag'] = 2
        return x


    # less than 40% 
    if x['rest'][0] < x['rest'][2] * .4:
    
        # remove old sleep task from task_q if present
        def remove_old_sleeps(x):
            logger2.logger.info("remove_old_sleeps")

            if x['task_q'] == []:
                return x

            else:
                for i in x['task_q']:
                    if i[0] == "sleep": 
                        x['task_q'].remove(i)

                return x


        x = remove_old_sleeps(x)

        # add sleep task - [task, priority, current turn, max turn]
        if x['rest'][0] < x['rest'][2] * .1:   # <10%
            sleep = ["sleep", 1, 0, x['sleep_dur']]
            x['task_q'].append(sleep) 

        elif x['rest'][0] < x['rest'][2] * .3:   # <30%
            sleep = ["sleep", 2, 0, x['sleep_dur']]
            x['task_q'].append(sleep)  

        elif x['rest'][0] < x['rest'][2] * .4:   # <40%
            sleep = ["sleep", 3, 0, x['sleep_dur']]
            x['task_q'].append(sleep)  

    return x


# TEST 1: active task is empty and sleep > 40% 
x = check_current_rest(a)
assert x['active_task'] == []
assert x['rest'][0] > x['rest'][2] * .4
assert x['flag'] == 1
print("1. pass")

# TEST 2: if active task is sleep, function should exit
x = check_current_rest(b)
assert x['active_task'][0] == 'sleep'
assert x['flag'] == 2
print("2. pass")

# TEST 3: if active task is empty and sleep < 40% a task sleep should be added to task_q at p3
x = check_current_rest(c)
assert x['active_task'] == []
assert x['rest'][0] < x['rest'][2] * .4
assert x['task_q'][0][0] == 'sleep'
assert x['task_q'][0][1] == 3
print("3. pass")

# TEST 4: if sleep < 10% and sleep of p3 already in task_q
x = check_current_rest(d)
assert x['active_task'][0] != 'sleep'
assert x['task_q'][0][1] == 1 
print("4. pass")

