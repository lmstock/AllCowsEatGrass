import logthis

population = {}
actors = []
waiting_room = []


def scheduler_run():
    logthis.logger.info("scheduler_run")
    
    for i in actors:
        print("scheduled actor: ", i)
        i.action()
        
    
    def empty_waiting_room():
        for i in waiting_room:
            print("actor in waiting room: ", i)
            actors.append(i)
        waiting_room.clear()
        
    empty_waiting_room()

