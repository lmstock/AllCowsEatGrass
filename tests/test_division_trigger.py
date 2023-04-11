

import test_logger2 as logger2

# === TEST CASES === #
a = {'_id': 'ObjectId("642d5e373990c645704b99cc")', 'repr_cooldown': [0, 10000], 'task_q': [], 'active_task': []}
b = {'_id': 'ObjectId("642d5e373990c645704b99cc")', 'repr_cooldown': [99, 99], 'task_q': [], 'active_task': []}

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
        x['task_q'].append(divide)
        x['repr_cooldown'][0] = 0
        return x


### TESTING ###
# TEST 1
x = check_division(a)
assert x['repr_cooldown'][0] == 1
assert x['task_q'] == []
print("TEST 1 pass")

# TEST 2
x = check_division(b)
assert x['repr_cooldown'][0] == 0
assert x['task_q'] != []
print("TEST 2 pass")


