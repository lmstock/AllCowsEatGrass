import PySimpleGUI as sg
from random import randint

"""
This code uses OLD non-PEP8 compliant calls.  
If you see methods in PySimpleGUI code like DrawLine (CamelCaseName), this is what I mean by non-PEP8 compliant.
To convert this call to the PEP8 version, change it to draw_line  (snake_case_name)

"""

pause_image = b'iVBORw0KGgoAAAANSUhEUgAAADQAAAA0CAYAAADFeBvrAAAACXBIWXMAAAsSAAALEgHS3X78AAADImlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4wLWMwNjAgNjEuMTM0Nzc3LCAyMDEwLzAyLzEyLTE3OjMyOjAwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IE1hY2ludG9zaCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0QkUwMEQ2OTIyMjMxMUUxOTVGNkJDRjI4QkM3QjVBRiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0QkUwMEQ2QTIyMjMxMUUxOTVGNkJDRjI4QkM3QjVBRiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjRCRTAwRDY3MjIyMzExRTE5NUY2QkNGMjhCQzdCNUFGIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjRCRTAwRDY4MjIyMzExRTE5NUY2QkNGMjhCQzdCNUFGIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+DzEuSgAAAO5JREFUaN7t2jEOgkAQheGnsbDYPQBcY1rOs1fwLpxn270GHAAKCxIs1MQYYRWxwX8SqmEefJBQ7LIbx1Fbqr02VoAAAQK0bdDh3RNTSlVKqbrNvJobJA1d18W+7+NUjnOu8t5nc8wsmln8Kaiu65Ok4+14rrOkc9u2appm8kbKsqyKosjmhBC0BLT/EH+ceQi5/to5372hhwvN9Q8fgL7N4SsHCBAgQIAAAQIECBAgQIAAAQIECBAgQKuDBl0X0oeF/bVz/gP09oK4mcUQwn0mtz80meOci977bM6SrRRJ2vHjBSBAgAABAgTof0AXDgNUu7eUeewAAAAASUVORK5CYII='

play_image = b'iVBORw0KGgoAAAANSUhEUgAAADQAAAA0CAYAAADFeBvrAAAACXBIWXMAAAsSAAALEgHS3X78AAADImlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4wLWMwNjAgNjEuMTM0Nzc3LCAyMDEwLzAyLzEyLTE3OjMyOjAwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IE1hY2ludG9zaCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDoxNjZEMTFCMDFGQ0MxMUUxQTNFOTlDQTc5RkIwNzUyRiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDoxNjZEMTFCMTFGQ0MxMUUxQTNFOTlDQTc5RkIwNzUyRiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkY2NURGMzYxMUZDQjExRTFBM0U5OUNBNzlGQjA3NTJGIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkY2NURGMzYyMUZDQjExRTFBM0U5OUNBNzlGQjA3NTJGIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+8iA8qwAAAYxJREFUaN7t2j9ugzAchuEvFaMtdYyYGDsicQByk26cg3Nwlg7tXkscoJXoAh0t2YM3upiIoSilxX+gP0tWFhTx5MUgAqdxHHGkcYeDDQIRiEAEOjYoubWBECIXQuQA7u38tLMD0CmljNbauNrBsixxuVy2BTVN8wggs7O18wWAHIZB9n3vDFTX9bYgWyWznwBwBjAVyxljXZqm3byYUspEe8jNQJiBJhQ45y3n/FoMgIwddGtEVWwrUDTFEgffGbSYK1CwYomHo8BrMV8gb8US+B9Oi4UCOSsWArSqGGPMADB7Ay0W45zLvYGWijEADwCe7Nw16Gwxxq6rH4PojnX3d6wBxnRH/AbgHcDrEUDTWe7ZrqFdgeb/UXwopTqt9XQdWn2RTWIrorWWfd9fq2ito19DmxaJBbRYZA9nOadFQoGcFfEB8lrEF8hbERegoEVcgYIV+Q1I2l/7u6cPwYv8BZTNQNEUWQ0qiqKtqgoLhaR9PuRsB8uyXLX9iV68IBCBCEQgAhGIQP8H9AXLAmW9qCf8hgAAAABJRU5ErkJggg=='

BG_COLOR = 'DodgerBlue'
GRAPH_SIZE = (600,300)
TAC_SIZE = (300,300)
COL_ITEM_SIZE = 15
SAMPLES = 1000
GRAPH_STEP_SIZE = 5
model_dict = {'Item 1':'-R1-', 'Item 2':'-R2', 'Item 3':'-R3-'}
parm_dict = {'Item 1':'-R4-', 'Item 2':'-R5-', 'Item 3':'-R6-'}
data_set_dict = {'Item 1':'-R7-', 'Item 2':'-R8-', 'Item 3':'-R9-'}
more_parms_dict = {'Item 1':'-R10-', 'Item 2':'-R11-', 'Item 3':'-R12-'}

def ColumnParm(title, radio_group, radio_dict):
    layout = [[sg.Text(title,  size=(COL_ITEM_SIZE,1), justification='center', font='Current 14', background_color=BG_COLOR)]]
    for item, key in radio_dict.items():
        layout += [[sg.Radio(item, group_id=radio_group, key=key, size=(COL_ITEM_SIZE,1))]]
    return sg.Frame('',layout, )

sg.theme('LightGreen')

layout = [  [sg.Text('My PSG Dashboard', justification='center', font='default 25', background_color=BG_COLOR, expand_x=True)],
            [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='-GRAPH-', background_color='lightblue')],
            [ColumnParm('Model', 1, model_dict), ColumnParm('Parameter', 2, parm_dict),ColumnParm('Data Set', 3, data_set_dict),ColumnParm('More Parameteres', 4, more_parms_dict),   ],
            [sg.Button('',image_data=play_image, button_color=sg.COLOR_SYSTEM_DEFAULT, key='-PLAY-'),
             sg.Button('', button_color=sg.COLOR_SYSTEM_DEFAULT, image_data=pause_image, key='-PAUSE-'),
             sg.ProgressBar(SAMPLES,orientation='h', size=(40,30), key='-PROGRESS-')]  ]

window = sg.Window('PSG Dashboard Example For Reddit', layout)

sample_num = x = lastx = lasty = 0
paused = False
while True:                             # Event Loop
    event, values = window.read(timeout=20)
    if event is None:
        break
    paused = paused if event not in ('-PAUSE-', '-PLAY-') else event == '-PAUSE-'
    if paused:
        continue
    y = randint(0,GRAPH_SIZE[1])        # get random point for graph
    if x < GRAPH_SIZE[0]:               # if still drawing initial width of graph
        window['-GRAPH-'].draw_line((lastx, lasty), (x, y), width=2)
    else:                               # finished drawing full graph width so move each time to make room
        window['-GRAPH-'].Move(-GRAPH_STEP_SIZE, 0)
        window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=2)
        x -= GRAPH_STEP_SIZE
    window['-PROGRESS-'].UpdateBar(sample_num % SAMPLES)
    lastx, lasty = x, y
    sample_num += 1
    x += GRAPH_STEP_SIZE
window.close()