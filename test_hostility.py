
from triggers import check_hostility


def test_host():

  a = {
      "_id": {"$oid": "6435f4c16d4f738da4e71fe3"},
      "hostility": [ 10, 100],
      "local_crets": [],
    "active_task": [],
    "target": 0
  }

  b = {
      "_id": {"$oid": "6435f4c16d4f738da4e71fe3"},
      "hostility": [ 10, 100],
      "local_crets": [
      [{"$oid": "6435f4c16d4f738da4e71fe3"},"teayay", ["wander",3,0,3]]
    ],
    "active_task": [],
    "target": 0
  }

  c = {
      "_id": {"$oid": "6435f4c16d4f738da4e71fe3"},
      "hostility": [ 10, 100],
      "local_crets": [
      [{"$oid": "6435f4c16d4f738da4e71fe3"},"teayay", ["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe4"},"od",["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe5"},"futakeoz",["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe6"},"duamda",["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe7"},"dooz",["wander",3,0,3]]
    ],
    "active_task": [],
    "target": 0
  }

  d = {
      "_id": {"$oid": "6435f4c16d4f738da4e71fe3"},
      "hostility": [100, 100],
      "local_crets": [],
    "active_task": [],
    "target": 0
  }

  e = {
      "_id": {"$oid": "6435f4c16d4f738da4e71fe3"},
      "hostility": [ 100, 100],
      "local_crets": [
      [{"$oid": "6435f4c16d4f738da4e71fe3"},"teayay", ["wander",3,0,3]]
    ],
    "active_task": [],
    "target": 0
  }

  f = {
      "_id": {"$oid": "6435f4c16d4f738da4e71fe3"},
      "hostility": [ 100, 100],
      "local_crets": [
      [{"$oid": "6435f4c16d4f738da4e71fe3"},"teayay", ["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe4"},"od",["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe5"},"futakeoz",["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe6"},"duamda",["wander",3,0,3]],
      [{"$oid": "6435f4c16d4f738da4e71fe7"},"dooz",["wander",3,0,3]]
    ],
    "active_task": [],
    "target": 0
  }


  # Test 1 - local crets is false, host < .9
  x = check_hostility(a)
  assert x['active_task'] == []
  assert x['target'] == 0
  assert x['local_crets'] == []
  print ("Test 1 pass")

  # Test 2 - local crets contains only self, host < .9
  x = check_hostility(b)
  assert x['active_task'] == []
  assert x['target'] == 0
  assert x['local_crets'] != []
  print ("Test 2 pass")

  # Test 3 - local crets contains list, host < .9
  x = check_hostility(c)
  assert x['active_task'] == []
  assert x['target'] == 0
  assert x['local_crets'] != []
  print ("Test 3 pass")

  # Test 4 - local crets is false, host > .9
  x = check_hostility(d)
  assert x['active_task'] == []
  assert x['target'] == 0
  assert x['local_crets'] == []
  print ("Test 4 pass")

  # Test 5 - local crets contains only self, host > .9
  x = check_hostility(e)
  assert x['active_task'] == []
  assert x['target'] == 0
  assert x['local_crets'] != []
  print ("Test 5 pass")

  # Test 6 - local crets contains list, host > .9
  x = check_hostility(f)
  assert x['active_task'][0] == "attack"
  assert x['target'] != 0
  assert x['local_crets'] != []
  print ("Test 6 pass")
