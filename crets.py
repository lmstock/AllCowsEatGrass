

### TEST ASSETS ###

test_species_a = {
  "species_type": "testcreature",
  "head": "oval",
  "size": "tiny",
  "body_type": "consisting of a head, torso, and limbs",
  "rest": [480,-0.48,480],
  "sleep_duration": 10,
  "rest_gain": 25,
  "satiety": [100,-1,100],
  "hostility": [0,47],
  "health": [100,100],
  "energy": [100,100],
  "speed": 78,
  "fov": 1000,
  "mutation_count": 0,
  "repr_cooldown": [0,20]
}

#bartokmongo.add_creature_species(test_species_a)

# originally for testing division
test_cret_a = {
  "species_type": "testcreature",
  "size": "tiny",
  "sleep_dur": 10,
  "rest_gain": 25,
  "rest": [368.15,-0.37,370],
  "satiety": [95,-1,100],
  "energy": [100,100],
  "hostility": [0,50],
  "health": [100,100],
  "speed": 94,
  "fov": 1000,
  "age": 0.000015,
  "x": 156,
  "y": 250,
  "task_q": [],
  "active_task": ["wander",3,0,3],
  "repr_cooldown": [5,100],
  "offspring": 0,
  "attack": 10,
  "defend": 10,
  "target": 0,
  "local_crets": [],
  "knowledge_base": {
    "xuge": [0.5,0.5,1],
    "imah": [5,0,1],
    "fefeiv": [5,0,1],
    "daix": [5,0,1],
	"ne": [5,0,1]},
  "is_alive": True
  }

# modified for testing attack 1
# hostility = 49
test_cret_b = {
  "species_type": "testcreature",
  "size": "tiny",
  "sleep_dur": 10,
  "rest_gain": 25,
  "rest": [368.15,-0.37,370],
  "satiety": [95,-1,100],
  "energy": [100,100],
  "hostility": [49,50],
  "health": [100,100],
  "speed": 94,
  "fov": 1000,
  "age": 0.000015,
  "x": 156,
  "y": 250,
  "task_q": [],
  "active_task": ["attack",1,0,3],
  "repr_cooldown": [5,100],
  "offspring": 0,
  "attack": 10,
  "defend": 10,
  "target": 0,
  "local_crets": [],
  "knowledge_base": {
    "xuge": [0.5,0.5,1],
    "imah": [5,0,1],
    "fefeiv": [5,0,1],
    "daix": [5,0,1],
	"ne": [5,0,1]},
  "is_alive": True
  }

# modified for testing attack 2
# out of range
test_cret_b2 = {
  "species_type": "testcreature",
  "size": "tiny",
  "sleep_dur": 10,
  "rest_gain": 25,
  "rest": [368.15,-0.37,370],
  "satiety": [95,-1,100],
  "energy": [100,100],
  "hostility": [49,50],
  "health": [100,100],
  "speed": 94,
  "fov": 1000,
  "age": 0.000015,
  "x": 10,
  "y": 250,
  "task_q": [],
  "active_task": ["attack",1,0,3],
  "repr_cooldown": [5,100],
  "offspring": 0,
  "attack": 10,
  "defend": 10,
  "target": 0,
  "local_crets": [],
  "knowledge_base": {
    "xuge": [0.5,0.5,1],
    "imah": [5,0,1],
    "fefeiv": [5,0,1],
    "daix": [5,0,1],
	"ne": [5,0,1]},
  "is_alive": True
  }

# modified for testing attack 3
# hatile retreats
test_cret_b3 = {
  "species_type": "testcreature",
  "size": "tiny",
  "sleep_dur": 10,
  "rest_gain": 25,
  "rest": [368.15,-0.37,370],
  "satiety": [95,-1,100],
  "energy": [100,100],
  "hostility": [49,50],
  "health": [3,100],
  "speed": 94,
  "fov": 1000,
  "age": 0.000015,
  "x": 156,
  "y": 250,
  "task_q": [],
  "active_task": ["attack",1,0,3],
  "repr_cooldown": [5,100],
  "offspring": 0,
  "attack": 10,
  "defend": 10,
  "target": 0,
  "local_crets": [],
  "knowledge_base": {
    "xuge": [0.5,0.5,1],
    "imah": [5,0,1],
    "fefeiv": [5,0,1],
    "daix": [5,0,1],
	"ne": [5,0,1]},
  "is_alive": True
  }

# modified for testing attack 1-3
# target 
test_cret_c = {
  "species_type": "testcreature",
  "size": "tiny",
  "sleep_dur": 10,
  "rest_gain": 25,
  "rest": [368.15,-0.37,370],
  "satiety": [95,-1,100],
  "energy": [100,100],
  "hostility": [49,50],
  "health": [100,100],
  "speed": 94,
  "fov": 1000,
  "age": 0.000015,
  "x": 156,
  "y": 250,
  "task_q": [],
  "active_task": ["wander",3,0,3],
  "repr_cooldown": [5,100],
  "offspring": 0,
  "attack": 10,
  "defend": 10,
  "target": 0,
  "local_crets": [],
  "knowledge_base": {
    "xuge": [0.5,0.5,1],
    "imah": [5,0,1],
    "fefeiv": [5,0,1],
    "daix": [5,0,1],
	"ne": [5,0,1]},
  "is_alive": True
  }







