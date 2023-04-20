import logger2
from core import promote_task_q

def test_pro_tsk():

     # TASK_Q = [action string, priority, current turn, duration]

     a = {
          'task_q': [],
          'active_task': [],
          'flag': 0
          }

     b = {
          'task_q': [["eat", 2, 0, 3],["wander", 3, 0, 3]],
          'active_task': [],
          'flag': 0
          }

     c = {
          'task_q': [["eat", 1, 0, 3],["sleep", 1, 0, 3]],
          'active_task': [],
          'flag': 0
          }


     

     # TEST 1: task_q is empty
     x = promote_task_q(a)
     assert x['active_task'][0] == 'wander'
     print("1. pass")

     # TEST 2: 2 diff priority options in task_q, choose high priority
     x = promote_task_q(b)
     assert x['active_task'][1] == 2
     print("2. pass")

     # TEST 2: 2 priority 1 options in task_q
     x = promote_task_q(c)
     assert x['active_task'][1] == 1
     l = len(x['task_q'])
     assert l == 1
     print("2. pass")