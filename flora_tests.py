import logger2
import to_color

import random


f = {'_id': 'ObjectId("64132eac6c873b6508b44391")', 'flora_species_type': 'azne', 'size': 'very_large', 'flora_type': 'pterido', 'energy': 100, 'growth_data': [4, 38, 0, 2452], 'x': 45, 'y': 347, 'age': 0.05, 'img': 28}

print(f)

# d = dice, s = sides
def roll(d,s):
    logger2.logger.debug("roll")
    total = 0
    for i in range(d):  
        print(i)  
        n = random.randint(1,s)
        total = total + n
    print(total)
    return total


def growth_check(f):
    logger2.logger.info("grow")
    print("growth data: ", f['growth_data'])

    def check_cooldown(f):
        logger2.logger.info("check_cooldown")
        if f['growth_data'][2] > f['growth_data'][3]:
            logger2.logger.info("passed cool down")
            return True
        else: 
            logger2.logger.info("failed cool down")

            # increment cool down
            f['growth_data'][2] = f['growth_data'][2] + 1
            return False
            
        
    def growth_roll(f):
        logger2.logger.info("growth_roll")
        roll_check = roll(1,100)
        print(" is ", roll_check, " > ", f['growth_data'][1], " ?")
        if roll_check > f['growth_data'][1]:
            logger2.logger.info("passed growth roll")
            return True
        else:
            logger2.logger.info("failed growth roll")
            return False


    def grow(f):
        logger2.logger.info("grow")

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

        msg = to_color.Colors.fg.blue + str(x) + str(y) + str(dist) + " " + str(x) + " " + str(y) + to_color.Colors.reset
        logger2.logger.info(msg) 

        # reset counter
        f['growth_data'][2] = 0


        print(to_color.Colors.fg.blue + "GEN NEW CRET" + to_color.Colors.reset)

        return f

###  YOU DO NOT WANT TO RETURN HERE ###
    # check cooldown
    x = check_cooldown(f)
    if x == False:
        return f

    y = check_cooldown(f)
    if y == False:
        return f
    
    f = grow(f)
    return f

growth_check(f)
print(f)