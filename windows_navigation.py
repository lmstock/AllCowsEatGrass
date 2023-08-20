import PySimpleGUI as sg
import windows_collections
import windows_habitat




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
            windows_collections.bestiary_window()

        if event == '-HERBARIUM-':
            windows_collections.herbarium_window()

        if event == '-POPULATION-':
            windows_collections.population_window()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()


def habitats_window():
    print("habitats_window")

    sg.theme('DarkBrown')

    col1 = [
        [sg.Button('Create Habitat', size=20, key="-CREATE_HABITAT-")],
        [sg.Button('Modify Habitat', size=20, key="-MODIFY_HABITAT-")],
        [sg.Button('Delete Habitat', size=20, key="-DELETE_HABITAT-")],
        [sg.Button('Habitat Statistics', size=20, key="-HABITAT_STATISTICS-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('HABITATS', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-CREATE_HABITAT-':
            windows_habitat.h_create.create_habitat_window()

        if event == '-MODIFY_HABITAT-':
            windows_habitat.modify_habitat_window()

        if event == '-HABITAT_STATISTICS-':
            windows_habitat.habitat_stats_window()

        if event == '-DELETE_HABITAT-':
            windows_habitat.delete_habitat_window()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()


def help():
    print("help set")

    sg.theme('DarkBrown')

    col1 = [

        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('VIVARIUM MANUALS', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-STOP-':
            pass


        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break

    window.close()


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
    collections_window()
