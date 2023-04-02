import mongotest
import PySimpleGUI as sg

def open_individual_window(collection):

    def get_headers():
        headers = []
        sample = []
        for k in collection.keys():
            sample = []
            sample.append(k)
        for l in collection[sample[0]].keys():
            headers.append(l)
        return headers

    def get_rows():
        rows = []
        for v in collection.values():
            row = []
            for i in v.values():
                row.append(i)
            rows.append(row)
        return rows
    
    headers = get_headers()
    rows = get_rows()


    table1 = sg.Table(values=rows, headings=headers, auto_size_columns=True, justification='center', key="-TABLE-", vertical_scroll_only=False, enable_events=True, expand_x=True, expand_y=True, enable_click_events=True)
    layout_collection = [[table1]]
    window = sg.Window("collection tables", layout_collection, size=(1100,800), resizable=True)

    while True:
        event, values = window.read()
        print("event: ", event, "values: ", values)

        if event == sg.WIN_CLOSED:
            break
        if '-CLICKED-' in event:
            sg.popup("you clicked row:{} Column: {}".format(event[2][0]. event[2][1]))
            individual = event[2][0]
            print (individual)

    window.close()



