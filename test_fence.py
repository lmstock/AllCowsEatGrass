from core import fence



def test_fence():

    a = {'x': 250,'y': 250 }
    b = {'x': 1000,'y': 250 }


    # TEST 1: no fence action required
    x = fence(a)
    assert x['x'] == 250
    assert x['y'] == 250
    print("1. pass")

    # TEST 2: no fence action required
    x = fence(b)
    assert x['x'] == 999
    assert x['y'] == 250
    print("1. pass")