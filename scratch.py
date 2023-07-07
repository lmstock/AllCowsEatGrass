
import db_calls

def modify_habitat(modify_hab):
    print("modify_habitat")

    habs = db_calls.list_habitats()

    if modify_hab['name'] in habs:
        print('yes')

    else:
        print('no')

    


mh = {'name': "Gaspar", 'size': '1000'}

modify_habitat(mh)