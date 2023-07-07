import random

#

#  MAMMAL POOLS
mammal_sizes = ["tiny", "small", "medium", "large", "very large", "colossal"]
mammal_colors = ["red", "orange", "yellow", "green", "blue", "violet"]
mammal_eyes_ct = [1, 2, 2, 2, 3]
mammal_repr = ["live birth", "live birth", "live birth", "division", "egg"]
mammal_traits = ["hooves", "tail", "hairs", "claws", "whiskers", "sharp teeth", "mane", "wings", "fingers"]
mammal_mvmt = ["flight", "walk", "climb", "swim", "run"]
attacks = ["song attack", "wrestle attack", "bite attack", "claw attack"]
mammal_adj1 = ["beautiful", "clean", "fancy", "handsome", "elegant", "fierce", "gleaming", "homely", "lively"]
mammal_adj2 = ["mysterious", "nervous", "odd", "prickly", "quaint", "scruffy", "tough", "unkempt", "vivacious", "wild"]
mammal_mutable_adj = ["well defined", "hidden", "non descript", "tidy", "clearly defined", "ordinary", "outrageous"]


def gen_mammal():
    print("gen_mammal")

    # ALL MAMMALS
    new_mammal = {}
    new_mammal["phylum"] = "chordate"
    new_mammal["class"] = "mammal"
    new_mammal["has_blood"] = True
    new_mammal["has_fur"] = True
    new_mammal["fur_color"] = random.choice(mammal_colors)
    new_mammal["legs"] = random.randrange(0,6,2)
    new_mammal["eyes"] = random.choice(mammal_eyes_ct)
    new_mammal["size"] = random.choice(mammal_sizes)
    new_mammal["adj1"] = random.choice(mammal_adj1)
    new_mammal["adj2"] = random.choice(mammal_adj2)

    # MUTABLE TRAITS
    new_mammal["mutable_traits"] = ["fur_color"]


    # RANDOM SELECTIONS
    def random_selections(pool):
        x = len(pool)
        quantity = random.randrange(0, x+1)
        for i in range(1,quantity):
            c = random.choice(pool)
            pool.remove(c)
            new_mammal["mutable_traits"].append(c)
            new_mammal[c] = True

    random_selections(mammal_traits)
    random_selections(mammal_mvmt)
    random_selections(attacks)

    x = random.choice(new_mammal["mutable_traits"])
    new_mammal["mutable_desc"] = (x, random.choice(mammal_mutable_adj))

    # MOULTING - PERIODIC SHEDDING of exoskeleton
    tf = ["True", "False"]
    new_mammal["moulting"] = random.choice(tf)
    new_mammal["has_exoskeleton"] = random.choice(tf)

    if new_mammal["moulting"] == True:
        new_mammal["moulting_stats"] = {}
        new_mammal["moulting_stats"]["stages_count"] = random.randrange(0,5)
        new_mammal["moulting_stats"]["stages_interval"] = random.randrange(1, 1000)
        new_mammal["moulting_stats"]["countdown to moulting"] = 0

    # MOULTING - CHANGE IN DEVELOPMENT PHASE


    new_mammal["description"] = [
        "This creature is an {0}.".format(new_mammal["class"]),
        "It is {0} sized and appears to be {1} in color.".format(new_mammal["size"], new_mammal["fur_color"]),
        "It has {0} leg(s) and {1} eye(s)".format(new_mammal["legs"], new_mammal["eyes"]),
        "it appears both {0} and {1} with {2} {3}".format(new_mammal["adj1"], new_mammal["adj2"], new_mammal["mutable_desc"][1], new_mammal["mutable_desc"][0])
    ]

    print("\n")
    for i in new_mammal["description"]:
        print(i)

    return new_mammal

#gen_mammal()