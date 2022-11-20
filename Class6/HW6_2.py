from tkinter import *
root = Tk()
root.title("Class6")
root.geometry("350x100")
def open(): 
    menubar1.entryconfig("Execute", state="normal")
def close():
    menubar1.entryconfig("Execute", state="disable")
menu = Menu(root)
menubar1 = Menu(menu)
menubar1.add_command(label="Open", command=open)
menubar1.add_command(label="Execute", state="disable")
menubar1.add_command(label="Close", command=close)
menu.add_cascade(label="File", menu=menubar1)

menubar1.add_separator()
menubar1more = Menu(menubar1)
menubar1more.add_command(label="X")
menubar1more.add_command(label="Y")
menubar1.add_cascade(label="Place", menu=menubar1more)

menubar2 = Menu(menu)
menubar2.add_command(label="AAA")
menubar2.add_command(label="BBB")
menu.add_cascade(label="Triple", menu=menubar2)
root.config(menu=menu)

root.mainloop()