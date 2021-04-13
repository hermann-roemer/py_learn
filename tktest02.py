import time as tm
import sys,datetime
from tkinter import *
from tkinter import messagebox



# Handler f. Escape auf root-Fenster
def esc_on_mr(self):
    print("ESC pressed...")
    tm.sleep(3)
    print("Bye...")
    # messagebox.showinfo("Info", "Info: Quitting ...")
    # messagebox.showerror("Error", "Just an Error Message...")
    messagebox.showwarning("Warning", "Just a Warning...")
    sys.exit(0)

# Callback-Routine für "Send" - Button
def snd_bt(event):
    if event.num == 1:
        bt="L"
    elif event.num == 2:
        bt="M"
    elif event.num == 3:
        bt="R"
    else:
        bt="ERROR"
    #print ("HEY")
    mtxt_append(minp01.get())

# Callback-Routine für "Clear" - Button
def clr_bt(event):
    mtxt01.delete('1.0',END)
    minp01.delete('0',END)

# Callback-Routine für "Quit" - Button
def q_bt(event):
    print ("Quit...")
    sys.exit()

def msg_bt(event):
    print(scvar.get())
    messagebox.showinfo("Info", "Passwort:  "+pwvar.get())
    pwin.delete('0',END)

def mtxt_append(txt):
    idx=END
    mtxt01.insert(idx, txt+"\n")
    minp01.delete('0',END)
    
    

# "Root"- Fenster / App "myroot"/mr
mr=Tk()
mr.title('Python - tkinter Sample 02')
mr.geometry("500x300+1000+550")
mr.bind('<Escape>',esc_on_mr)

scvar=DoubleVar()
pwvar=StringVar()

# Label (Textfeld)
lbl=Label(mr, height=3,width=30,text="======= Hello World =====\n"+datetime.datetime.now().strftime("=%A, %d.%m.%Y, %H:%M =")+"\n"+20*'=' )
lbl.place(x=6,y=10)

# Input-Feld und dazugehoeriges Label
ilbl01=Label(mr,width=10,text="Input:")
ilbl01.place(x=40,y=70)

minp01=Entry(mr, width=50)
minp01.place(x=100,y=70)

#Ausgabefeld
mtxt01=Text(mr,height= 4, width=42 )
mtxt01.place( x=70, y=110 )
mtxt01.insert(INSERT, 'Hallo...\nAlle\n')
ln=0


# Button "Send" 
sndbt=Button(mr,text="Send")
sndbt.bind('<Button>',snd_bt)
sndbt.place(x=10,y=260)

# Button "Clear"
clrbt=Button(mr,text="Clear")
clrbt.bind('<Button>',clr_bt)
clrbt.place(x=60, y=260)

# Button "Quit"
qbt=Button(mr, text="Quit")
qbt.place(x=460,y=260)
qbt.bind('<Button>',q_bt)

# Message Button
msgbt=Button(mr, text="Info")
msgbt.bind('<Button>',msg_bt)
msgbt.place(x=300,y=260)

sc01=Scale(mr, from_=0, to=10, variable = scvar)
sc01.place(x=450, y=30)

pwlb=Label(mr, width=5, text='Pwd: ')
pwlb.place(x=40, y=200)
pwin=Entry(mr, width=20, textvariable=pwvar, show='*', )
pwin.place(x=100, y=200)

frm=Frame(mr)
frm.place(x=240, y=10)

#lbl02=Label(frm, text= "Ein beliebiger Text")
#img01=PhotoImage(frm,file='C:\User\Hermann\devel\git_test\py_learn\bild01.png')
img01=PhotoImage(file='smiley03.png')

lbf=Label(frm,image=img01,width=150,height=50)
#lbl02.pack()
# lbf.place(x=0,y=0)
lbf.pack()
        

#lbl02.pack()

mr.mainloop()