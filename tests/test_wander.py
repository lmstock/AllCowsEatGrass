import random


a = {
     'speed': 460.0,
     'x': 0,
     'y': 0,
     'active_task': ['play', 3, 4, 6],
     }

b = {
     'speed': 460.0,
     'x': 590,
     'y': -590,
     'active_task': ['play', 3, 4, 6],
     }

c = {
     'speed': 460.0,
     'x': 13,
     'y': 1005,
     'active_task': ['play', 3, 4, 6],
     }

d = {
     'speed': 460.0,
     'x': 590,
     'y': -1590,
     'active_task': ['play', 3, 4, 6],
     }

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



def wander(x):

    # increment active_task
    x = incr_active_task(x)
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

    x = fence(x)
    return x


# TEST 1: increment turn
x = wander(a)
assert x['active_task'][2] == 5
print("1. pass")

# TEST 2: inside fence, no change
x = wander(b)
assert x['x'] < 1000
assert x['x'] > -1000
assert x['y'] < 1000
assert x['y'] > -1000
print("2. pass")

# TEST 3: outside of north fence
x = wander(c)
assert x['x'] < 1000
assert x['x'] > -1000
assert x['y'] < 1000
assert x['y'] > -1000
print("2. pass")

# TEST 3: outside of west fence
x = wander(d)
assert x['x'] < 1000
assert x['x'] > -1000
assert x['y'] < 1000
assert x['y'] > -1000
print("2. pass")