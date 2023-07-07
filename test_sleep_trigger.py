import logger2
from triggers import check_current_rest


def test_slp_trigger():

     ### TESTING ###
     a = {
          'sleep_duration': 460.0,
          'rest': [150.07, -1, 170], 
          'task_q': [],
          'active_task': []
          }

     b = {
          'sleep_duration': 460.0,
          'rest': [67.07, -1, 170],  
          'task_q': [],
          'active_task': ["sleep", 1, 0, 460],
          }

     c = {
          'sleep_duration': 460.0,
          'rest': [67.07, -1, 170], # should generate a p3
          'task_q': [],
          'active_task': []
          }

     d = {
          'sleep_duration': 460.0,
          'rest': [15.07, -1, 170],
          'task_q': [["sleep", 1, 0, 460]],
          'active_task': ["play", 1, 0, 460],
          'is_alive': False
          }

     e = {
          'sleep_duration': 460.0,
          'rest': [15.07, -1, 170],
          'task_q': [["sleep", 3, 0, 460], ["eat", 2, 0, 460]],
          'active_task': ["play", 1, 0, 460]
          }


     # TEST 1: active task is empty and sleep > 40% 
     x = check_current_rest(a)
     assert x['active_task'] == []
     assert x['rest'][0] > x['rest'][2] * .4
     print("1. pass")

     # TEST 2: if active task is sleep, function should exit
     x = check_current_rest(b)
     assert x['active_task'][0] == 'sleep'
     print("2. pass")

     # TEST 3: if active task is empty and sleep < 40% a task sleep should be added to task_q at p3
     x = check_current_rest(c)
     assert x['active_task'] == []
     assert x['rest'][0] < x['rest'][2] * .4
     assert x['task_q'][0][0] == 'sleep'
     assert x['task_q'][0][1] == 3
     print("3. pass")

     # TEST 4: if sleep < 10% and sleep of p3 already in task_q
     x = check_current_rest(d)
     assert x['active_task'][0] != 'sleep'
     assert x['task_q'][0][1] == 1 
     print("4. pass")

