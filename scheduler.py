import logthis

population = {}
actors = []
waiting_room = []


def scheduler_run():
    logthis.logger.debug("scheduler_run")
    
    for i in actors:
        #print(i.__dict__)

        b = {
            "profile": i.creature_id,
            "type": i.type,
            "size": i.size,
            "sleep_dur": i.sleep_dur,
            "max_energy": i.max_energy,
            "rest_gain": i.rest_gain,
            "energy": i.energy,
            "task_q": i.task_q,
            "active_task": i.active_task
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

