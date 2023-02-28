
import creature_actions as ca
import logthis

def increment_active_task(self):
    logthis.logger.debug("increment_active_task")




    #if active_task is empty, pass
    if self.active_task == []:
        pass


    else:

        if self.active_task[0] == "sleep":
            #sleep(self)
            ca.sleep(self)

        elif self.active_task[0] == "wander":
            ca.wander(self)

        elif self.active_task[0] == "nothing":
            ca.nothing(self)

        elif self.active_task[0] == "eat":
            ca.eat(self)
        
        elif self.active_task[0] == "play":
            ca.play(self)

        elif self.active_task[0] == "observe":
            ca.observe(self)



