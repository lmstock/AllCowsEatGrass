import random

import logger2
import mongotest
import game_conf
import core
import to_color



# checks on what the individual is doing each turn
def flora_action(f):
    logger2.logger.debug("flora_action")

    def increment_turn(f):
        logger2.logger.debug("increment_turn")

        # update attributes that change each turn
        f['age'] = round(f['age'] + .01, 2)
        f['growth_data'][2] = f['growth_data'][2] + 1
        return f


    def growth_check(f):
        logger2.logger.debug("grow")

        def check_cooldown(f):
            logger2.logger.debug("check_cooldown")
            if f['growth_data'][2] > f['growth_data'][3]:
                logger2.logger.debug("passed cool down")
                return True
            else: 
                logger2.logger.debug("failed cool down")

                # increment cool down
                f['growth_data'][2] = f['growth_data'][2] + 1
                return False
            
        def growth_roll(f):
            logger2.logger.debug("growth_roll")
            roll_check =  core.roll(1,100)

            if roll_check > f['growth_data'][1]:
                return True
            else:
                return False

        def grow(f):
            logger2.logger.debug("grow")

            # check for duplicate species at that location
            def check_for_duplicate(species,x,y):
                msg = str(x) + " " + str(y) + " check for duplicate"
                logger2.logger.info(msg)

                # db function
                cursor = mongotest.check_for_dup(species, x, y)
                for i in cursor:
                    if i['x'] == x and i['y'] == y:
                        msg = to_color.Colors.fg.blue + "duplicate true" + to_color.Colors.reset
                        logger2.logger.info(msg)
                        return True
                    else:
                        
                        logger2.logger.info("duplicate false")
                        return False

            x = f['x']
            y = f['y']
            dist = f['growth_data'][0]

            dirs = ["w", "n", "e", "s"]
            c = random.choice(dirs)

            if c == "w":
                x = x - dist
            if c == "e":
                x = x + dist
            if c == "n":
                y = y + dist
            else: # s
                y = y - dist

            msg = to_color.Colors.fg.blue + str(dist) + " " + str(x) + " " + str(y) + to_color.Colors.reset
            logger2.logger.debug(msg) 

            # reset counter
            f['growth_data'][2] = 0

            # count offspring
            if 'offspring' not in f: 
                f['offspring'] = 1

            else:
                f['offspring'] = f['offspring'] + 1

            if check_for_duplicate(f['flora_species_type'],x,y) == True:
                pass
            else:
                generate_flora(f['flora_species_type'], x, y)


            return f


        # check cooldown
        x = check_cooldown(f)
        if x == False:
            return (f)
        else: pass

        # check growth_roll
        y = growth_roll(f)
        if y == False:
            return (f)
        else: pass
        
        f = grow(f)
        return f



    





    f = increment_turn(f)
    f = growth_check(f)


    mongotest.update_flora_byid(f['_id'], f)
        
# always print flora gen to terminal
def generate_flora(flora_type, x, y):
    logger2.logger.info("generate flora")

    s = mongotest.read_flora_species("flora_species_type", flora_type)

    # iterate through with i
    for i in s:
        print(to_color.Colors.fg.green, i, to_color.Colors.reset)

    # add to db
    new_flora = {
        "flora_species_type": i["flora_species_type"],
        "size": i["size"],
        "flora_type": i["flora_type"],
        "energy": i["energy"],
        "growth_data": i["growth_data"],   
        "x": x,
        "y": y,
        "age": 0,
        "img": i['img']
    }

    logger2.logger.debug(str(new_flora))
    mongotest.add_flora(new_flora)


def get_random_flora_type():
    logger2.logger.debug("get_random_flora_type")
    return random.choice(mongotest.list_flora())

def generate_random_flora():
    logger2.logger.info("generate_random_flora")

    x = core.roll(1,500)
    y = core.roll(1,500)

    t = get_random_flora_type()
    print(t,x,y)
    generate_flora(t,x,y)
