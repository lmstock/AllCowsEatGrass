import logthis

population = {}
actors = []
waiting_room = []


def scheduler_run():
    logthis.logger.debug("scheduler_run")
    
    for i in actors:
        a = str(i.__dict__)
        logthis.logger.info(a)
        i.action()
        
    
    def empty_waiting_room():
        logthis.logger.debug("empty_waiting_room")
        for i in waiting_room:
            actors.append(i)
        waiting_room.clear()
        
    empty_waiting_room()

