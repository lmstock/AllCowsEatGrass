import PySimpleGUI as sg
import logger2
import bartokmongo
import flora




def herbarium_window():
    print("herbarium_window")

    sg.theme('DarkBrown')

    

    col1 = [
        [sg.Text("HERBARIUM", font=14)],
        [sg.Text("click on individual to open more detail")],
        [sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
        [sg.Push(), sg.Button("Generate Random Flora"), sg.Text("number of Flora to generate: "), sg.InputText(default_text=5, key="-GEN_FLORA-", size=(20,20))],
        [sg.Button('mass extinction event', size=20, key="-MASS-")],
        [sg.Button('full extinction event', size=20, key="-FULL-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('HERBARIUM', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-GENERATE-':
            logger2.logger.info("Generate Random Flora")
            f_quantity = int(window["-FLORGEN-"].get())
            for i in range(f_quantity):
                flora.generate_random_flora()

        if event == '-MASS-':
            logger2.logger.info("Mass Species Extinction")
            bartokmongo.mass_extinction_event("herbarium", 75)

        if event == '-FULL-':
            logger2.logger.info("Full Extinction 100%")
            bartokmongo.full_extinction_event("herbarium")

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    herbarium_window()
