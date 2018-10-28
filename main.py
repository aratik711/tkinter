from tkinter import *

def kg_convert():
    print(kg_value.get())
    t1.delete("1.0", END)
    t1.insert(END,float(kg_value.get())*1000)
    t2.delete("1.0", END)
    t2.insert(END,float(kg_value.get())*2.20462)
    t3.delete("1.0", END)
    t3.insert(END,float(kg_value.get())*35.274)

window=Tk()
window.geometry('300x100')

l1 = Label(window, text="Kg")
l1.grid(row=0,column=0)

kg_value=StringVar()
e1=Entry(window,textvariable=kg_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Calculate",command=kg_convert)
b1.grid(row=0,column=2)


t1=Text(window,width=10,height=1)
t1.grid(row=1,column=0)

t2=Text(window,width=10,height=1)
t2.grid(row=1,column=1)

t3=Text(window,width=10,height=1)
t3.grid(row=1,column=2)

window.mainloop()
