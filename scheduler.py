import logthis
import flora_species


# creatures
population = {}
actors = []
waiting_room = []

# flora
flora_population = {}
flora_actors = []
green_room = []

def scheduler_run():
    logthis.logger.debug("scheduler_run")
    
    for i in flora_actors:
        #print(i.__dict__)
        i.action()

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
        
        #print(b)
        i.action()



        
    
    def empty_waiting_room():
        logthis.logger.debug("empty_waiting_room")
        for i in waiting_room:
            actors.append(i)
        waiting_room.clear()
        
    empty_waiting_room()

    def empty_green_room():
        logthis.logger.debug("empty_green_room")
        for i in green_room:
            flora_actors.append(i)
        green_room.clear()

    empty_green_room()

