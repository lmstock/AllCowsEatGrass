import random


# reptile POOLS
reptile_sizes = ["tiny", "small", "medium", "large", "very large", "colossal"]
reptile_colors = ["red", "orange", "yellow", "green", "blue", "violet"]
reptile_repr = ["division", "live birth", "egg", "egg", "egg"]
arthorpod_traits = ["shell", "scales", "hairs", "claws", "pincers", "stinger", "mouth parts", "wings"]
reptile_mvmt = ["flight", "walk", "climb", "swim", "run"]
attacks = ["song attack", "tail attack", "bite attack", "claw attack", "squeeze attack"]
reptile_adj1 = ["attractive", "colorful", "creepy", "dangerous", "elegant", "fierce", "gleaming", "homely", "lively"]
reptile_adj2 = ["mysterious", "nervous", "odd", "prickly", "quaint", "sleepy", "tough", "unusual", "vivacious", "wild"]
reptile_mutable_adj = ["well defined", "hidden", "non descript", "tidy", "clearly defined", "ordinary", "exaggerated"]


def gen_reptile():
    print("gen_reptile")

    # ALL reptileS
    new_reptile = {}
    new_reptile["phylum"] = "chordate"
    new_reptile["class"] = "reptile"
    new_reptile["has_exoskeleton"] = True
    new_reptile["has_blood"] = True
    # head, thorax, abdomen = True
    new_reptile["size"] = random.choice(reptile_sizes)
    new_reptile["scales_color"] = random.choice(reptile_colors)
    new_reptile["reproduction"] = random.choice(reptile_repr)
    new_reptile["eyes"] = 2
    new_reptile["legs"] = random.randrange(0, 6, 2)
    new_reptile["adj1"] = random.choice(reptile_adj1)
    new_reptile["adj2"] = random.choice(reptile_adj2)


    # MUTABLE TRAITS
    new_reptile["mutable_traits"] = ["exoskeleton_color", "eyes", "legs", ]


    # RANDOM SELECTIONS
    def random_selections(pool):
        x = len(pool)
        quantity = random.randrange(0, x+1)
        for i in range(1,quantity):
            c = random.choice(pool)
            pool.remove(c)
            new_reptile["mutable_traits"].append(c)
            new_reptile[c] = True

    random_selections(arthorpod_traits)
    random_selections(reptile_mvmt)
    random_selections(attacks)

    x = random.choice(new_reptile["mutable_traits"])
    new_reptile["mutable_desc"] = (x, random.choice(reptile_mutable_adj))


    # MOULTING - PERIODIC SHEDDING of exoskeleton
    tf = ["True", "False"]
    new_reptile["moulting"] = random.choice(tf)

    if new_reptile["moulting"] == True:
        new_reptile["moulting_stats"] = {}
        new_reptile["moulting_stats"]["stages_count"] = random.randrange(0,5)
        new_reptile["moulting_stats"]["stages_interval"] = random.randrange(1, 1000)
        new_reptile["moulting_stats"]["countdown to moulting"] = 0

    # MOULTING - CHANGE IN DEVELOPMENT PHASE



    new_reptile["description"] = [
        "This creature is an {0}.".format(new_reptile["class"]),
        "It is {0} sized and appears to be {1} in color.".format(new_reptile["size"], new_reptile["scales_color"]),
        "It has {0} leg(s) and {1} eye(s)".format(new_reptile["legs"], new_reptile["eyes"]),
        "it appears both {0} and {1} with {2} {3}".format(new_reptile["adj1"], new_reptile["adj2"], new_reptile["mutable_desc"][1], new_reptile["mutable_desc"][0])
    ]

    print("\n")
    for i in new_reptile["description"]:
        print(i)

    return new_reptile

gen_reptile()

