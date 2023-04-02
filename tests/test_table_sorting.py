import PySimpleGUI as sg
import operator



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



headers = ["fish","dog","cat","lucky cat"]
values1 = [[1,2,3,4],[5,6,8,6,],[0,3,5,4]]

table1 = sg.Table(headings=headers, values=values1[:][:], key="-TABLE-", enable_click_events=True)

layout = [[table1],
        [sg.Text('Cell Clicked: '), sg.T(k='-CLICKED-')],
        [sg.Button("CLOSE")]
        ]

window = sg.Window("TEST TABLE", layout)

table_sorting = [1, "asc"]

while True:
    event, values = window.read()
    print("event: ", event, "values: ", values)
    
    if event == sg.WIN_CLOSED:
        break

    if event[0] == '-TABLE-':
        
        if event[2][0] == -1 and event[2][1] != -1:
            
            # capture the column selected
            col_num_clicked = event[2][1]
            print(col_num_clicked)

            if col_num_clicked == table_sorting[0]:
                if table_sorting[1] == "asc":
                    new_table = rev_sort_table(values1[:][:],(col_num_clicked, 0))
                    table_sorting[0] = col_num_clicked
                    table_sorting[1] = "des"
                else:
                    new_table = sort_table(values1[:][:],(col_num_clicked, 0))
                    table_sorting[0] = col_num_clicked
                    table_sorting[1] = "asc"

            else:
                new_table = sort_table(values1[:][:],(col_num_clicked, 0))
                table_sorting[0] = col_num_clicked
                table_sorting[1] = "asc"


            print(table_sorting)
            window['-TABLE-'].update(new_table)
        window['-CLICKED-'].update(f'{event[2][0]},{event[2][1]}')

    if event == "CLOSE":
        break

window.close()
