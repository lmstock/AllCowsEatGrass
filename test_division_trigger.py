

from triggers import check_division

def test_div_trigger():

    # === TEST CASES === #
    a = {'_id': 'ObjectId("642d5e373990c645704b99cc")', 'repr_cooldown': [0, 10000], 'task_q': [], 'active_task': []}
    b = {'_id': 'ObjectId("642d5e373990c645704b99cc")', 'repr_cooldown': [99, 99], 'task_q': [], 'active_task': []}




    ### TESTING ###
    # TEST 1
    x = check_division(a)
    assert x['repr_cooldown'][0] == 1
    assert x['task_q'] == []
    print("TEST 1 pass")

    # TEST 2
    x = check_division(b)
    assert x['repr_cooldown'][0] == 0
    assert x['task_q'] != []
    print("TEST 2 pass")


