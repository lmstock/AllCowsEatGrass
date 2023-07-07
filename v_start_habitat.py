import PySimpleGUI as sg
import db_calls




def start_habitat():
    print("start habitat")

    sg.theme('Green')

    col1 = [
        [sg.Text("Run Vivarium")],
        [sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
        [sg.Button('Start Habitat', size=20, key="-START-")],
        [sg.Button('Stop Habitat', size=20, key="-STOP-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('LIVE HABITAT', layout)


    while True:
        event, values = window.read()
        print(event, values)
        

        if event == '-START-':
            pass

        if event == '-STOP-':
            pass

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()


if __name__ == "__main__":
    start_habitat()
