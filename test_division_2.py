
# import creature_repr_actions, crets, bartokmongo
# import random

# ### USE CRET FROM POPULATION ###
# # - SOMETHING IN UPDATING BESTIARY IS BROKEN AFTER MUTATION
# # - THIS IS THE BEGINNING OF THE TEST FOR SPECIES GEN
# # - - HOW TO RUN THIS ?


# def test_div():

#     ### SETUP ###

#     # GET RANDOM CREATURE AND ITS SPECIES FROM DB

#     # returns creature as dict
#     rand_sample = bartokmongo.get_rand_pop()
#     sample_list = []
#     for i in rand_sample:
#         sample_list.append(i['_id'])
#         x = random.choice(sample_list)
#         creature = bartokmongo.read_ind_by_id(x)
    
#     # species is dict
#     species = bartokmongo.read_creature_species_du('species_type', creature['species_type'])

#     print(creature)
#     print(species)
    

#     # runs the whole divide function which generates a child and possibly a mutation
#     a = creature_repr_actions.divide(creature)

#     # # identify child in db
#     find_child = bartokmongo.find_latest_addition()

#     for i in find_child:
#         age = i['age']
#         offspring = i['offspring']


            

#     # ### TESTS ###

#     # # Verify child age, offspring
#     # assert age == 0
#     # assert offspring == 0

#     # # Verify parent age, offspring
#     # assert a['age'] > 0
#     # assert a['offspring'] == 1
#     # print("TEST 1 pass")



#     ### CLEANUP ###

#     # we may or may not need to remove the additions made during this test

# test_div()