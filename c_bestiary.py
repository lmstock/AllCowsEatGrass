import PySimpleGUI as sg
import logger2
import bartokmongo
import creature_species




def bestiary_window():
    print("bestiary_window")

    sg.theme('DarkBrown')

    table_headers = ["species_type", "phylum", "size", "exoskeleton_color", "eyes", "legs"]
    
    def get_rows():
        rows = []
        for i in bestiary:
            row = []
            for k,v in i.items():
                row.append(v)
            rows.append(row)
        return rows

    col1 = [
        [sg.Text("BESTIARY", font=14)],
        [sg.Text("click on individual to open more detail")],
        [sg.Table([[1,2,3], [4,5,6]], num_rows=2, headings=table_headers)],
        [sg.Push(),  sg.Button("Generate Creature Species", size=20, key="-GENERATE-"), sg.Text("number of Species to generate: "), sg.InputText(default_text=10, key="-GEN_SPECIES-", size=(20,20))],
        [sg.Button('mass extinction event', size=20, key="-MASS-")],
        [sg.Button('full extinction event', size=20, key="-FULL-")],
        [sg.Button('Exit', size=20, key="-EXIT-")]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('BESTIARY', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == '-GENERATE-':
            logger2.logger.info("Generate Creature Species")
            cs_quantity = int(window["-GEN_SPECIES-"].get())
            for i in range(cs_quantity):
                creature_species.generate_creature_species()

        if event == '-MASS-':
            logger2.logger.info("Mass Species Extinction")
            bartokmongo.mass_extinction_event("bestiary", 75)

        if event == '-FULL-':
            logger2.logger.info("Full Extinction 100%")
            bartokmongo.full_extinction_event("bestiary")

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


    window.close()

if __name__ == "__main__":
    bestiary_window()
