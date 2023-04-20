

import copy

x = {"a":0, "b":1}



def change_var(x):
    y = copy.copy(x)
    y.pop("a")
    print(x,y)
    

change_var(x)

print(x)

