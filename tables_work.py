import bartokmongo




# write html file with game data
# titles
compendium_title = "Alkows Compendium"
pop_title = "Alkows Compendium"

# css
style_sheet = "style.css"

# file paths
compendium3 = "C:\\Users\\michelle\\code\\bartok\\AllCowsEatGrass\\test_compendium3.html"


# db functions
bestiary = bartokmongo.get_bestiary()
herbarium = bartokmongo.get_herbarium()

# headers
bestiary_headers = ["_id", "phylum", "class", "species_type", "size", "body_type", "mutable_traits", "mutation_count", "description"]
herbarium_headers = ["_id", "flora_species_type", "size", "energy", "growth_data"]


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
            for k, v in this_dict.items():
                row = []

                # adds a new row 
                dash.write("\t\t\t\t<tr>\n")

                print(header_list)
                print(v.keys())
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



def compendium_report():

    write_html_head(compendium3,compendium_title,style_sheet)
    body_html(compendium3,compendium_title)

    append_html_tables(compendium3, bestiary, bestiary_headers, "bestiary")
    append_html_tables(compendium3, herbarium, herbarium_headers, "herbarium")

compendium_report()