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
import compendiums
import census_data





sg.theme('Green')

start_tick = game_conf.w.current_tick


# pysimplegui - your layout is a list of lists 
layout = [
    [sg.Text("ALKHOUS - CONTROL"), sg.Text(start_tick, key="-TICK-")],

    [sg.Push(), sg.Text("number of ticks to run: "), sg.InputText(size=(20,20), default_text=100, key="-COUNT-")], [sg.Push(), sg.Button("Run Model"), sg.ProgressBar(10, orientation='h', size=(50,8), key='-PROBAR-')],

    [sg.Push(), sg.Text("number of Species to generate: "), sg.InputText(default_text=10, key="-CRETSPECGEN-", size=(20,20)), sg.Button("Generate Creature Species")],
    [sg.Push(), sg.Text("number of Creatures to generate: "), sg.InputText(default_text=5, key="-CRETGEN-", size=(20,20)), sg.Button("Generate Random Creatures")],
    [sg.Push(), sg.Text("number of Flora Species to generate: "), sg.InputText(default_text=10, key="-FLORSPECGEN-", size=(20,20)), sg.Button("Generate Random Flora Species")],
    [sg.Push(), sg.Text("number of Flora to generate: "), sg.InputText(default_text=5, key="-FLORGEN-", size=(20,20)), sg.Button("Generate Random Flora")],
    
    
    [sg.Button("View Bestiary", size=(28,1)), sg.Button("Full Species Extinction 100%", size=(28,1)), sg.Button("Mass Species Extinction", size=(28,1))],
    [sg.Button("Creature Census data", size=(28,1)), sg.Button("Full Creature Culling 100%", size=(28,1)), sg.Button("Mass Creature Culling", size=(28,1))], 
    [sg.Button("View Herbarium", size=(28,1)), sg.Button("Full Flora Species Extinction 100%", size=(28,1)), sg.Button("Mass Flora Species Extinction", size=(28,1))],
    [sg.Button("Flora Census data", size=(28,1)), sg.Button("Full Flora Culling 100%", size=(28,1)), sg.Button("Mass Flora Culling", size=(28,1))], 
      
    [sg.Button("Close")]
    ]

# create window
window = sg.Window("Demo alkows - mu", layout)

def run_model():
        game_conf.w.increment_tick()
        scheduler.scheduler_run()
        game_conf.w.update_world()
        compendiums.compendium_report()
        census_data.census_report()


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

        if event == "View Bestiary":
            logger2.logger.info("bestiary_window")
            bestiary = mongotest.get_bestiary()
            collection_window.open_collection_window(bestiary)

        if event == "View Herbarium":
            logger2.logger.info("herbarium_window")
            herbarium = mongotest.get_herbarium()
            collection_window.open_collection_window(herbarium)

        if event == "Creature Census data":
            logger2.logger.info("cret pop")
            cret_census = mongotest.get_cret_census()
            collection_window.open_collection_window(cret_census)

        if event == "Flora Census data":
            logger2.logger.info("flora pop")
            flora_census = mongotest.get_flora_census()
            collection_window.open_collection_window(flora_census)

        if event == "Full Species Extinction 100%":
            logger2.logger.info("Full Species Extinction 100%")
            mongotest.full_extinction_event("bestiary")

        if event == "Mass Species Extinction":
            logger2.logger.info("Mass Species Extinction")
            mongotest.mass_extinction_event("bestiary", 75)

        if event == "Full Creature Culling 100%":
            logger2.logger.info("Full Creature Extinction 100%")
            mongotest.full_extinction_event("population")

        if event == "Mass Creature Culling":
            logger2.logger.info("Mass Creature Culling")
            mongotest.mass_extinction_event("population", 75)

        if event == "Full Flora Species Extinction 100%":
            logger2.logger.info("Full Creature Extinction 100%")
            mongotest.full_extinction_event("herbarium")

        if event == "Mass Flora Species Extinction":
            logger2.logger.info("Mass Flora Species Extinction")
            mongotest.mass_extinction_event("herbarium", 75)

        if event == "Full Flora Culling 100%":
            logger2.logger.info("Full Creature Extinction 100%")
            mongotest.full_extinction_event("flora_pop")

        if event == "Mass Flora Culling":
            logger2.logger.info("Mass Flora Culling")
            mongotest.mass_extinction_event("flora_pop", 75)



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







    window.close()


model_main(window)