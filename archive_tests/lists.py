bestora_headers = ["flora_id", "type", "age", "energy", "coords"]

bestora = {   
 0: {'age': 0.81,
     'coords': (333, 116),
     'energy': 100,
     'flora_id': 0,
     'growth_data': [],
     'img': "<Surface(30x30x32 SW)>",
     'size': 'large',
     'type': 'afuw'},
 1: {'age': 0.81,
     'coords': (235, 153),
     'energy': 100,
     'flora_id': 1,
     'growth_data': [],
     'img': "<Surface(30x30x32 SW)>",
     'size': 'large',
     'type': 'hoakak'},
 2: {'age': 0.81,
     'coords': (84, 183),
     'energy': 100,
     'flora_id': 2,
     'growth_data': [],
     'img': "<Surface(30x30x32 SW)>",
     'size': 'very_large',
     'type': 'afakakva'}
}

# take list of strings and return a dict mapping list sequence {string: index}
def map_header_order(listz):
    map = {}
    ct = 0
    for i in listz:
        map[i] = ct
        ct = ct + 1
    print(map)
    return map

m = map_header_order(bestora_headers)

# returns list of values in map_header order
def order_list(mp, dct):
    
    for k in dct.items():
        row = []

        for j in mp.items():    


            for l in k[1].items():

                if l[0] == j[0]:
                    row.append(l[1])

        print (row)   


                
    return row

x = order_list(m, bestora)
#print(x)