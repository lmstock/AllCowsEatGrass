import logger2, core
from creature_actions import sleep


def test_slp():
     ### TESTING ###
     # Active task here will alway be the defined action

     # rest: [current, loss per turn, max]
     # active_task: [action, priority, current inc, max inc]

     a = {
          'rest': [250, -1.41, 520],
          'active_task': ['sleep', 3, 1, 630],
          'rest_gain': .79
          }

     b = {
          'rest': [99, -1, 100],
          'active_task': ['sleep', 3, 1, 630],
          'rest_gain': 2
          }

     c = {
          'rest': [99, -1, 700],
          'active_task': ['sleep', 3, 629, 630],
          'rest_gain': 2
          }





     # TEST 1: active task is increased by 1, rest is increased
     x = sleep(a)
     assert x['active_task'][2] == 2
     assert x['rest'][0] == 250.79
     print("1. pass")

     # TEST 2: active task is completed due to well rested.
     x = sleep(b)
     assert x['active_task'] == []
     print("2. pass")

