import PySimpleGUI as sg
import db_calls
import funcs



def delete_habitat_window():

    sg.theme('DarkBrown')

    habs_list = db_calls.list_habitats()
    habs = '\n'.join(item for item in habs_list)

    window_msg = sg.Text(' ', text_color='white', visible=True, size=50, key="-MSG-")

    col1 = [
        [window_msg],
        [sg.Text('Habitat Name', size=25, key="-HABITAT_NAME_LABEL-"), sg.Input('Gaspar Borys', size=25, key="-HABITAT_NAME_INPUT-")],

        [sg.Button('Delete', bind_return_key=True, size=20, key="-DELETE_BTN-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1), sg.Multiline(size=(40, 25), auto_refresh=True, write_only=True, key='-OUTPUT-', default_text="++ CURRENT HABITATS ++\n\n" + habs)]]

    
    # window Label
    window = sg.Window('DELETE HABITATS', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-DELETE_BTN-':

            x = funcs.delete_habitat(values['-HABITAT_NAME_INPUT-'])   

            window['-MSG-'].update(x[0], text_color=x[1], visible=True)

            habs = db_calls.list_habitats()
            window['-HABITAT_NAME_INPUT-'].update("")
            window['-OUTPUT-'].update("++ CURRENT HABITATS ++\n\n" + habs)
            window.refresh()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    delete_habitat_window()