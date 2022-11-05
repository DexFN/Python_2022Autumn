from tkinter import *
import datetime as d
today=d.date.today()
root=Tk()
root.geometry('400x400+150+200')
root.title("Class4_HW2")
birth=Entry(root,font=('Arial',18))
Label(root,text="Enter you birth date: \n Input format is yyyy.mm.dd").pack()
def clicked():
    birth_1=birth.get().split(".")
    year = today.year - int(birth_1[0])              # 用今天的年份，減去使用者的生日年份 ( 年份差 )
    month = today.month - int(birth_1[1])
    if month<0:
        year = year - 1
        month = 12 + month
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = today.day - int(birth_1[2])
    if day<0:
        month = month - 1
    if month<0:
        year = year - 1
        month = 12 + month
    day = day_list[month] + day

    Label(root,text=f"{year} years old, {month} months, {day} days.").pack()


Button2=Button(root,text="enter",command=clicked)

birth.pack()
Button2.pack()
root.mainloop()