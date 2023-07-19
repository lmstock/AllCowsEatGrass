from pymongo import MongoClient

c = MongoClient()
db = c['Vivarium']

def get_collection(collection_choice):
    collection_dict = {}
    for i in db[collection_choice].find():

        collection_dict.update({i['_id']:i})
    return collection_dict

# list all vivariums
def list_habitats():
    print("list_habitats")
    habs_list = []
    for i in db["habitats"].find():
        habs_list.append(i['name'])
    return habs_list

# list vivariums and data (for modify_habs)
def list_habs_data():
    print("list_habs_data")
    hab_data = []
    for i in db['habitats'].find():
        x = []
        x.append(i['name'])
        x.append(i['size'])
        x.append(i['llf_regen'])
        hab_data.append(x)
    return hab_data




def create_new_habitat(hab_dict):
    print("create_habitat")
    x = db["habitats"].insert_one(hab_dict)
    return x.inserted_id


def delete_habitat(name):
    print("delete habitat")
    query_object = {'name': name}
    x = db["habitats"].delete_one(query_object)
    return x

def mod_hab(modify_hab):
    print("db modify habitat")
    name = {"name" : modify_hab['name']}
    new_vals = { "$set" : modify_hab }
    
    ret_value = db['habitats'].update_one(name, new_vals)
    print(ret_value)
    return ret_value

