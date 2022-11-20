from tkinter import *
fenster = Tk()
fenster.title("Window")

def switch():
    b1["state"] = DISABLED

def switch1():
    b1["state"] = ACTIVE

#--Buttons
b1=Button(fenster, text="Button")
b1.config(height = 5, width = 7)
b1.grid(row=0, column=0)    

b2 = Button(text="disable", command=switch)
b2.grid(row=0,column=1)
b2 = Button(text="active", command=switch1)
b2.grid(row=0,column=2)

fenster.mainloop()