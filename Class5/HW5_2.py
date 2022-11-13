from tkinter import *
root = Tk()
root.title("Class5")
root.geometry("500x500")

mybutton1 = Button(root, text = "1")
mybutton2 = Button(root, text = "2")
mybutton3 = Button(root, text = "3")

mybutton1.pack(side = "top")
mybutton2.pack(side = "left")
mybutton3.pack(side = "bottom")

root.mainloop()