import PySimpleGUI as sg

headers = ["fish","dog","cat","lucky cat"]
values1 = [[1,2,3,4],[5,6,8,6,],[0,3,5,4]]

table1 = sg.Table(headings=headers, values=values1[:][:])

layout = [[table1]]

window = sg.Window("test", layout)

while True:
    event, values = window.read()
    print("event: ", event, "values: ", values)

    if event == sg.WIN_CLOSED:
        break

    # returns True if event is tuple
    #if isinstance(event, tuple):

window.close()
