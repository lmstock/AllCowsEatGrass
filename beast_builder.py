import random
from arthropod_gen import gen_arthropod
from mammal_gen import gen_mammal
from birds_gen import gen_bird


phylum_types = ["arthropod", "chordata"]   # mollusk

chordata_class = ["mammals", "birds", "reptiles"]  # fish amphibians 

# texture colors


def random_creature_gen():
    x = random.choice(phylum_types)

    if x == "arthropod":
        new_creature = gen_arthropod()
        return new_creature

    elif x == "chordata":
        x = random.choice(chordata_class)

        if x == "mammals":
            new_creature = gen_mammal()
            return new_creature
        
        if x == "birds":
            new_creature = gen_bird()
            return new_creature
        
        if x == "reptiles":
            new_creature = gen_bird()
            return new_creature
        
    return new_creature


#random_creature_gen()






'''
i like this group of major phylum: https://en.wikipedia.org/wiki/Animal

'''