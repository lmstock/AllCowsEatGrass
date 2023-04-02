from time import sleep
import PySimpleGUI as sg

import game_conf
import scheduler
import logger2
import mongotest
import creature
import creature_species
import flora
import flora_species
import collection_window





sg.theme('Green')

start_tick = game_conf.w.current_tick


# pysimplegui - your layout is a list of lists 
layout = [
    [sg.Text("ALKHOUS - CONTROL"), sg.Text(start_tick, key="-TICK-")],

    [sg.Push(), sg.Text("number of ticks to run: "), sg.InputText(size=(20,20), default_text=5, key="-COUNT-")], [sg.Push(), sg.Button("Run Model"), sg.ProgressBar(10, orientation='h', size=(50,8), key='-PROBAR-')],

    [sg.Push(), sg.Text("number of creatures to generate: "), sg.InputText(default_text=2, key="-CRETGEN-", size=(20,20)), sg.Button("Generate Random Creatures")],
    [sg.Push(), sg.Text("number of flora to generate: "), sg.InputText(default_text=3, key="-FLORGEN-", size=(20,20)), sg.Button("Generate Random Flora")],
    [sg.Push(), sg.Text("number of Species to generate: "), sg.InputText(default_text=4, key="-CRETSPECGEN-", size=(20,20)), sg.Button("Generate Creature Species")],
    [sg.Push(), sg.Text("number of flora Species to generate: "), sg.InputText(default_text=4, key="-FLORSPECGEN-", size=(20,20)), sg.Button("Generate Random Flora Species")],
    [sg.Button("Bestiary"), sg.Button("Herbarium"), sg.Button("Flora Pop"), sg.Button("Cret Pop")],
      
    [sg.Button("Close")]
    ]

# create window
window = sg.Window("Demo alkows - mu", layout)

def run_model():
        game_conf.w.increment_tick()
        scheduler.scheduler_run()
        #mongotest.manage_hist()
        game_conf.w.update_world()



def model_main(window):
    while True:
        event, values = window.read()
        print(event, values)
        

        #end program is user closes window or ok btn
        if event == "Close" or event == sg.WIN_CLOSED:
            break

        if event == "Generate Random Creatures":
            logger2.logger.info("Generate Random Creatures")
            c_quantity = int(window["-CRETGEN-"].get())
            for i in range(c_quantity):
                creature.generate_creature(creature.get_random_creature_type())

        if event == "Generate Random Flora":
            logger2.logger.info("Generate Random Flora")
            f_quantity = int(window["-FLORGEN-"].get())
            for i in range(f_quantity):
                flora.generate_random_flora()

        if event == "Generate Creature Species":
            logger2.logger.info("Generate Creature Species")
            cs_quantity = int(window["-CRETSPECGEN-"].get())
            for i in range(cs_quantity):
                creature_species.generate_creature_species()

        if event == "Generate Random Flora Species":
            logger2.logger.info("Generate Flora Species")
            fs_quantity = int(window["-FLORSPECGEN-"].get())
            for i in range(fs_quantity):
                flora_species.generate_flora_species()

        if event == "Bestiary":
            logger2.logger.info("bestiary_window")
            bestiary = mongotest.get_bestiary()
            collection_window.open_collection_window(bestiary)

        if event == "Herbarium":
            logger2.logger.info("herbarium_window")
            herbarium = mongotest.get_herbarium()
            collection_window.open_collection_window(herbarium)

        if event == "Cret Pop":
            logger2.logger.info("cret pop")
            cret_census = mongotest.get_cret_census()
            collection_window.open_collection_window(cret_census)

        if event == "Flora Pop":
            logger2.logger.info("flora pop")
            flora_census = mongotest.get_flora_census()
            collection_window.open_collection_window(flora_census)


        if event == "Run Model":
            print("\n")
            
            logger2.logger.info("\033[01m === Run Model === \033[0m")

            count = int(window["-COUNT-"].get())
            window.refresh()

            for i in range(count):
                run_model()
                window['-PROBAR-'].update_bar(i+1, count)
                window['-TICK-'].update(game_conf.w.current_tick)

            logger2.logger.info("\033[01m === End Model Run === \033[0m")
            print("\n")


        if event == "Pause Model":
            print("Pause Model")




    window.close()


model_main(window)