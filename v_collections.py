import PySimpleGUI as sg
import c_bestiary, c_herbarium, c_population




def collections_window():
    print("collections_window")

    sg.theme('DarkBrown')

    col1 = [
        [sg.Button('Bestiary', size=20, key="-BESTIARY-")],
        [sg.Button('Herbarium', size=20, key="-HERBARIUM-")],
        [sg.Button('Population', size=20, key="-POPULATION-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('COLLECTIONS', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-BESTIARY-':
            c_bestiary.bestiary_window()

        if event == '-HERBARIUM-':
            c_herbarium.herbarium_window()

        if event == '-POPULATION-':
            c_population.population_window()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    collections_window()
