import PySimpleGUI as sg
import db_calls
import funcs



def modify_habitat_window():

    sg.theme('DarkBrown')

    habs_list = db_calls.list_habs_data()

    data_string = funcs.format_string_for_modify(habs_list)




    window_msg = sg.Text(' ', text_color='white', visible=True, size=50, key="-MSG-")

    col1 = [
        [window_msg],
        [sg.Text('Habitat to Modify', size=25, key="-HABITAT_NAME_LABEL-"), sg.Input('Gaspar Borys', size=25, key="-HABITAT_NAME_INPUT-")],
        [sg.Text('Habitat Size - will be squared', size=25, key="-HABITAT_SIZE_LABEL-"), sg.Input('1000', size=25, key="-HABITAT_SIZE_INPUT-")],
        [sg.Text('Lower Life Forms Regeneration Rate', size=25, key="-LLF_REGEN_LABEL-"), sg.Input('50', size=25, key="-LLF_REGEN_INPUT-")],
        [sg.Button('Modify', size=20, key="-MODIFY_BTN-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1), sg.Multiline(size=(40, 25), key="-OUTPUT-", default_text="++ CURRENT HABITATS ++\n\n" + data_string)]]

    


    # window Label
    window = sg.Window('MODIFY HABITATS', layout)


    while True:
        event, values = window.read()
        print("events", event)
        print("values", values)

        if event == '-MODIFY_BTN-':

            modify_hab = {}
            modify_hab['name'] = values['-HABITAT_NAME_INPUT-']
            modify_hab['size'] = values['-HABITAT_SIZE_INPUT-']
            modify_hab['llf_regen'] = values['-LLF_REGEN_INPUT-']

            # function returns success or failure message
            x = funcs.modify_habitat(modify_hab)

            window['-MSG-'].update(x[0], text_color=x[1], visible=True)

            habs = db_calls.list_habitats()

            habs_list = db_calls.list_habitats()
            habs = '\n'.join(item for item in habs_list)

            window['-OUTPUT-'].update("++ CURRENT HABITATS ++\n\n" + habs)
            window.refresh()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    modify_habitat_window()