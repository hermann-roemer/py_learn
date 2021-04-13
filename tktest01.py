from tkinter import *
import datetime

dtm=datetime.datetime.now().strftime("==%A, %d.%m.%Y, %H:%M ==")

global ln
ln=0
print(ln)


def okbtn_pressed(xxx):
    ln=3
    
    if xxx.num == 1:
        txt = "LB"
        
    elif xxx.num == 2:
       txt = "MB"
       
    elif xxx.num ==3:
       txt = "RB"
    else:
        txt = "Hääää??"
    txt = txt +": "+ minp01.get()
    print ( txt)
    # idx=str(ln)+'.2'
    idx=END
# printing one line (at the END) to the Text ...)    
    mtxt01.insert(idx, txt+"\n")
    
    
    
    print("::"+etxt.get())
# deleting content of the Entry
    minp01.delete('0',END)
    

def qbtn_pressed(event):
    if event.num == 1 or event.num == 3 :
        print("Quitting...")
        import sys
        quit()

    
myapp=Tk()
etxt=StringVar()
myapp.title("Hermanns TK Window")
myapp.geometry("500x300+1000+500")

#frm01=Frame(myapp)
#frm01.pack

tlabel01=Label(myapp,text = "Hello World : ")
tlabel01.place(x=0,y=40)
# tlabel01.pack()

mlb02=Label(myapp,text=dtm)
mlb02.place(x=120,y=10)

minp01=Entry(myapp, width=60)
minp01.place(x=100,y=40)

mtxt01=Text(myapp,height= 10, width=40 )
mtxt01.place( x=40, y=80 )
mtxt01.insert(INSERT, 'Hallo...\nAlle\n')
ln=0

okbtn=Button(myapp, text="OK")
okbtn.place(x=10,y=260)
okbtn.bind('<Button>',okbtn_pressed)


qbtn=Button(myapp, text="Quit")
qbtn.place(x=460,y=260)
qbtn.bind('<Button-1>',qbtn_pressed)
#qbtn.pack( )

myapp.mainloop()

print("BYE...")