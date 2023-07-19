
import game_conf
import bartokmongo
import shutil
import logger2


# write html file with game data
# titles
compendium_title = "Alkows Census Data"
pop_title = "Alkows Census Data"

# css
style_sheet = "style.css"

# file paths
census3 = "file path"
cp_census3 = "file path"

# db functions


# headers
cret_pop_headers = ["_id", "phylum", "class","species_type", "size", "age", "x", "y", "active_task", "task_q", "reproduction", "offspring", "mutable_traits", "energy", "satiety", "hostility", "health"]
flora_pop_headers = ["_id", "flora_species_type", "size", "age", "energy", "growth_data", "x", "y", "offspring"]


# setup page
def write_html_head(file_path, title, css):
    with open (file_path, "w") as dash:

        refresh = str(30)

        dash.write(
            "<!DOCTYPE html>\n"
            "<html>\n"
            "\t<head>\n"
            "\t\t<title>" + title + "</title>\n"
            '\t\t<link rel="stylesheet" href=' + css + '>\n'
            '\t\t<meta http-equiv="refresh" content=' + refresh + '>\n'
            "\t</head>\n"
        )

# set title and current tick
def body_html(file_path, title):
    with open(file_path, "a") as dash:

        dash.write(
            "\t<body>\n"
            "\t\t<h1>" + title + "</h1>\n"  
            "\t\t<p> current_tick:  " + str(game_conf.w.current_tick) + "</p>\n"
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



            # k is the species or creature / row
            for k,v in this_dict.items():
                row = []

                # adds a new row for each key
                dash.write("\t\t\t\t<tr>\n")

                for h in header_list:

                    if h not in v.keys():
                        row.append("na")

                    for vi in v.items():
                            
                        if vi[0] == h:
                            row.append(vi[1])
                
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


def census_report():
    logger2.logger.debug("census_report")

    pop = bartokmongo.get_cret_census()
    flora_pop = bartokmongo.get_flora_census()
    
    write_html_head(census3,compendium_title,style_sheet)
    body_html(census3,compendium_title)

    append_html_tables(census3, pop, cret_pop_headers, "creature census")
    append_html_tables(census3, flora_pop, flora_pop_headers, "flora census")

    shutil.copyfile(census3, cp_census3)

