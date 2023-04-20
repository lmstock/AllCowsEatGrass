from creature_actions import wander


def test_wnder():

     a = {
          'speed': 460.0,
          'x': 0,
          'y': 0,
          'active_task': ['play', 3, 4, 6],
          }

     b = {
          'speed': 460.0,
          'x': 590,
          'y': -590,
          'active_task': ['play', 3, 4, 6],
          }

     c = {
          'speed': 460.0,
          'x': 13,
          'y': 1005,
          'active_task': ['play', 3, 4, 6],
          }

     d = {
          'speed': 460.0,
          'x': 590,
          'y': -1590,
          'active_task': ['play', 3, 4, 6],
          }






     # TEST 1: increment turn
     x = wander(a)
     assert x['active_task'][2] == 5
     print("1. pass")

     # TEST 2: inside fence, no change
     x = wander(b)
     assert x['x'] < 1000
     assert x['x'] > -1000
     assert x['y'] < 1000
     assert x['y'] > -1000
     print("2. pass")

     # TEST 3: outside of north fence
     x = wander(c)
     assert x['x'] < 1000
     assert x['x'] > -1000
     assert x['y'] < 1000
     assert x['y'] > -1000
     print("2. pass")

     # TEST 3: outside of west fence
     x = wander(d)
     assert x['x'] < 1000
     assert x['x'] > -1000
     assert x['y'] < 1000
     assert x['y'] > -1000
     print("2. pass")