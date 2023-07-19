import PySimpleGUI as sg
import bartokmongo




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

