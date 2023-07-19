import PySimpleGUI as sg
import bartokmongo


def create_window():

    table_headers = ["id", "species_type", "phylum", "size", "exoskeleton_color", "eyes", "legs"]
    bestiary = bartokmongo.get_bestiary()

    def get_rows():
        rows = []
        for i in bestiary:
            row = []
            for k,v in i.items():
                row.append(v)
            rows.append(row)
        return rows

    print (bestiary)
    rows = get_rows()

    table = sg.Table(headings=table_headers, values=rows[:][:], auto_size_columns=True, justification='center', key="-TABLE-", vertical_scroll_only=False, expand_x=True, expand_y=True, enable_click_events=True, display_row_numbers=True)
    col1 = [
        [table]
    ]

    layout = [[sg.Column(col1)]]

    # window Label
    window = sg.Window('POPULATION', layout)


    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break


        window.close()

if __name__ == "__main__":
    create_window()


create_window()