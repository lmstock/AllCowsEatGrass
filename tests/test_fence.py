

a = {'x': 250,'y': 250 }
b = {'x': 1000,'y': 250 }

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


# TEST 1: no fence action required
x = fence(a)
assert x['x'] == 250
assert x['y'] == 250
print("1. pass")

# TEST 2: no fence action required
x = fence(b)
assert x['x'] == 999
assert x['y'] == 250
print("1. pass")