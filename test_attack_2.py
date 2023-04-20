
import bartokmongo, crets

from creature_actions import attack

def test_attack_2():

    ##### TEST FOR STANDARD ATTACK SCENARIO #####
    #    - hostile not in range

    ### SETUP ###

    # add hostile cret to db
    h = bartokmongo.add_test_creature(crets.test_cret_b2)
    h_id = h.inserted_id

    #add target to db
    t = bartokmongo.add_test_creature(crets.test_cret_c)
    t_id = t.inserted_id

    print(h_id, t_id)

    # set target
    update = {"target": t_id}
    bartokmongo.update_cret_byid(h_id, update)

    # set actors
    hostile = bartokmongo.read_ind_by_id(h_id)
    target = bartokmongo.read_ind_by_id(t_id)


    ### ATTACK ###
    hostile = attack(hostile)


    # actor attributes that are changed wont display in 
    # db call until it gets to the end of action() sequence
    # var is set here for testing
    hostile_health = hostile['health']

    ### RESULTS ###
    hostile = bartokmongo.read_ind_by_id(h_id)
    target = bartokmongo.read_ind_by_id(t_id)

    # Verify attributes
    assert hostile['target'] != None
    assert hostile_health == [100,100]
    assert target['health'] == [100,100]
    print("TEST 1 pass")


    ### CLEANUP ###

    # remove all crets of species type 'testcreature'
    bartokmongo.remove_test_crets()

