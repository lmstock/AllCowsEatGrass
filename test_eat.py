
from creature_actions import eat


def test_eat_a():

     ### TESTING ###
     # Active task here will alway be the defined action

     # satiety: [current, loss per turn, max]
     # active_task: [action, priority, current inc, max inc]

     a = {
          'satiety': [50, -1, 100],
          'active_task': ['eat', 3, 1, 3]
          }

     b = {
          'satiety': [90, -1, 100],
          'active_task': ['eat', 3, 1, 3]
          }
     
     c = {
          'satiety': [105, -1, 100],
          'active_task': ['eat', 3, 1, 3]
          }





     # TEST 1: active task is increased by 1, satiety is increased
     x = eat(a)
     assert x['active_task'][2] == 2
     assert x['satiety'][0] == 83
     print("1. pass")

     # TEST 2: active task is completed.
     x = eat(b)
     assert x['active_task'] == []
     print("2. pass")

     
     # TEST 2: active task is completed.
     x = eat(c)
     assert x['active_task'] == []
     assert x['satiety'][0] <= x['satiety'][2]
     print("3. pass")


