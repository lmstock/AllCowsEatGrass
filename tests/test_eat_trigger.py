import logger2

### TESTING ###


a = {

     'satiety': [100, -1, 100],
     'task_q': [],
     'active_task': [],
     'flag': 0
     }

b = {

     'satiety': [100, -1, 100],
     'task_q': [],
     'active_task': ['eat', 3, 5, 6],
     'flag': 0
     }

c = {

     'satiety': [38, -1, 100],
     'task_q': [],
     'active_task': [],
     'flag': 0
     }

d = {

     'satiety': [4, -1, 100],
     'task_q': [['eat', 3, 5, 6]],
     'active_task': ['play', 3, 5, 6],
     'flag': 0
     }

logger2.logger.info("EAT TRIGGER TEST")


# EAT TRIGGER
def check_current_satiety(x):
    logger2.logger.debug("check_current_satiety")

    if x['active_task'] == []:
        logger2.logger.debug("active task is empty")
        x['flag'] = 1
    

    elif x['active_task'][0] == "eat":
        x['flag'] = 2
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

# TEST 1: active task is empty and satiety > 40% 
x = check_current_satiety(a)
assert x['active_task'] == []
assert x['satiety'][0] > x['satiety'][2] * .4
assert x['flag'] == 1
print("1. pass")

# TEST 2: if active task is eat, function should exit
x = check_current_satiety(b)
assert x['active_task'][0] == 'eat'
assert x['flag'] == 2
print("2. pass")

# TEST 3: if active task is empty and eat < 40% a task eat should be added to task_q at p3
x = check_current_satiety(c)
assert x['active_task'] == []
assert x['satiety'][0] < x['satiety'][2] * .4
assert x['task_q'][0][0] == 'eat'
assert x['task_q'][0][1] == 3
print("3. pass")

# TEST 4: if eat < 10% and eat of p3 already in task_q
x = check_current_satiety(d)
assert x['active_task'][0] != 'eat'
assert x['task_q'][0][1] == 1 
print("4. pass")

