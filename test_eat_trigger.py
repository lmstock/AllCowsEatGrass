import logger2
from triggers import check_current_satiety


def test_eat_trig():

     ### TESTING ###

     a = {
          'satiety': [100, -1, 100],
          'task_q': [],
          'active_task': []
          }

     b = {

          'satiety': [100, -1, 100],
          'task_q': [],
          'active_task': ['eat', 3, 5, 6],
          }

     c = {

          'satiety': [38, -1, 100],
          'task_q': [],
          'active_task': []
          }

     d = {
          'satiety': [4, -1, 100],
          'task_q': [['eat', 3, 5, 6]],
          'active_task': ['play', 3, 5, 6],
          'is_alive': True
          }



     # TEST 1: active task is empty and satiety > 40% 
     x = check_current_satiety(a)
     assert x['active_task'] == []
     assert x['satiety'][0] > x['satiety'][2] * .4
     print("1. pass")

     # TEST 2: if active task is eat, function should exit
     x = check_current_satiety(b)
     assert x['active_task'][0] == 'eat'
     print("2. pass")

     # TEST 3: if active task is empty and eat < 40% a task eat should be added to task_q at p3
     x = check_current_satiety(c)
     assert x['active_task'] == []
     assert x['satiety'][0] < x['satiety'][2] * .4
     assert x['task_q'][0][0] == 'eat'
     assert x['task_q'][0][1] == 3
     print("3. pass")

     # TEST 4: if eat < 10% and eat of p3 already in task_q
     x = check_current_satiety(d)
     assert x['active_task'][0] != 'eat'
     assert x['task_q'][0][1] == 1 
     print("4. pass")

