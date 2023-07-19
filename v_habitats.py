import PySimpleGUI as sg
import h_create, h_delete, h_modify, h_stats



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
            h_create.create_habitat_window()

        if event == '-MODIFY_HABITAT-':
            h_modify.modify_habitat_window()

        if event == '-HABITAT_STATISTICS-':
            h_stats.habitat_stats_window()

        if event == '-DELETE_HABITAT-':
            h_delete.delete_habitat_window()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    habitats_window()
