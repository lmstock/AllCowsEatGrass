besttest = ["one", "two", "three"]


bestdict = {
    "one": 1,
    "two": 2
}

emptydict = [1,2]

x = bool(emptydict)


def list_of_things(x):
    if x == 10:
        return
    
    elif x == 12:
        pass

    elif x == 20:
        print(x)


list_of_things(12)
