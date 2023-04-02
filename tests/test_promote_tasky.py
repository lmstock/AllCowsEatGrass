import test_logger2 as logger2
import random

# TASK_Q = [action string, priority, current turn, duration]

a = {
     'task_q': [],
     'active_task': [],
     'flag': 0
     }

b = {
     'task_q': [["eat", 2, 0, 3],["wander", 3, 0, 3]],
     'active_task': [],
     'flag': 0
     }

c = {
     'task_q': [["eat", 1, 0, 3],["sleep", 1, 0, 3]],
     'active_task': [],
     'flag': 0
     }


def promote_task_q(x):
    logger2.logger.debug("promote_task_q")

    if x['active_task'] == []:

        p1,p2,p3 = [],[],[]

        for i in x['task_q']:
            if i[1] == 1: p1.append(i)
            elif i[1] == 2: p2.append(i)
            else: p3.append(i)


        if p1 != []: t = random.choice(p1)
        elif p2 != []: t = random.choice(p2)
        elif p3 != []: t = random.choice(p3)
        else: 
            t = ["wander", 3, 0, 3]

        x['active_task'] = t

        try:
            x['task_q'].remove(t)
        except Exception as e:
            pass

    return x
    

# TEST 1: task_q is empty
x = promote_task_q(a)
assert x['active_task'][0] == 'wander'
print("1. pass")

# TEST 2: 2 diff priority options in task_q, choose high priority
x = promote_task_q(b)
assert x['active_task'][1] == 2
print("2. pass")

# TEST 2: 2 priority 1 options in task_q
x = promote_task_q(c)
assert x['active_task'][1] == 1
l = len(x['task_q'])
assert l == 1
print("2. pass")