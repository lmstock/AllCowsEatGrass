import test_logger2 as logger2
import test_core as core

### TESTING ###
# Active task here will alway be the defined action

# rest: [current, loss per turn, max]
# active_task: [action, priority, current inc, max inc]

a = {
     'rest': [250, -1.41, 520],
     'active_task': ['sleep', 3, 1, 630],
     'rest_gain': .79
     }

b = {
     'rest': [99, -1, 100],
     'active_task': ['sleep', 3, 1, 630],
     'rest_gain': 2
     }

c = {
     'rest': [99, -1, 700],
     'active_task': ['sleep', 3, 629, 630],
     'rest_gain': 2
     }


def sleep(x):
    logger2.logger.debug("sleep")

    # increment active_task
    x = core.incr_active_task(x)

    # increase current_rest
    x['rest'][0] = round(x['rest'][0] + x['rest_gain'], 2)

    # do not exceed max_rest remove from active task if full
    if x['rest'][0] >= x['rest'][2]:
        x['rest'][0] = x['rest'][2]

        # clear active_task
        x['active_task'] = []

    return x



# TEST 1: active task is increased by 1, rest is increased
x = sleep(a)
assert x['active_task'][2] == 2
assert x['rest'][0] == 250.79
print("1. pass")

# TEST 2: active task is completed due to well rested.
x = sleep(b)
assert x['active_task'] == []
print("2. pass")

