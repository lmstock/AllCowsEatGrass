import species
import flora_species
import scheduler
import game_setup
import pprint

# write html file with game data

tab_title = "Alkows Test Dash"
style_sheet = "style.css"

page_title = "Alkows Trest Dasch"
r_bestiary = species.bestiary
r_herbarium = flora_species.herbarium
r_population = scheduler.population
r_flora_population = scheduler.flora_population


def write_html():

    with open("C:\\Users\\michelle\\code\\bartok\\AllCowsEatGrass\\page2.html", "w") as dash:

        dash.write(
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "<title>" + tab_title + "</title>\n"
            '<link rel="stylesheet" href=' + style_sheet + '>\n'
            '<meta http-equiv="refresh" content="10">\n'
            "</head>\n"
            "<body>\n"
            "<h2>" + page_title + "</h2>\n"

            "<p>" + str(game_setup.turn) + "</p>\n"
            "<p> BESTIARY </p>\n"
            )
        
        for i in r_bestiary.items():
            dash.write("<p>" + str(i) + "</p>\n")

        dash.write(
            "<p> HERBARIUM </p>\n"            
        )

        for i in r_herbarium.items():
            dash.write("<p>" + str(i) + "</p>\n")

        dash.write(
            "<p> POPULATION </p>\n"            
        )

        for i in r_population.items():
            dash.write("<p>" + str(i) + "</p>\n")

        dash.write(
            "<p> FLORA POPULATION </p>\n"            
        )

        for i in r_flora_population.items():
            dash.write("<p>" + str(i) + "</p>")