import random

task_q = []

wander = ["wander", 3, 0, 3]
sleep = ["sleep", 3, 0, 7]
juggle = ["juggle", 2, 0, 7]
tumble = ["tumble", 2, 0, 7]
hide = ["hide", 2, 0, 7]
wobble = ["wobble", 3, 0, 7]
chase = ["chase", 2, 0, 7]
gobble = ["gobble", 2, 0, 7]

task_q.append(wander)
task_q.append(sleep)
task_q.append(juggle)
task_q.append(tumble)
task_q.append(hide)
task_q.append(wobble)
task_q.append(chase)
task_q.append(gobble)

# get new task from task q based on highest priority
def get_new_task():
     print("get_new_task")

     p1,p2,p3 = [],[],[]

     for i in task_q:
          if i[1] == 1: p1.append(i)
          elif i[1] == 2: p2.append(i)
          else: p3.append(i)

     if p1 != []: x = random.choice(p1)
     elif p2 != []: x = random.choice(p2)
     else: x = random.choice(p3)

     print(p1)
     print(p2)
     print(p3)
     
     return x

task = get_new_task()
print (task)