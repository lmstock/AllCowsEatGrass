import random

import logger2
import game_conf


# checks active task for empty or completion
def check_active_task(s):
    logger2.logger.debug("check_active_task")
    

    active_task = s['active_task']
    task_q = s['task_q']



    if active_task == []:

        # if no active task, get one
        def get_new_task(s):
            logger2.logger.debug("get_new_task")

            duration = random.randint(1,8)

            p1,p2,p3 = [],[],[]

            for i in task_q:
                if i[1] == 1: p1.append(i)
                elif i[1] == 2: p2.append(i)
                else: p3.append(i)

            if p1 != []: x = random.choice(p1)
            elif p2 != []: x = random.choice(p2)
            elif p3 != []: x = random.choice(p3)
            else: 
                if game_conf.w.current_tick % 2 == 0:
                    x = ["wander", 3, 0, duration]
                else: x = ["play", 3, 0, duration]
            try:
                task_q.remove(x)
            except Exception as e:
                pass

            return x

        active_task = get_new_task(s)

    elif active_task[2] == active_task[3]:
        active_task = []


    s['active_task'] = active_task
    s['task_q'] = task_q

    return s
                

