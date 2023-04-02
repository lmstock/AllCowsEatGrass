import random
import logger2



# d = dice, s = sides
def roll(d,s):
    logger2.logger.debug("roll")
    total = 0
    for i in range(d):    
        n = random.randint(1,s)
        total = total + n
    return total


def incr_active_task(x):
    x['active_task'][2] = x['active_task'][2] + 1
    return x

def fence(x):
    if x['x'] > 999:
        x['x'] = 999

    if x['x'] < -999:
        x['x'] = -999

    if x['y'] > 999:
        x['y'] = 999

    if x['y'] < -999:
        x['y'] = -999


    return x

def check_active_task(x):
    logger2.logger.debug("check_active_task")

    # creature died, there is probably a cleaner way to do this.
    if x == None:
        pass

    # pass if empty
    if x['active_task'] == []:
        return x

    # check active task for completion
    elif x['active_task'][2] >= x['active_task'][3]:
        x['active_task'] = []
        return x
    else: return x


def promote_task_q(x):
    logger2.logger.debug("promote_task_q")

    # creature died, there is probably a cleaner way to do this.
    if x == None:
        pass

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

