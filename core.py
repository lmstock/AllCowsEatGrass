import random
import logger2, bartokmongo



# d = dice, s = sides
def roll(d,s):
    logger2.logger.debug("roll")
    total = 0
    for i in range(d):    
        n = random.randint(1,s)
        total = total + n
    return total


def incr_active_task(x):
    x['active_task'][2] = x['active_task'][2] + 1
    return x

def fence(x):
    if x['x'] > 999:
        x['x'] = 999

    if x['x'] < -999:
        x['x'] = -999

    if x['y'] > 999:
        x['y'] = 999

    if x['y'] < -999:
        x['y'] = -999

    return x

def check_active_task(x):
    logger2.logger.debug("check_active_task")

    # creature died, there is probably a cleaner way to do this.
    if x == None:
        pass

    # pass if empty
    if x['active_task'] == []:
        return x

    # check active task for completion
    if x['active_task'][2] >= x['active_task'][3]:
        x['active_task'] = []
        return x
    else: return x


def promote_task_q(x):
    logger2.logger.debug("promote_task_q")

    # creature died, there is probably a cleaner way to do this.
    if x == None:
        pass

    if x['active_task'] == []:

        p1,p2,p3 = [],[],[]

        for i in x['task_q']:
            if i[1] == 1: p1.append(i)
            elif i[1] == 2: p2.append(i)
            else: p3.append(i)


        if p1 != []: t = random.choice(p1)
        elif p2 != []: t = random.choice(p2)
        elif p3 != []: t = random.choice(p3)
        else: 
            t = ["wander", 3, 0, 3]

        x['active_task'] = t

        try:
            x['task_q'].remove(t)
        except Exception as e:
            pass

    return x


def whatsmyname(name, mutation_count):
    # will get us to 676 variants from a single species. there is no reason to proceed past that
            
    def nbr_to_ltr(n):
        alphamap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                    'g': 7, 'h': 8, 'i':9, 'j':10, 'k':11, 'l':12,
                    'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 
                    's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24,
                    'y':25, 'z':26 }
        
        for k,v in alphamap.items():
            if v == n:
                return k
            
    if mutation_count == 0:
        mutation_name = name + ".a"
        return mutation_name

    elif mutation_count > 0 and mutation_count < 26:

        # increment ct and change to letter
        n = mutation_count + 1
        n = nbr_to_ltr(n)

        mutation_name = name + "." + n
    
        return mutation_name
    
    elif mutation_count >= 26:
        s = int(mutation_count/26)
        s = nbr_to_ltr(s)

        n = mutation_count % 26
        if n == 0:
            n = str(0)
        else:
            n = nbr_to_ltr(n)

        mutation_name = name + "." + s + n
        return mutation_name






