import PySimpleGUI as sg
from pymongo import MongoClient
from bson.objectid import ObjectId
import bartokmongo



def open_bestiary_window():

    def get_bestiary():
        beasts = bartokmongo.get_bestiary()
        return beasts

    bestiary = get_bestiary()


    headers = ["_id", "phylum", "class", "species_type", "size", "mutation_count", "description"]

    def get_rows():
        print("yes")
        rows = []
        for k,v in bestiary.items():
            row = []

            for h in headers:

                if h not in v.keys():
                    row.append("na")
                
                for vi in v.items():
                    if vi[0] == h:
                        row.append(vi[1])

            rows.append(row)

        return rows
            
    


    rows = get_rows()



    table1 = sg.Table(values=rows, headings=headers, auto_size_columns=True, justification='center', key="-TABLE-", enable_events=True, expand_x=True, expand_y=True, vertical_scroll_only=False, enable_click_events=True)
    layout_bestiary = [[table1]]
    window = sg.Window("tbale demo", layout_bestiary, size=(800,600), resizable=True)

    while True:
        event, values = window.read()
        print("event: ", event, "values: ", values)

        if event == sg.WIN_CLOSED:
            break
        if '-CLICKED-' in event:
            sg.popup("you clicked row:{} Column: {}".format(event[2][0]. event[2][1]))

    window.close()

open_bestiary_window()


