import PySimpleGUI as sg
import db_calls




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


if __name__ == "__main__":
    help()
