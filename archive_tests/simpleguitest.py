from time import sleep
import PySimpleGUI as sg

layout = [
    [sg.Text("alkows - mu")],
    [sg.Button("Start Model")],
    [sg.Button("Pause Model")],
    [sg.Button("Close")]
    ]

# create window
window = sg.Window("Demo", layout)

def count():
    for i in range(10):
        print (i)
        sleep(1)

while True:
    event, values = window.read()


    #end program is user closes window or ok btn
    if event == "Close" or event == sg.WIN_CLOSED:
        break

    if event == "Start Model":
        print("Start Model")
        count()


    if event == "Pause Model":
        print("Pause Model")




window.close()

