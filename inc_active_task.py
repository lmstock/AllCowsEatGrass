
import creature_actions as ca
import logger2
import core

def increment_active_task(s):
    logger2.logger.debug("increment_active_task")

    #if active_task is empty, pass
    if s['active_task'] == []:

        s['active_task'] = ["wander", 3, 1, 1]
        return s


    else:

        if s['active_task'][0] == "sleep":
            result = ca.sleep(s)

        elif s['active_task'][0] == "wander":
            result = ca.wander(s)

        elif s['active_task'][0] == "eat":
            result = ca.eat(s)
        
        elif s['active_task'][0] == "play":
            result = ca.play(s)

        elif s['active_task'][0] == "divide":
            result = ca.divide(s)

        elif s['active_task'][0] == "die":
            result = ca.die(s)

        s = core.check_active_task(result)
        s = core.promote_task_q(s)
        return s

    


