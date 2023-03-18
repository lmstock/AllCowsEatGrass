import random
import pygame

import logger2
import mongotest
import game_conf
import core
import to_color

import game_imgs.flor_imgs as flor_imgs



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
        logger2.logger.info("grow")


        def check_cooldown(f):
            logger2.logger.info("check_cooldown")
            if f['growth_data'][2] > f['growth_data'][3]:
                return True
            else: return False
            
        def growth_roll(f):
            logger2.logger.info("growth_roll")
            roll_check = core.roll(1,100)
            if roll_check > f['growth_data'][1]:
                return True
            else: return False

        def grow(f):
            logger2.logger.debug("grow")

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

            msg = to_color.Colors.fg.blue + str(growth_roll) + " " + str(x) + " " + str(y) + to_color.Colors.reset
            logger2.logger.info(msg) 

            # reset counter
            f['growth_data'][2] = 0

            # count offspring
            if len(f['growth_data']) == 4:
                f.update({'growth_data'[4] : 1})
                logger2.logger.info("offspring")
            else:
                f['growth_data'][4] = f['growth_data'][4] + 1
                logger2.logger.info("no offspring")

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



    



    def update_viewport(f):
        logger2.logger.debug("update_viewport")
        coords = (f['x'],f['y'])
        img_index = int(f['img'])

        x = flor_imgs.flors_list[img_index]
        game_conf.w.game_display.blit(x, coords)
        pygame.display.update()

    f = increment_turn(f)
    f = growth_check(f)

    update_viewport(f)
    mongotest.update_flora_byid(f['_id'], f)
        

def generate_flora(flora_type, x, y):
    logger2.logger.info("generate flora")

    msg = flora_type, x, y
    logger2.logger.info(msg)

    s = mongotest.read_flora_species("flora_species_type", flora_type)

    # iterate through with i
    for i in s:
        print(i)

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
