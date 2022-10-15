from tkinter import *

root = Tk()

root.title("Class4_HW1")

root.geometry("400x400+150+200") 

myLabel = Label(root, text="點擊按鈕次數計算", fg = "Orange", font = ("Garamond",25, "bold"))

myLabel.pack()

i=1



def clicked():
        global i
        label = Label(root, text = i)
        label.pack()
        i+=1

myButton = Button(root, text = "Click me!", command = clicked, font = ("Garamond", 16))

myButton.pack(pady = 20)

root.mainloop()