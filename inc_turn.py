
import logthis


# UPDATE ATTRIBUTES THAT CHANGE EACH TURN
def increment_turn(s):
    logthis.logger.debug("increment_turn")

    
    if s.active_task == []:
        pass
    
    else:
        if s.active_task[0] != "sleep":
            s.rest[0] = round(s.rest[0] + s.base_fatigue, 2)

        if s.active_task[0] != "eat":
            s.satiety[0] = round(s.satiety[0] + s.satiety[1], 2)
        
        s.age = round(s.age + .0000025, 7)
