from inc_turn import update_kb


def update_knowledge_base():

     #change
     # local_crets = (i['_id'], i['species_type'], i['active_task'])
     # knowledge_base = {"species_name": observation count, investigation count, response code}


     a = {
          'knowledge_base': {"up" : [0.5, 0.5, 1]},
          'active_task': [],
          'local_crets': []
          }

     b = {
          'knowledge_base': {"ex" : [0.5, 0.5, 1], "oweh": [1, 0, 1]},
          'active_task': [],
          'local_crets': [("cret_id", "oweh", ['play', 3, 5, 6])]
          }

     c = {
          'knowledge_base': {"ex" : [0.5, 0.5, 1], "oweh": [1, 0, 1]},
          'active_task': [],
          'local_crets': [("cret_id", "oweh", ['attack', 3, 5, 6])]
          }

     d = {
          'knowledge_base': {"ex" : [0.5, 0.5, 1], "else": [1, 0, 1]},
          'active_task': [],
          'local_crets': [("cret_id", "oweh", ['play', 3, 5, 6])]
          }

     e = {
          'knowledge_base': {"ex" : [0.5, 0.5, 1], "else": [1, 0, 1]},
          'active_task': [],
          'local_crets': [("cret_id", "oweh", ['attack', 3, 5, 6])]
          }

     f = {
          'knowledge_base': {"ex" : [0.5, 0.5, 1], "else": [1, 0, 1]},
          'active_task': [],
          'local_crets': [("cret_id", "oweh", [])]
          }






     # TEST 1: local crets is empty
     x = update_kb(a)
     assert x['local_crets'] == []
     print("1. pass")

     # TEST 2: cret in kb, not attacking
     x = update_kb(b)
     assert x['knowledge_base']['oweh'][2] == 1
     assert x['knowledge_base']['oweh'][0] == 2
     print("2. pass")

     # # TEST 3: cret in kb, is attacking
     x = update_kb(c)
     assert x['knowledge_base']['oweh'][2] == 3
     assert x['knowledge_base']['oweh'][0] == 2
     print("3. pass")

     # TEST 4: cret not in kb, not attacking
     x = update_kb(d)
     assert x['knowledge_base']['oweh'][0] == 1
     assert x['knowledge_base']['oweh'][2] == 1
     print("4. pass")

     # TEST 5: cret not in kb, is attacking
     x = update_kb(e)
     assert x['knowledge_base']['oweh'][0] == 1
     assert x['knowledge_base']['oweh'][2] == 3
     print("5. pass")

     # TEST 6: cret not in kb, has no active_task
     x = update_kb(f)
     assert x['knowledge_base']['oweh'][0] == 1
     assert x['knowledge_base']['oweh'][2] == 1
     assert len(x['knowledge_base']) == 3
     print("5. pass")





