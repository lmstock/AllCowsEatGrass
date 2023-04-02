import test_logger2 as logger2
import test_core as core

### TESTING ###
# Active task here will alway be the defined action

# satiety: [current, loss per turn, max]
# active_task: [action, priority, current inc, max inc]

a = {
     'satiety': [50, -1, 100],
     'active_task': ['eat', 3, 1, 3]
     }

b = {
     'satiety': [90, -1, 100],
     'active_task': ['eat', 3, 1, 3]
     }


def eat(x):
    logger2.logger.debug("eat")

    # increment active_task
    x = core.incr_active_task(x)

    # increase satiety
    x['satiety'][0] = round(x['satiety'][0] + 33, 2)  

    # do not exceed max_rest remove from active task if full
    if x['satiety'][0] >= x['satiety'][2]:
        x['satiety'][0] = x['satiety'][2]

        #instead of this, remove from active task
        x['active_task'] = []
    
    return x



# TEST 1: active task is increased by 1, satiety is increased
x = eat(a)
assert x['active_task'][2] == 2
assert x['satiety'][0] == 83
print("1. pass")

# TEST 2: active task is completed.
x = eat(b)
assert x['active_task'] == []
print("2. pass")