import logthis

population = {}
actors = []
waiting_room = []


def scheduler_run():
    logthis.logger.debug("scheduler_run")
    
    for i in actors:
        #print(i.__dict__)

        b = {
            "p": i.creature_id,
            "type": i.type,
            "sze": i.size,
            # "sleep_dur": i.sleep_dur,
            # "mx_nrg": i.max_energy,
            # "r_gain": i.rest_gain,
            # "b_f": i.base_fatigue,
            "nrg": i.energy,
            "tsk_q": i.task_q,
            "actve_tsk": i.active_task,
            "speed": i.speed
        }
        
        print(b)

        # a = str(i.__dict__)
        # logthis.logger.info(a)

        i.action()
        
    
    def empty_waiting_room():
        logthis.logger.debug("empty_waiting_room")
        for i in waiting_room:
            actors.append(i)
        waiting_room.clear()
        
    empty_waiting_room()

