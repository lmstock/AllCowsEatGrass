import logthis
import random


# creatures

# census data on every creature
population = {}

# list of creatures by creature id
actors = []

# creatures sent here after creation 
# to be added to actors on following turn
waiting_room = []

# flora

# census data on every generated flora
flora_population = {}

# list of flora by flora id
flora_actors = []

# flora sent here after creation
# to be added to flora actors on following turn
green_room = []


# scheduler runs once a turn and sets each actor to their tasks
def scheduler_run():
    logthis.logger.debug("scheduler_run")

    # shuffle lists
    random.shuffle(flora_actors)
    random.shuffle(actors)
    
    for i in flora_actors:
        i.action()

    for i in actors:

        # prints additional self info to terminal
        b = {
            "p": i.creature_id,
            "type": i.type,
            #"sze": i.size,
            #"satiety": i.satiety,
            #"rest": i.rest,
            "tsk_q": i.task_q,
            "actve_tsk": i.active_task,
            "speed": i.speed,
            "fov": i.fov,
            "coords": i.world_coords
        }
        
        #print(b)
        i.action()



    # If newly created creatures are added to the actors list on the same turn as
    # they are created, something bad happened but I dont remember what..
    
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

