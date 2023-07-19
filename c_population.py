import PySimpleGUI as sg

def population_window():
    print("population_window")

    sg.theme('DarkBrown')

    

    col1 = [
        [sg.Text("POPULATION")],
        [sg.Text("click on individual to open more detail")],
        [sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
        [sg.Button('Gen Individual', size=20, key="-GEN_IND-")],
        [sg.Button('mass die off', size=20, key="-MASS-")],
        [sg.Button('full creature die off', size=20, key="-FULL-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('POPULATION', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-GEN_IND-':
            pass

        if event == '-MASS-':
            pass

        if event == '-FULL-':
            pass

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    population_window()
