from tkinter import *
root = Tk()
root.title("Class5")
root.geometry("220x120")

mylabel1 = Label(root, text = "Kube Shop").grid(row=0, column=1, columnspan=2, sticky=W+E)
mylabel2 = Label(root, text = "戶外餐桌椅組").grid(row=1, column=0, columnspan=3, sticky=W)
mylabel3 = Label(root, text = "$1200").grid(row=2, column=0, sticky=W)
mybutton1 = Button(root, text = "+").grid(row=3, column=0, sticky=W)
mylabel4 = Label(root, text = "0").grid(row=3, column=1, sticky=W)
mybutton2 = Button(root, text = "-").grid(row=3, column=2, sticky=W)

root.mainloop()