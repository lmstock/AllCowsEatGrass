import PySimpleGUI as sg
import v_habitats
import v_collections
import v_start_habitat
import v_helpset
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
            v_habitats.habitats_window()

        if event == '-COLLECTIONS-':
            v_collections.collections_window()

        if event == '-START-':
            run_model.run_model_function()

        if event == '-HELP-':
            v_helpset.help()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()


if __name__ == "__main__":
    vivarium_window()