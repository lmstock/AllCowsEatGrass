import random


# bird POOLS
bird_sizes = ["tiny", "small", "medium", "large", "very large", "mega"]
bird_colors = ["red", "orange", "yellow", "green", "blue", "violet"]
bird_repr = ["division", "live birth", "egg", "egg", "egg"]
bird_traits = ["feathers", "fingers", "talons", "beak", "wings"]
bird_mvmt = ["flight", "walk", "climb", "swim", "run"]
attacks = ["song attack", "peck attack", "bite attack", "talon attack"]
bird_adj1 = ["attractive", "colorful", "creepy", "dangerous", "elegant", "fierce", "gleaming", "homely", "lively"]
bird_adj2 = ["mysterious", "nervous", "odd", "prickly", "quaint", "sleepy", "tough", "unusual", "vivacious", "wild"]
bird_mutable_adj = ["well defined", "hidden", "non descript", "tidy", "clearly defined", "ordinary"]


def gen_bird():
    print("gen_bird")

    # ALL birdS
    new_bird = {}
    new_bird["phylum"] = "chordate"
    new_bird["class"] = "bird"
    new_bird["has_blood"] = True
    # head, thorax, abdomen = True
    new_bird["size"] = random.choice(bird_sizes)
    new_bird["feather_color"] = random.choice(bird_colors)
    new_bird["reproduction"] = random.choice(bird_repr)
    new_bird["eyes"] = 2
    new_bird["legs"] = 2
    new_bird["adj1"] = random.choice(bird_adj1)
    new_bird["adj2"] = random.choice(bird_adj2)


    # MUTABLE TRAITS
    new_bird["mutable_traits"] = ["exoskeleton_color", "eyes", "legs", ]


    # RANDOM SELECTIONS
    def random_selections(pool):
        x = len(pool)
        quantity = random.randrange(0, x+1)
        for i in range(1,quantity):
            c = random.choice(pool)
            pool.remove(c)
            new_bird["mutable_traits"].append(c)
            new_bird[c] = True

    random_selections(bird_traits)
    random_selections(bird_mvmt)
    random_selections(attacks)

    x = random.choice(new_bird["mutable_traits"])
    new_bird["mutable_desc"] = (x, random.choice(bird_mutable_adj))


    # MOULTING - PERIODIC SHEDDING of exoskeleton
    tf = ["True", "False"]
    new_bird["moulting"] = random.choice(tf)
    new_bird["has_exoskeleton"] = random.choice(tf)


    if new_bird["moulting"] == True:
        new_bird["moulting_stats"] = {}
        new_bird["moulting_stats"]["stages_count"] = random.randrange(0,5)
        new_bird["moulting_stats"]["stages_interval"] = random.randrange(1, 1000)
        new_bird["moulting_stats"]["countdown to moulting"] = 0


    # MOULTING - CHANGE IN DEVELOPMENT PHASE



    new_bird["description"] = [
        "This creature is an {0}.".format(new_bird["class"]),
        "It is {0} sized and appears to be {1} in color.".format(new_bird["size"], new_bird["feather_color"]),
        "It has {0} leg(s) and {1} eye(s)".format(new_bird["legs"], new_bird["eyes"]),
        "it appears both {0} and {1} with {2} {3}".format(new_bird["adj1"], new_bird["adj2"], new_bird["mutable_desc"][1], new_bird["mutable_desc"][0])
    ]

    print("\n")
    for i in new_bird["description"]:
        print(i)

    return new_bird

#gen_bird()

