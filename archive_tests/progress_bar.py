
import PySimpleGUI as sg
from time import sleep

layout = [
    [sg.Text("Progress Bar demo")],
    [sg.Text("number of ticks: "), sg.InputText(default_text=10, key="-COUNT-")],
    [sg.Button("Progress"), sg.ProgressBar(max_value=100, orientation='h', size=(20,20), key='-PROGRESS-')],  # have to set a value
    [sg.Button("Close")]
    ]

def update_tick(tick):
    tick = tick + 1
    sleep(1)
    return tick

window = sg.Window("Demo", layout, size=(600,600))

def main():
    tick = 0
    while True:
        event, values = window.read()
        
        if event == "Progress":
            
            count = int(window["-COUNT-"].get())
            window.refresh()

            for i in range(count):
                #tick = update_tick(tick) # use this to slow down for observation
                #print(i)

                window['-PROGRESS-'].update_bar(i+1, count)
                window.refresh()

        #end program is user closes window or ok btn
        if event == "Close" or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()