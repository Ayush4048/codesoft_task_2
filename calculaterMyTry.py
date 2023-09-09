from tkinter import *
def click(event):
    global value
    text=event.widget.cget("text")
    if text=="=":
        if value.get().isdigit():
            Newvalue=int(value.get())
        else:
            try:
                Newvalue=eval(display.get())
            except Exception as e:
                value.set("error")
        value.set(Newvalue)

    elif text=="c":
        value.set("")
        #display.update()
    else:
        value.set(value.get()+text)
        #display.update()   
windows=Tk()
windows.geometry("550x750")
windows.maxsize(550,750)
windows.title("Calculater")
value=StringVar()
value.set("")
display=Entry(windows,textvar=value,font=("serif",40,"bold"))
display.pack(fill=X,ipadx=20,ipady=20,padx=10)
l1=["1","2","3","4","5","6","7","8","9","0","_","+","x"," /"," %","c","=","00"]
x=0
for i in range(6):
    fr=Frame(windows,bg="black")
    for j in range(3):
        b1=Button(fr,text=f"{l1[x]}", font="lucida 32 bold" ,padx=55,pady=0,bg="light grey" )
        b1.pack(side=LEFT,ipadx=10,ipady=10)
        b1.bind(f"<Button-1>",click)
        x+=1
    fr.pack(fill=X,side=TOP)
windows.mainloop()