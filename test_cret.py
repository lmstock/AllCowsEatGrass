


import game_imgs.imgs
from creature import Creature
from species import Species

# test species for testing

def gen_test_species():
    test_species1 = Species(
        "akpeto",
        game_imgs.imgs.cret2_large,
        "pointy",
        'mega',
        'humanoid',
        460,  # sleep duration
        190,
        .41,
        -.35,
        37100,

    )

# test creature for testing

def gen_test_crets():

    test_cret1 = Creature(
        "sleepy", #creature_type,
        "my_img",
        "my_bg_img",
        "medium", #my_size,

        320, #sleep_dur,
        1.38, #rest_gain,
        -.65, #base_fatigue,

        [200, 440], #rest,
        [38, 100], #satiety,
        [100, 100], #energy,

        [100, 100], #hostility,
        [100, 100], #health,
        [49.5, 99, 297, 594], #speed
        [1000] #fov
        )

    test_cret2 = Creature(
        "hungry", #creature_type,
        "my_img",
        "my_bg_img",
        "tiny", #my_size,

        320, #sleep_dur,
        1.38, #rest_gain,
        -.65, #base_fatigue,

        [320, 440], #rest,
        [38, 100], #satiety,
        [100, 100], #energy,

        [100, 100], #hostility,
        [100, 100], #health,
        [49.5, 99, 297, 594], #speed
        [1000] #fov
        )







