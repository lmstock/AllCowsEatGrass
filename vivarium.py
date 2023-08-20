import PySimpleGUI as sg
import windows_navigation
import windows_collections
import windows_detail
import windows_habitat
import run_model



def vivarium_window():

    sg.theme('DarkBrown')

    vivarium_column = [
        [sg.Button('Habitats', size=25, key="-HABITATS-")],
        [sg.Button('Collections', size=25, key="-COLLECTIONS-")],
        [sg.Button('Start Habitat', size=25, key="-START-")],
        [sg.Button('Help', size=25, key="-HELP-")],
        [sg.Button('Exit Vivarium', size=25, key="-EXIT-")]
    ]

    layout = [[sg.Column(vivarium_column), sg.Multiline(size=(40, 20), default_text="this is here so I dont forget how to use columns")]]

    # window Label
    window = sg.Window('VIVARIUM', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-HABITATS-':
            windows_habitat.create_habitat_window()

        if event == '-COLLECTIONS-':
            windows_navigation.collections_window()

        if event == '-START-':
            run_model.run_model_function()

        if event == '-HELP-':
            windows_navigation.help()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()


if __name__ == "__main__":
    vivarium_window()