import PySimpleGUI as sg
from pymongo import MongoClient
from bson.objectid import ObjectId
import mongotest



def open_bestiary_window():

    def get_bestiary():
        beasts = mongotest.bestiary.find()
        bestiary = {}
        for i in beasts:
            bestiary.update({i['species_type']:i})
        return bestiary

    bestiary = get_bestiary()

    def get_headers():
        headers = []
        sample = []
        for k in bestiary.keys():
            sample = []
            sample.append(k)
        for l in bestiary[sample[0]].keys():
            headers.append(l)
        return headers

    def get_rows():
        rows = []
        for v in bestiary.values():
            row = []
            for i in v.values():
                row.append(i)
            rows.append(row)
        return rows
    
    bestiary = get_bestiary()
    print(bestiary)
    headers = get_headers()

    rows = get_rows()
    print("headers ", headers)
    print("rows ", rows)


    table1 = sg.Table(values=rows, headings=headers, auto_size_columns=True, justification='center', key="-TABLE-", enable_events=True, expand_x=True, expand_y=True, enable_click_events=True)
    layout_bestiary = [[table1]]
    window = sg.Window("tbale demo", layout_bestiary, size=(1100,800), resizable=True)

    while True:
        event, values = window.read()
        print("event: ", event, "values: ", values)

        if event == sg.WIN_CLOSED:
            break
        if '-CLICKED-' in event:
            sg.popup("you clicked row:{} Column: {}".format(event[2][0]. event[2][1]))

    window.close()



