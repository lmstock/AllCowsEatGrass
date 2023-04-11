import random
import core
import logger2
import mongotest
import creature



def sleep(x):
    logger2.logger.debug("sleep")

    # increment active_task
    x = core.incr_active_task(x)

    # increase current_rest
    x['rest'][0] = round(x['rest'][0] + x['rest_gain'], 2)

    # do not exceed max_rest remove from active task if full
    if x['rest'][0] >= x['rest'][2]:
        x['rest'][0] = x['rest'][2]

        # clear active_task
        x['active_task'] = []

    return x


def eat(x):
    logger2.logger.debug("eat")

    # increment active_task
    x = core.incr_active_task(x)

    # increase satiety
    x['satiety'][0] = round(x['satiety'][0] + 33, 2)  

    # do not exceed max_rest remove from active task if full
    if x['satiety'][0] >= x['satiety'][2]:
        x['satiety'][0] = x['satiety'][2]

        # clear active task
        x['active_task'] = []
    
    return x


def wander(x):
    logger2.logger.debug("wander")

    # increment active_task
    x = core.incr_active_task(x)
    speed = x['speed']

    dirs = ["w", "nw", "ne", "e","se", "s", "sw"]
    c = random.choice(dirs)
    
    if c == "w": x['x'] = x['x'] - speed

    elif c == "nw": 
        x['x'] = x['x'] - speed
        x['y'] = x['y'] + speed
        
    elif c == "n": x['y'] = x['y'] + speed
    
    elif c == "ne":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] + speed

    elif c == "e": x['x'] = x['x'] + speed
    
    elif c == "se":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] - speed

    elif c == "s": x['y'] = x['y'] - speed  # s

    else:   #sw
        x['x'] = x['x'] - speed
        x['y'] = x['y'] - speed

    x = core.fence(x)
    
    return x
     

# NEEDS INVENTED, WRITTEN, AND TEST WRITTEN
def investigate(x):
    # knowledge gathering
    logger2.logger.debug("investigate")

    # increment active_task
    x = core.incr_active_task(x)

    return x


# WANDER FASTER
def play(x):

    # increment active_task
    x = core.incr_active_task(x)

    speed = x['speed'] * 1.5

    dirs = ["w", "nw", "ne", "e","se", "s", "sw"]
    c = random.choice(dirs)
    
    if c == "w": x['x'] = x['x'] - speed

    elif c == "nw": 
        x['x'] = x['x'] - speed
        x['y'] = x['y'] + speed
        
    elif c == "n": x['y'] = x['y'] + speed
    
    elif c == "ne":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] + speed

    elif c == "e": x['x'] = x['x'] + speed
    
    elif c == "se":
        x['x'] = x['x'] + speed
        x['y'] = x['y'] - speed

    elif c == "s": x['y'] = x['y'] - speed  # s

    else:   #sw
        x['x'] = x['x'] - speed
        x['y'] = x['y'] - speed

    x = core.fence(x)
    return x


def die(x):
    # health runs out
    logger2.logger.debug("die")
    msg = " \033[31ma creature " + str(x['_id']) + " has passed from this mortal plane\033[0m"
    logger2.logger.info(msg)

    x['is_alive'] = False
    mongotest.remove_individual_byid(x["_id"])
    mongotest.add_to_mortuary(x)
    return x
    

# creates a creature from parent through "creature division"
# x = parent
def divide(p):
    logger2.logger.debug("divide")

    # reset cooldown before division
    p['repr_cooldown'][0] = 0

    # clear active task
    p['active_task'] = []  

    # count offspring
    if 'offspring' not in p: 
        p['offspring'] = 1

    else:
        p['offspring'] = p['offspring'] + 1

    parent_species_type = p['species_type']


    def mutate(x):
        # gen mutation - 
        # mutation 5-20% more or less
        mutables = ['sleep_dur', 'rest_gain', 'rest', 'satiety', 'energy', 'hostility', 'health', 'speed', 'fov', 'repr_cooldown']
        direction = ['loss', 'gain']
        amount = random.randrange(5,20)

        m = random.choice(mutables)
        d = random.choice(direction)

        # pull parent species from bestiary
        parent_species_type = x['species_type']
        s = mongotest.read_creature_species_du('species_type', parent_species_type)


        # create mutation and add to bestiary
        def add_mutated_species_to_bestiary(x, m, d, amount):
            logger2.logger.debug("add_mutation_to_bestiary")

            # setup new species
            new_species = {
                "species_type": x['species_type'],
                "head": x['head'],
                "size": x['size'],
                "body_type": x['body_type'],

                "rest": x['rest'],
                "sleep_duration": x['sleep_duration'],
                "rest_gain": x['rest_gain'],

                "satiety": x['satiety'],
                "hostility": x['hostility'],
                "health": x['health'],
                "energy": x['energy'],

                "speed": x['speed'],
                "fov": x['fov'],
                'mutation_count': 0,
                "repr_cooldown": [0, 100]
            }

            # get count for naming scheme below
            original_mutation_count = x['mutation_count']

            # increment mutation count of parent
            ct = x['mutation_count'] = x['mutation_count'] + 1
            update =  {"$set": {"mutation_count": ct}}
            mongotest.update_species_by_name(parent_species_type, update)

            # update new species name
            name = x['species_type']
            my_new_species_name = core.whatsmyname(name, original_mutation_count)
            new_species['species_type'] = my_new_species_name

            # APPLY  MUTATION TO NEW SPECIES
            if m == 'rest':
                a = round(p['rest'][2] * amount * .01)
                if d == 'loss':
                    new_species[m][2] = new_species[m][2] - a
                else:
                    new_species[m][2] = new_species[m][2] + a

            elif m == 'satiety':
                a = round(p['satiety'][2] * amount * .01)
                if d == 'loss':
                    new_species[m][2] = new_species[m][2] - a
                else:
                    new_species[m][2] = new_species[m][2] + a

            elif m == 'energy':
                a = round(p['energy'][1] * amount * .01)
                if d == 'loss':
                    new_species[m][1] = new_species[m][1] - a
                else:
                    new_species[m][1] = new_species[m][1] + a

            elif m == 'hostility':
                a = round(p['hostility'][1] * amount * .01)
                if d == 'loss':
                    new_species[m][1] = new_species[m][1] - a
                else:
                    new_species[m][1] = new_species[m][1] + a
            
            elif m == 'health':
                a = round(p['health'][1] * amount * .01)
                if d == 'loss':
                    new_species[m][1] = new_species[m][1] - a
                else:
                    new_species[m][1] = new_species[m][1] + a

            elif m == 'speed':
                a = round(p['speed'] * amount * .01)
                if d == 'loss':
                    new_species[m] = new_species[m] - a
                else:
                    new_species[m] = new_species[m] + a

            elif m == 'fov':
                a = round(p['fov'] * amount * .01)
                if d == 'loss':
                    new_species[m] = new_species[m] - a
                else:
                    new_species[m] = new_species[m] + a

            elif m == 'sleep_duration':
                a = round(p['sleep_duration'] * amount * .01)
                if d == 'loss':
                    new_species[m] = new_species[m] - a
                else:
                    new_species[m] = new_species[m] + a
            
            elif m == 'rest_gain':
                a = round(p['rest_gain'] * amount * .01)
                if d == 'loss':
                    new_species[m] = new_species[m] - a
                else:
                    new_species[m] = new_species[m] + a

            elif m == 'repr_cooldown':
                a = round(p['repr_cooldown'][1] * amount * .01)
                if d == 'loss':
                    new_species[m][1] = new_species[m][1] - a
                else:
                    new_species[m][1] = new_species[m][1] + a

            mongotest.add_creature_species(new_species)
            announcement = '\033[34m' + str(my_new_species_name) + ',  A new species has evolved! \033[0m'
            logger2.logger.info(announcement)
            return new_species['species_type']

        # this returns the type for creature gen below
        new_species_name = add_mutated_species_to_bestiary(s, m, d, amount)
    
        return new_species_name
    

    
    
    
    mutation_check = core.roll(1,10)
    
    if mutation_check == 5:
        # mutate species
        species_type = mutate(p)


    else:
        # gen offspring from parentf
        species_type = parent_species_type


    # gen creature from new species
    creature.generate_creature(species_type)
    
    announcement = '\033[32m' + str(species_type) + ',  A new creature is born! \033[0m'
    logger2.logger.info(announcement)

    return p

    