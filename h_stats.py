import PySimpleGUI as sg
import db_calls



def habitat_stats_window():

    sg.theme('DarkBrown')

    col1 = [
        [sg.Text('Habitat Name', size=25, key="-HABITAT_NAME_LABEL-"), sg.Input('Gaspar Borys', size=25, key="-HABITAT_NAME_INPUT-")],

        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1), sg.Multiline(size=(40, 25), default_text="++ CURRENT HABITATS ++\n\n")]]

    ### what statistics?


    # window Label
    window = sg.Window('HABITATS STATISTICS', layout)


    while True:
        event, values = window.read()
        print(event, values)


        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    habitat_stats_window()