import PySimpleGUI as sg
import db_calls
import funcs



def create_habitat_window():

    sg.theme('DarkBrown')

    habs_list = db_calls.list_habitats()
    habs = '\n'.join(item for item in habs_list)

    window_msg = sg.Text(' ', text_color='white', visible=True, size=32, key="-MSG-")

    col1 = [
        [window_msg],
        [sg.Text('Habitat Name', size=25, key="-HABITAT_NAME_LABEL-"), sg.Input('Gaspar Borys', size=25, key="-HABITAT_NAME_INPUT-")],
        [sg.Text('Habitat Size - will be squared', size=25, key="-HABITAT_SIZE_LABEL-"), sg.Input('1000', size=25, key="-HABITAT_SIZE_INPUT-")],
        [sg.Text('Lower Life Forms Start %', size=25, key="-LLF_P_LABEL-"), sg.Input('50', size=25, key="-LLF_P_INPUT-")],
        [sg.Text('Lower Life Forms Regen Rate', size=25, key="-LLF_REGEN_LABEL-"), sg.Input('10', size=25, key="-LLF_REGEN_INPUT-")],
        [sg.Button('Create', size=20, key="-CREATE_BTN-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1), sg.Multiline(size=(40, 25), auto_refresh=True, write_only=True, key='-OUTPUT-', default_text="++ CURRENT HABITATS ++\n\n" + habs)]]


    # window Label
    window = sg.Window('CREATE HABITATS', layout)


    while True:
        event, values = window.read()
        print("events", event)
        print("values", values)

        if event == '-CREATE_BTN-':
    
            new_habitat = {
                'name': values['-HABITAT_NAME_INPUT-'],
                'size': values['-HABITAT_SIZE_INPUT-'],
                'llf_p': values['-LLF_P_INPUT-'],
                'llf_regen': values['-LLF_REGEN_INPUT-']
            }

            # function returns success or failure message 
            x = funcs.create_habitat(new_habitat)   

            window['-MSG-'].update(x[0], text_color=x[1], visible=True)

            habs = db_calls.list_habitats()
            window['-OUTPUT-'].update("++ CURRENT HABITATS ++\n\n" + habs)
            window.refresh()

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    create_habitat_window()