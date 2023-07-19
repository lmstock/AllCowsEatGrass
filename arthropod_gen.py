import random


# ARTHROPOD POOLS
arthropod_sizes = ["tiny", "small", "medium", "large", "very large", "colossal"]
arthropod_colors = ["red", "orange", "yellow", "green", "blue", "violet"]
arthropod_repr = ["division", "live birth", "egg", "egg", "egg"]
arthorpod_traits = ["antennea", "gills", "hairs", "claws", "pincers", "stinger", "mouth parts", "wings"]
arthropod_mvmt = ["flight", "walk", "climb", "swim", "run"]
attacks = ["song attack", "sting attack", "bite attack", "claw attack", "pinch attack"]
arthropod_adj1 = ["attractive", "colorful", "creepy", "dangerous", "elegant", "fierce", "gleaming", "homely", "lively"]
arthropod_adj2 = ["mysterious", "nervous", "odd", "prickly", "quaint", "sleepy", "tough", "unusual", "vivacious", "wild"]
arthropod_mutable_adj = ["well defined", "hidden", "non descript", "tidy", "clearly defined", "ordinary"]


def gen_arthropod():
    print("gen_arthropod")

    # ALL ARTHROPODS
    new_arthropod = {}
    new_arthropod["phylum"] = "arthropod"
    new_arthropod["has_exoskeleton"] = True
    new_arthropod["has_hemolymph"] = True
    # head, thorax, abdomen = True
    new_arthropod["size"] = random.choice(arthropod_sizes)
    new_arthropod["exoskeleton_color"] = random.choice(arthropod_colors)
    new_arthropod["reproduction"] = random.choice(arthropod_repr)
    new_arthropod["eyes"] = random.randrange(0,20)
    new_arthropod["legs"] = random.randrange(0,20)
    new_arthropod["adj1"] = random.choice(arthropod_adj1)
    new_arthropod["adj2"] = random.choice(arthropod_adj2)


    # MUTABLE TRAITS
    new_arthropod["mutable_traits"] = ["exoskeleton_color", "eyes", "legs", ]


    # RANDOM SELECTIONS
    def random_selections(pool):
        x = len(pool)
        quantity = random.randrange(0, x+1)
        for i in range(1,quantity):
            c = random.choice(pool)
            pool.remove(c)
            new_arthropod["mutable_traits"].append(c)
            new_arthropod[c] = True

    random_selections(arthorpod_traits)
    random_selections(arthropod_mvmt)
    random_selections(attacks)

    x = random.choice(new_arthropod["mutable_traits"])
    new_arthropod["mutable_desc"] = (x, random.choice(arthropod_mutable_adj))


    # MOULTING - PERIODIC SHEDDING of exoskeleton
    tf = ["True", "False"]
    new_arthropod["moulting"] = random.choice(tf)

    if new_arthropod["moulting"] == True:
        new_arthropod["moulting_stats"] = {}
        new_arthropod["moulting_stats"]["stages_count"] = random.randrange(0,5)
        new_arthropod["moulting_stats"]["stages_interval"] = random.randrange(1, 1000)
        new_arthropod["moulting_stats"]["countdown to moulting"] = 0

    # MOULTING - CHANGE IN DEVELOPMENT PHASE



    new_arthropod["description"] = [
        "This creature is an {0}.".format(new_arthropod["phylum"]),
        "It is {0} sized and appears to be {1} in color.".format(new_arthropod["size"], new_arthropod["exoskeleton_color"]),
        "It has {0} leg(s) and {1} eye(s)".format(new_arthropod["legs"], new_arthropod["eyes"]),
        "it appears both {0} and {1} with {2} {3}".format(new_arthropod["adj1"], new_arthropod["adj2"], new_arthropod["mutable_desc"][1], new_arthropod["mutable_desc"][0])
    ]

    print("\n")
    for i in new_arthropod["description"]:
        print(i)

    return new_arthropod

#gen_arthropod()

