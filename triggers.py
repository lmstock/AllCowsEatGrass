
import random
import logthis
import scheduler


def trigger_tasks(s):
    logthis.logger.debug("trigger_tasks")

    # check for interrupt
    if s.interrupt == True:
        pass
    # SLEEP TRIGGER
    def check_current_rest():

        if s.active_task == []:
            pass
    
        elif s.active_task[0] == "sleep":
            return


        # less than 40% 
        if s.rest[0] < s.rest[1] * .4:
        
            # remove old sleep tasks from task_q if present
            def remove_old_sleeps():
                logthis.logger.debug("remove_old_sleeps")

                if s.task_q == []:
                    return

                else:
                    for i in s.task_q:
                        if i[0] == "sleep":
                            s.task_q.remove(i)

            remove_old_sleeps()

            # add sleep task - [task, priority, current turn, max turn]
            if s.rest[0] < s.rest[1] * .1:   # <10%
                sleep = ["sleep", 1, 0, s.sleep_dur]

            elif s.rest[0] < s.rest[1] * .3:   # <30%
                sleep = ["sleep", 2, 0, s.sleep_dur]

            elif s.rest[0] < s.rest[1] * .4:   # <40%
                sleep = ["sleep", 3, 0, s.sleep_dur]

            s.task_q.append(sleep)   
    check_current_rest()

    # EAT TRIGGER
    def check_current_satiety():

        if s.active_task == []:
            pass
        
        else:
            if s.active_task[0] == "eat":
                pass

            else:
                # if satiety less than 40%
                if s.satiety[0] < s.satiety[1] * .4:
                    
                    # remove old eat tasks from task_q if present
                    def remove_old_eats():
                        logthis.logger.debug("remove_old_eats")

                        if s.task_q == []:
                            pass

                        else:
                            for i in s.task_q:
                                if i[0] == "eat":
                                    s.task_q.remove(i)

                    remove_old_eats()

                    # add eat task - [task, priority, current turn, max turn]
                    if s.satiety[0] < s.satiety[1] * .1:   # <10%
                        eat = ["eat", 1, 0, 6]

                    elif s.satiety[0] < s.satiety[1] * .3:   # <30%
                        eat = ["eat", 2, 0, 6]

                    elif s.satiety[0] < s.satiety[1] * .4:   # <40%
                        eat = ["eat", 3, 0, 6]

                    s.task_q.append(eat) 

                # if satiety is not less than 40%    
                else: pass
    check_current_satiety()

    # FIELD OF VIEW CHECK
    def check_fov():

        logthis.logger.debug("check_fov")

        # chance to check fov
        #if s.salt[0] < 5:

        # locals list
        local_crets = []

        # get fov   
        x_range = s.world_coords[0] - 1000, s.world_coords[0] + 1000
        y_range = s.world_coords[1] - 1000, s.world_coords[1] + 1000
        fov = (x_range, y_range)

        # check for local_crets
        for i in scheduler.population.items():

            # is creature in population x coord in x range of active entity?
            if i[1]['world_coords'][0] in range(fov[0][0], fov[0][1]):
                msg = (i[1]['creature_id'], " - ", i[1]['world_coords'][0], " is in range ", fov[0][0], " - ", fov[0][1])
                logthis.logger.debug(msg)

                # is creature in population y coord in y range of active entity?
                if i[1]['world_coords'][1] in range(fov[1][0], fov[1][1]):
                    msg = i[1]['creature_id'], " - ", i[1]['world_coords'][1], "is in range ", fov[1][0], " - ", fov[1][1]
                    logthis.logger.debug(msg)

                    local_crets.append(i[1]['creature_id'])

                else: msg = i[1]['creature_id'], " - ", i[1]['world_coords'][1], "NOT in range ", fov[1][0], " - ", fov[1][1]
                logthis.logger.debug(msg)

            else: msg = i[1]['creature_id'], " - ", i[1]['world_coords'][0], " NOT in range ", fov[0][0], " - ", fov[0][1]
            logthis.logger.debug(msg)

        msg = s.creature_id ,":  LOCALS: ", local_crets
        logthis.logger.debug(msg)
        return local_crets
    local_crets = check_fov() # returns a list of creatures in fov by creature_id

    # check knowledge base - returns a creature from fov
    def check_kb(local_crets):
        logthis.logger.debug("check_kb")

        if local_crets == False:
            pass
        else:
            x = random.choice(local_crets)
            return x

    x = check_kb(local_crets)
    #s.active_task = "observe"

