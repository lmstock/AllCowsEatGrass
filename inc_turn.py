
import logger2


# UPDATE ATTRIBUTES THAT CHANGE EACH TURN
def increment_turn(x):
    logger2.logger.debug("increment_turn")

    # identify creature in logger
    # msg = "\033[32m" + "i am: " + str(x['_id']) + " " + str(x['species_type']) + "\033[0m"
    # logger2.logger.info(msg)

    if x['active_task'] == []:
        x['rest'][0] = round(x['rest'][0] + x['base_fatigue'], 2)
        x['satiety'][0] = round(x['satiety'][0] + x['satiety'][1], 2)
        

    elif x['active_task'][0] != "sleep":
        x['rest'][0] = round(x['rest'][0] + x['base_fatigue'], 2)
        

    elif x['active_task'][0] != "eat":
        x['satiety'][0] = round(x['satiety'][0] + x['satiety'][1], 2)
        
    if x['rest'][0] < 0: x['rest'][0] = 0
    if x['satiety'][0] < 0: x['satiety'][0] = 0
    x['age'] = round(x['age'] + .0000025, 7)


    return x
