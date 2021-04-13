import PySimpleGUI as rsg
import subprocess
from subprocess import PIPE
import os
import time
import sys
#import sh

def osdetect():
    result = "None"
    if sys.platform.lower().find('win') >= 0:
        result = 'Windows-System'
    #        os.system(command)
    elif sys.platform.lower().find('linux') >= 0:
        result = 'Linux-System'
    return result

def get_ip_info_cmd(platform):
    result="None"
    command = 'None'
    if osdetect() == 'Windows-System':
        command = 'ipconfig'
#        result = subprocess.getoutput(command)
#        os.system(command)
    elif osdetect() == 'Linux-System':
        command = 'ifconfig'
#     result=subprocess.getoutput(command)
    return command

def get_ip_info(platform):
    result = "None"
    mysubprocess=subprocess.Popen(get_ip_info_cmd(osdetect()),stdout=PIPE,stderr=PIPE)
    output,error=mysubprocess.communicate()
    return output.decode()


txt="Program: "+sys.argv[0]
print(txt)
platform = osdetect()
ip_info_cmd = get_ip_info_cmd(platform)
print("Hey, dies ist ein "+platform+" der ip_info-Befehl ist "+ip_info_cmd)
print(get_ip_info(platform))


layout = [ [rsg.Text(txt) ],
           [rsg.Text("Patform: "+osdetect()+" ip_info_cmd: "+ip_info_cmd)],
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
#        sh.ipconfig()
#        os.system("date")
 #       window['-ML1'].restore_std_out()
#        print ("====")
    elif answer == "IpInfo":
        window['-ML1'].reroute_stdout_to_here()
        print(str(get_ip_info(platform)))
#        print(platform)
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


