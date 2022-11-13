from tkinter import *
root = Tk()
root.title("Class5")
root.geometry("250x150")

mylabel1 = Label(root, text = "三人座沙發 綠色／灰色／黑色")
mylabel2 = Label(root, text = "NT. 28,900")
mybutton1 = Button(root, text = "-")
mylabel3 = Label(root, text = "0")
mybutton2 = Button(root, text = "+")

mylabel1.pack(side = "top")
mylabel2.pack(side = "left")
mybutton1.pack(side = "right")
mylabel3.pack(side = "right")
mybutton2.pack(side = "right")

root.mainloop()