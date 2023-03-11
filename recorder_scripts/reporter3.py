
population_data1 = "C:\\Users\\michelle\\code\\bartok\\AllCowsEatGrass\\population_data_1.html"
title = "Alkows Population Data 1"
style_sheet = "style.css"


# setup page
def write_html_head(file_path, title, css):
    with open (file_path, "w") as dash:

        refresh = str(30)

        dash.write(
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js'></script>"
            "\t<head>\n"
            "\t\t<title>" + title + "</title>\n"
            '\t\t<link rel="stylesheet" href=' + css + '>\n'
            '\t\t<meta http-equiv="refresh" content=' + refresh + '>\n'
            "\t</head>\n"
        )

def write_page_head(file_path):
    with open (file_path, "a") as dash:
        dash.write(
            "<h1>Population Data</h1>\n"
        )


def build_graphs(file_path, chartId):
    with open (file_path, "a") as dash:

        # for each individual, create section
        dash.write(
            "<canvas id=" + chartId + ' style="width:100%;max-width:700px"></canvas>\n'
            "<script>\n"
            "const config = {\n"
            "type: 'line',\n"
            "data: data,\n"
            "};\n"

            
           
            "</script>"
            )



write_html_head(population_data1, title, style_sheet)
write_page_head(population_data1)



build_graphs(population_data1, "chart1")