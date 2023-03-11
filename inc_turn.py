
import logger2


# UPDATE ATTRIBUTES THAT CHANGE EACH TURN
def increment_turn(s):
    logger2.logger.debug("increment_turn")

    active_task = s['active_task']
    rest = s['rest']
    satiety = s['satiety']
    age = s['age']
    base_fatigue = s['base_fatigue']


    if active_task == []:
        rest[0] = round(rest[0] + base_fatigue, 2)
        satiety[0] = round(satiety[0] + satiety[1], 2)
    
    elif active_task[0] != "sleep":
        rest[0] = round(rest[0] + base_fatigue, 2)

    elif active_task[0] != "eat":
        satiety[0] = round(satiety[0] + satiety[1], 2)
        
    age = round(age + .0000025, 7)

    s['active_task'] = active_task
    s['rest'] = rest
    s['satiety'] = satiety
    s['age'] = age
    s['base_fatigue'] = base_fatigue

    return s
