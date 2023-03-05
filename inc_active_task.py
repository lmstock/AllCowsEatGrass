
import creature_actions as ca
import archive_tests.logthis as logthis

def increment_active_task(s):
    logthis.logger.debug("increment_active_task")

    active_task = s['active_task']


    #if active_task is empty, pass
    if active_task == []:
        return s


    else:

        if active_task[0] == "sleep":
            result = ca.sleep(s)

        elif active_task[0] == "wander":
            result = ca.wander(s)

        elif active_task[0] == "nothing":
            result = ca.nothing(s)

        elif active_task[0] == "eat":
            result = ca.eat(s)
        
        elif active_task[0] == "play":
            result = ca.play(s)

        elif active_task[0] == "observe":
            result = ca.observe(s)

        return result



