import PySimpleGUI as rsg

layout = [
    [rsg.Text("Hallo Welt")],
    [rsg.Button('OK'), rsg.Button("Quit")],
    [rsg.Button("Hey")]
    ]
title = "HeRo-W"
window = rsg.Window(title, layout)
while True:
    
    answer, value = window.read()
    print(answer)

    if answer == rsg.WINDOW_CLOSED or answer == "Quit" :
        break
