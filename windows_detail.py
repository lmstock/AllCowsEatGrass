import PySimpleGUI as sg




def individual_window():
    print("individual_window")

    sg.theme('DarkBrown')

    

    col1 = [
        [sg.Text("IMPORTANT TEXT HERE")],
        [sg.Table([[1,2,3], [4,5,6]], [ 'Col 1','Col 2','Col 3'], num_rows=2)],
        [sg.Text("CHANGE LOCATION")],
        [sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('INDIVIDUAL', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()


def species_window():
    print("species_window")

    sg.theme('DarkBrown')

    

    col1 = [
        [sg.Text("IMPORTANT TEXT HERE")],
        [sg.Table([[1,2,3], [4,5,6]], [ 'Col 1','Col 2','Col 3'], num_rows=2)],

        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('SPECIES', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()


if __name__ == "__main__":
    individual_window()
