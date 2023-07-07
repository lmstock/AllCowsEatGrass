import PySimpleGUI as sg




def population_window():
    print("population_window")

    sg.theme('DarkBrown')

    

    col1 = [
        [sg.Text("click on individual to open more detail")],
        [sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('POPULATION', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    population_window()
