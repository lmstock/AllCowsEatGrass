import species
import game_conf


import flora_species
import scheduler


# write html file with game data

title = "Alkows Compendium"
style_sheet = "style.css"


r_bestiary = species.bestiary
r_herbarium = flora_species.herbarium
r_population = scheduler.population
r_flora_population = scheduler.flora_population

file_path = "C:\\Users\\michelle\\code\\bartok\\AllCowsEatGrass\\compendium.html"

r_bestiary_headers = ["species_id", "name", "head", "size", "body_type", "rest", "base_fatigue", "rest_gain", "speed"]
r_herbarium_headers = ["species_id", "name", "size", "type", "energy", "growth_data"]
r_population_headers = ["creature_id", "type", "age", "rest", "rest_gain", "size", "sleep_dur", "health", "energy", "satiety", "hostility", "fov", "world_coords", "task_q", "active_task"]
r_flora_population_headers = ["flora_id", "type", "age", "energy", "coords"]


def write_html_head(file_path, title, css):
    with open (file_path, "w") as dash:

        refresh = str(10)

        dash.write(
            "<!DOCTYPE html>\n"
            "<html>\n"
            "\t<head>\n"
            "\t\t<title>" + title + "</title>\n"
            '\t\t<link rel="stylesheet" href=' + css + '>\n'
            '\t\t<meta http-equiv="refresh" content=' + refresh + '>\n'
            "\t</head>\n"
        )

def body_html(file_path, title):
    with open(file_path, "a") as dash:

        dash.write(
            "\t<body>\n"
            "\t\t<h1>" + title + "</h1>\n"  
            "\t\t<p> current_tick:  " + str(game_conf.g.current_tick) + "</p>\n"
        )

def append_html_tables(file_path, this_dict, header_list, table_name):
    with open(file_path, "a") as dash:

        x = bool(this_dict)
        if x == False:
            pass

        else: 
            dash.write(
                "\t\t<p class='table_label'> " + table_name + "</p>\n"
                "\t\t\t<table>\n"
                "\t\t\t\t<tr>\n"
                )

            # write table headers
            for i in header_list:
                dash.write(
                    "\t\t\t\t\t<th>" + i + "</th>\n"
                )

            # end table row
            dash.write("\t\t\t\t</tr>\n")

            # get table header map
            def map_header_order(listz):
                map = {}
                ct = 0
                for i in listz:
                    map[i] = ct
                    ct = ct + 1
                return map

            header_map = map_header_order(header_list)

            # k is the species or creature / row
            for k in this_dict.items():
                row = []

                # adds a new row for each key
                dash.write("\t\t\t\t<tr>\n")

                # ids the map item we are looking for first
                for j in header_map.items():

                    # match it with ks attribute list
                    for l in k[1].items():
                        
                        # when match append row
                        if l[0] == j[0]:
                            row.append(l[1])
                
                # adds data to row
                for i in row:
                    d = str(i)
                    dash.write(str("\t\t\t\t\t<td>" + d + "</td>\n"))
                
                # end of row
                dash.write("\t\t\t\t</tr>\n")

            dash.write(
                "\t\t\t</table>"
                "<br>\n"
                )


        
def write_html():

    if game_conf.g.current_tick < 5:
        pass
    else: 

        write_html_head(file_path, title="Alkows", css='"style.css"')

        body_html(file_path, title)

        append_html_tables(file_path, r_bestiary, r_bestiary_headers, table_name="BESTIARY")
        append_html_tables(file_path, r_herbarium, r_herbarium_headers, table_name="HERBARIUM")
        append_html_tables(file_path, r_population, r_population_headers, table_name="POPULATION")
        append_html_tables(file_path, r_flora_population, r_flora_population_headers, table_name="FLORA POPULATION")