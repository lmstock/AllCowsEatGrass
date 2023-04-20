import random, copy
import logger2, bartokmongo, core


def reset_parent_after_repr(p):
    # reset parent cooldown before division
    p['repr_cooldown'][0] = 0

    # clear parent active task
    p['active_task'] = []  

    # increment parent offspring count
    if 'offspring' not in p: 
        p['offspring'] = 1

    else:
        p['offspring'] = p['offspring'] + 1

    return p


def gen_child_from_parent(p):
    logger2.logger.debug("gen_child_from_parent")

    # copy parent to child
    parent_id = p['_id']
    child = bartokmongo.read_creature_parent(parent_id)

    # reset attribute for child
    child.pop("_id")
    child['age'] = 0
    child['task_q'] = []
    child['active_task'] = []
    child['offspring'] = 0

    return child


def gen_mutation():
    # gen mutation - 
    # mutation 5-20% more or less
    mutables = ['sleep_dur', 'rest_gain', 'rest', 'satiety', 'energy', 'hostility', 'health', 'speed', 'fov', 'repr_cooldown']
    direction = ['loss', 'gain']
    amount = random.randrange(5,20)

    m = random.choice(mutables)
    d = random.choice(direction)
    mutation = [m, d, amount]

    return mutation


def apply_mutation_to_child(child, mutation, new_species_name):
    # APPLY  MUTATION TO CHILD
    child['species_type'] = new_species_name

    m = mutation[0]
    d = mutation[1]
    amount = mutation[2]

    if m == 'rest':
        a = round(child['rest'][2] * amount * .01)
        if d == 'loss':
            child[m][2] = child[m][2] - a
        else:
            child[m][2] = child[m][2] + a

    elif m == 'satiety':
        a = round(child['satiety'][2] * amount * .01)
        if d == 'loss':
            child[m][2] = child[m][2] - a
        else:
            child[m][2] = child[m][2] + a

    elif m == 'energy':
        a = round(child['energy'][1] * amount * .01)
        if d == 'loss':
            child[m][1] = child[m][1] - a
        else:
            child[m][1] = child[m][1] + a

    elif m == 'hostility':
        a = round(child['hostility'][1] * amount * .01)
        if d == 'loss':
            child[m][1] = child[m][1] - a
        else:
            child[m][1] = child[m][1] + a
    
    elif m == 'health':
        a = round(child['health'][1] * amount * .01)
        if d == 'loss':
            child[m][1] = child[m][1] - a
        else:
            child[m][1] = child[m][1] + a

    elif m == 'speed':
        a = round(child['speed'] * amount * .01)
        if d == 'loss':
            child[m] = child[m] - a
        else:
            child[m] = child[m] + a

    elif m == 'fov':
        a = round(child['fov'] * amount * .01)
        if d == 'loss':
            child[m] = child[m] - a
        else:
            child[m] = child[m] + a

    elif m == 'sleep_duration':
        a = round(child['sleep_duration'] * amount * .01)
        if d == 'loss':
            child[m] = child[m] - a
        else:
            child[m] = child[m] + a
    
    elif m == 'rest_gain':
        a = round(child['rest_gain'] * amount * .01)
        if d == 'loss':
            child[m] = child[m] - a
        else:
            child[m] = child[m] + a

    elif m == 'repr_cooldown':
        a = round(child['repr_cooldown'][1] * amount * .01)
        if d == 'loss':
            child[m][1] = child[m][1] - a
        else:
            child[m][1] = child[m][1] + a

    return child


def new_species_name(p):
    species_type = p['species_type']
    species = bartokmongo.read_creature_species_du("species_type", species_type)
    count = species['mutation_count']
    nsn = core.whatsmyname(species_type,count)
    return nsn


def add_species_to_bestiary(c):

    new_bestiary_entry = copy.copy(c)
    new_bestiary_entry['mutation_count'] = 0
    new_bestiary_entry.pop('target')
    new_bestiary_entry.pop('local_crets')
    new_bestiary_entry.pop('knowledge_base')
    new_bestiary_entry.pop('is_alive')
    new_bestiary_entry.pop('age')
    new_bestiary_entry.pop('task_q')
    new_bestiary_entry.pop('active_task')
    new_bestiary_entry.pop('offspring')

    new_name = new_bestiary_entry['species_type']
    announcement = '\033[34m' + str(new_name) + ',  A new species has evolved! \033[0m'
    logger2.logger.info(announcement)

    bartokmongo.add_creature_species(new_bestiary_entry)


def update_mutation_count(p):
    # increment mutation count of parent species
    sp = p['species_type']
    species = bartokmongo.read_creature_species_du('species_type',sp)

    ct = species['mutation_count'] = species['mutation_count'] + 1
    update =  {"$set": {"mutation_count": ct}}
    bartokmongo.update_species_by_name(species, update)




# creates a creature from parent through "creature division" - p = parent
def divide(p):
    logger2.logger.debug("divide")

    p = reset_parent_after_repr(p)
    c = gen_child_from_parent(p)

    # check for mutation
    mutation_check = core.roll(1,10)
    
    species_name = ""

    if mutation_check == 5:
        logger2.logger.debug("mutation check passed")
        
        # mutate species
        m = gen_mutation()
        nsn = new_species_name(p)
        c = apply_mutation_to_child(c,m,nsn)
        add_species_to_bestiary(c)
        update_mutation_count(p)
        species_name = nsn
        
    else:
        species_name = p['species_type']

    bartokmongo.add_creature(c)
    announcement = '\033[32m' + str(species_name) + ',  A new creature is born! \033[0m'
    logger2.logger.info(announcement)
    return p

