import PySimpleGUI as rsg
import os


txt="OS: "+os.name

def editfile(fname):
    if os.name == 'nt' :
        os.system("notepad "+fname)
        
    
    

layout = [
    [rsg.Text(txt) ],
    [rsg.Input(size=(25,1), key='-IN1')],
    [rsg.Text("Hallo", size=(25,1), key='-OUT1') ],
     [ rsg.Button('OK'),rsg.Button("Quit"),rsg.Button("Hey") ]
    ]
title = "HeRo-W"
window = rsg.Window(title, layout)
while True:
    answer, values = window.read()
    txt1 = answer + ': ' +values['-IN1']
    window['-OUT1'].update(txt1)
    if answer == rsg.WINDOW_CLOSED or answer == "Quit" :
        break
window.close()

fname=rsg.popup_get_file("Zu öffnende Date:")
#print(fname)
#print (str(type(fname)))

if not str(fname) == 'None' :
    editfile(fname)
    

#print("Auf Wiedersehen Welt")
rsg.popup("Auf Wiedersehen!")

