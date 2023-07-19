
import creature_repr_actions, crets, bartokmongo

### SETS UP TEST CREATURE ###
# - SOMETHING IN UPDATING BESTIARY IS BROKEN AFTER MUTATION
# - SEE see test_division_2 for test using cret from population


def test_div():

    ### SETUP ###

    # add parent test cret to population for test
    bartokmongo.add_creature(crets.test_cret_a)
    bartokmongo.add_creature_species(crets.test_species_a)

    # setup ind for divide function
    id = crets.test_cret_a['_id']
    a = bartokmongo.read_ind_by_id(id)



    # runs the whole divide function which generates a child and possibly a mutation
    a = creature_repr_actions.divide(a)

    # identify child in db
    find_child = bartokmongo.find_latest_addition()

    for i in find_child:
        age = i['age']
        offspring = i['offspring']


            

    ### TESTS ###

    # Verify child age, offspring
    assert age == 0
    assert offspring == 0

    # Verify parent age, offspring
    assert a['age'] > 0
    assert a['offspring'] == 1
    print("TEST 1 pass")



    ### CLEANUP ###

    # remove all crets of species type 'testcreature'
    bartokmongo.remove_test_crets()


    # remove all species in bestiary that descend from testcreature
    bartokmongo.remove_test_species()
