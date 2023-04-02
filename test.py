import random



# d = dice, s = sides
def roll(d,s):

    total = 0
    for i in range(d):    
        n = random.randint(1,s)
        total = total + n
    return total

def gen_sleep_habits():
    sleep_roll = roll(10,9)

    sleep_duration = round((sleep_roll/100) * 1000, 2)
    awake_duration = round(1000 - sleep_duration, 2)

    fully_rested = roll(5,15) * 10   # 5d20 * 10 for full energy (5, 500)
    rest_gain = round(fully_rested/sleep_duration, 2)
    base_fatigue = round((fully_rested/awake_duration) * -1, 2)
    return sleep_duration, fully_rested, rest_gain, base_fatigue

s = gen_sleep_habits()
print (s)