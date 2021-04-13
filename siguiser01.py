import PySimpleGUI as rsg
import serial,time,os,sys
import subprocess
from subprocess import PIPE
#import os
#import time
#import sys
#import sh

def osdetect():
    result = "None"
    if sys.platform.lower().find('win') >= 0:
        result = 'Windows-System'
    #        os.system(command)
    elif sys.platform.lower().find('linux') >= 0:
        result = 'Linux-System'
    return result

serport='/dev/ttyUSB0'
sertmout=10

# Window Input timeout in ms 
wtmout=60000

try:
    ser=serial.Serial(serport, 9600, timeout=sertmout )
except:
    print("Error opening "+serport)
    quit()
print("opened serial Port "+ser.name+"with timeout "+str(sertmout))

    
txt="Program: "+sys.argv[0] +"\tPlatform: "+ "\tDevice: "+ser.name+"\ttimeout: "+str(sertmout)
print(txt)
platform = osdetect()

layout = [ [rsg.Text(txt) ],
           [rsg.Input("show ?", size=(60,5),key='-IN1') ],
           [rsg.HorizontalSeparator()],  
           [rsg.Multiline( size=(60,20), key='-ML1', reroute_stdout=False,autoscroll=True,auto_refresh=True) ],           
           [
             rsg.Button("Send"), rsg.Button("Clear"),rsg.Button("Quit"),
           ]
         ]

title = "HeRo-W"
o_stdout=sys.stdout
window = rsg.Window(title, layout,resizable=True)
cnt=0

while True:
    cnt = cnt + 1
    answer, values = window.read(timeout=wtmout)
#    print ("Answer: "+str(answer)+"-Count:("+str(cnt)+")")
#    print (values)
    if answer == "Send":
#        print("DEBUG")
        sendstr = values['-IN1'] +'\n'
        print(sendstr)
        ser.write(sendstr.encode())
        time.sleep(1)
#        print(".")
        window['-ML1'].reroute_stdout_to_here()
        ln=''
        while True:
          ch=ser.read()
          if len(ch) == 0:
              print("Timed out...\nLast (uncomplete) Line: " + ln )
              ser.write(b'\nTimed out... closing Connection\n')
              break
          try:
              dch=ch.decode()
          except:
              ch=b'*'
          if ch == b'\r'or ch == b'\n':
              print ("Got Line: " + ln)
              ln=''
          else:
              ln = ln + dch
 #         print(ln)
        window['-ML1'].reroute_stdout_to_here()
        print("Bye")
    elif answer == rsg.WINDOW_CLOSED or answer == "Quit" :
        window['-ML1'].restore_stdout()
        break
    elif answer == "Clear":
        window['-ML1'].Update('----cleared----')
        window['-ML1'].restore_stdout()
        print("cleared ML1")
        sys.stdout=o_stdout
        print("restored")
    elif answer == "__TIMEOUT__":
        rsg.popup("Aufwachen ...")
    else:
        print("#")
        continue
       
print("BYE")
#time.sleep(2)
window.close()
ser.close
sys.stdout=o_stdout
#time.sleep(5)
print("Auf Wiedersehen Welt")


