import PySimpleGUI as rsg
import os
import subprocess
import time
import sys

txt="OS: "+os.name

def ip_info():
    result="None"
    if sys.platform == 'win32' :
        command='ipconfig'
#        os.system(command)
    elif sys.platform == 'linux2':
        command=ifconfig
        
    result=subprocess.getoutput(command)
    return result

print("Hey")
layout = [ [rsg.Text(txt) ],
           [rsg.Output(size=(60,5),key='-OUT1') ],
           [rsg.HorizontalSeparator()],  
           [rsg.Multiline( size=(60,20), key='-ML1', reroute_stdout=False) ],           
           [
             rsg.Button("IpInfo"),rsg.Button("Hey"), rsg.Button("Clear"), 
             rsg.Button('OK'),rsg.Button("Quit"),
           ]
         ]

title = "HeRo-W"
o_stdout=sys.stdout
window = rsg.Window(title, layout,resizable=True)
cnt=0
while True:
    cnt = cnt + 1
    answer, values = window.read(timeout=20000)
    print (str(answer)+":("+str(cnt)+")")

    if answer == "Clear":
        window['-ML1'].update("---cleared---\n")
        cnt=0
#        window['-ML1'].restore_stdout()        
    elif answer == "Hey":
        print ("==HEY==")
#        os.system("date")
 #       window['-ML1'].restore_std_out()
#        print ("====")
    elif answer == "IpInfo":
        window['-ML1'].reroute_stdout_to_here()
        print(ip_info())
        window['-ML1'].restore_stdout()
    elif answer == rsg.WINDOW_CLOSED or answer == "Quit" :
 #       window['-ML1'].restore_stdout()
        break
    elif answer == "__TIMEOUT__":
        rsg.popup("Aufwachen ...")
        
print("BYE")
#time.sleep(2)
window.close()
sys.stdout=o_stdout
#time.sleep(5)
print("Auf Wiedersehen Welt")


