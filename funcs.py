import db_calls

# Vivarium functions



def create_habitat(new_habitat):
    print("create_habitat")

    # new_habitat = dictionary of user input
    # print(new_habitat)

    # habs list of current habitats
    habs = db_calls.list_habitats()
    # print(habs)

    if new_habitat['name'] in habs:
        msg = "name in use, choose another name"
        # print(msg)
        return msg, "red"
        
    
    else:
        new_habitat.update({'ticks_per_day': 100, 'current_tick': 0, 'habitat_health': 1000})
        # print(new_habitat)
        result = db_calls.create_new_habitat(new_habitat)
        msg = "new habitat created: " + str(result)
        return msg, "green"


def modify_habitat(modify_hab):
    # validate name and launch db function
    print("modify_habitat")

    habs = db_calls.list_habitats()
    print(habs)

    if modify_hab['name'] not in habs:
        msg = "name not in use, choose another habitat"
        return msg, "red"
    
    else:
        result = db_calls.mod_hab(modify_hab)
        msg = str(result)
        return msg, "green"
    

def format_string_for_modify(d):
    # this function returns a string of the habitat data for modify_habitat page
    # it accepts a list of lists of habitat data from list_habs_data()
    print("format_string_for_modify")
    habs_list = []
    for i in d:
        habs = '\t\t'.join(item for item in i)
        habs_list.append(habs)

    final_str = '\n'.join(item for item in habs_list)
    return final_str



def delete_habitat(name):
    print("delete_habitat - inpro")

    # habs list of current habitats
    habs = db_calls.list_habitats()
    print(habs)
    print("name: ", name)

    if name not in habs:
        msg = "name not in use, choose another habitat"
        # print(msg)
        return msg, "red"
    
    else:
        result = db_calls.delete_habitat(name)
        print(result)
        return result, "green"