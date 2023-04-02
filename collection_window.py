
import PySimpleGUI as sg
import operator



def open_collection_window(collection):

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
    
    def sort_table(table, cols):

        for col in reversed(cols):
            try:
                table = sorted(table, key=operator.itemgetter(col))
            except Exception as e:
                print(e)
        return table

    def rev_sort_table(table, cols):

        for col in reversed(cols):
            try:
                table = sorted(table, key=operator.itemgetter(col), reverse=True)
            except Exception as e:
                print(e)
        return table
    
    headers = get_headers()
    data = get_rows()

    table1 = sg.Table(values=data[:][:], headings=headers, auto_size_columns=True, justification='center', key="-TABLE-", vertical_scroll_only=False, expand_x=True, expand_y=True, enable_click_events=True)
    layout_collection = [[table1],[sg.Text('Cell clicked:'), sg.T(k='-CLICKED-')],[sg.Button("CLOSE")]]
    window = sg.Window("Collections Window", layout_collection, resizable=True)

    table_sorting = [1, "asc"]  # sorting flag

    while True:
        event, values = window.read()
        print("event: ", event, "values: ", values)

        if event == sg.WIN_CLOSED:
            break


        if event[0] == '-TABLE-':

            if event[2][0] == -1 and event[2][1] != -1:

                col_num_clicked = event[2][1]

                if col_num_clicked == table_sorting[0]:
                    if table_sorting[1] == "asc":
                        new_table = rev_sort_table(data[:][:],(col_num_clicked, 0))
                        table_sorting[0] = col_num_clicked
                        table_sorting[1] = "des"
                    else:
                        new_table = sort_table(data[:][:],(col_num_clicked, 0))
                        table_sorting[0] = col_num_clicked
                        table_sorting[1] = "asc"

                else:
                    new_table = sort_table(data[:][:],(col_num_clicked, 0))
                    table_sorting[0] = col_num_clicked
                    table_sorting[1] = "asc"

                window['-TABLE-'].update(new_table)
            window['-CLICKED-'].update(f'{event[2][0]},{event[2][1]}')

        if event == "CLOSE":
            break

    window.close()



