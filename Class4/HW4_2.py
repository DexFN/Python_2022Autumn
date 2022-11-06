from tkinter import *
import datetime as d
today=d.date.today()
root=Tk()
root.geometry('400x400+150+200')
root.title("Class4_HW2")
birth=Entry(root,font=('Arial',18))
Label(root, text="Enter you birth date: \n Input format is yyyy.mm.dd", fg = "Orange", font = ("Arial",18)).pack()
def clicked():
    birth1=birth.get().split(".")
    Year = today.year - int(birth1[0])              
    Month = today.month - int(birth1[1])
    if Month<0:
        Year = Year - 1
        Month = 12 + Month
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = today.day - int(birth1[2])
    if day<0:
        Month = Month - 1
    if Month<0:
        Year = Year - 1
        Month = 12 + Month
    day = day_list[Month] + day

    Label(root,text=f"{Year} years old, {Month} months, {day} days.").pack(pady=20)


Button2=Button(root, text = "Enter!", command = clicked, font = ("Arial", 18))

birth.pack()
Button2.pack()
root.mainloop()