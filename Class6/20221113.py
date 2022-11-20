#引入 tkinter module
from tkinter import *

#建立主視窗 Frame
root = Tk()

#設定視窗標題
root.title("Class6")

#---------------------------------------------------------

# root.geometry("200x200")
# mybutton1 = Button(root, text="東").pack(anchor=E)
# mybutton2 = Button(root, text="西").pack(anchor=W)
# mybutton3 = Button(root, text="南").pack(anchor=S)
# mybutton4 = Button(root, text="北").pack(anchor=N)
# mybutton5 = Button(root, text="東南").pack(anchor=SE)
# mybutton6 = Button(root, text="西北").pack(anchor=NW)

#---------------------------------------------------------

# root.geometry("300x200")
# mybutton1 = Button(root, text="button1").grid(row=0, column=0)
# mybutton2 = Button(root, text="button2").grid(row=0, column=1)
# mybutton3 = Button(root, text="button3").grid(row=0, column=2)

# mybutton4 = Button(root, text="button4").grid(row=1, column=0)
# mybutton5 = Button(root, text="button5").grid(row=1, column=2)
# mybutton6 = Button(root, text="button6").grid(row=2, column=1)

#---------------------------------------------------------

# root.geometry("300x200")
# mybutton1 = Button(root, text="button1").grid(row=0, column=0)
# mybutton2 = Button(root, text="button2").grid(row=0, column=1)
# mybutton3 = Button(root, text="button3").grid(row=0, column=2)

# mybutton4 = Button(root, text="button4").grid(row=1, column=0, columnspan=2, sticky=W+E)

#---------------------------------------------------------

# root.geometry("350x150")
# mylabel1 = Label(root, text="Width").grid(row=0, column=1)
# mylabel2 = Label(root, text="Height").grid(row=1, column=1)
# mytextbox1=Entry(root,font=('Arial',18)).grid(row=0, column=2)
# mytextbox2=Entry(root,font=('Arial',18)).grid(row=1, column=2)
# mybutton3 = Button(root, text="Result").grid(row=0, column=3, rowspan=2, sticky=N+S)

#---------------------------------------------------------

# root.geometry("350x100")
# menubar = Menu(root)
# filemenu = Menu(menubar)
# filemenu.add_command(label="Open")
# filemenu.add_command(label="Save")
# filemenu.add_command(label="Exit")
# menubar.add_cascade(label="File", menu=filemenu)
# root.config(menu=menubar)

#---------------------------------------------------------

# #建立主選單
# menu = Menu(root)
# #建立第一個選單的子選單，有三個選項
# menubar1 = Menu(menu)
# menubar1.add_command(label="Open")
# menubar1.add_command(label="Save")
# menubar1.add_command(label="Exit")
# #建立第一個捲車File，綁定子選單
# menu.add_cascade(label="File", menu=menubar1)
# #建立第二個萱單的子選單，有三個選項
# menubar2 = Menu(menu)
# menubar2.add_command(label="AAA")
# menubar2.add_command(label="BBB")
# menubar2.add_command(label="CCC")
# #子選單分隔線
# menubar2.add_separator()
# #建立子選單內的子選單，有三個選項
# menubar2more = Menu(menubar2)
# menubar2more.add_command(label="X")
# menubar2more.add_command(label="Y")
# menubar2more.add_command(label="Z")
# menubar2.add_cascade(label="File", menu=menubar2more)
# #建立第二個選單File，綁定子選單
# menu.add_cascade(label="Test", menu=menubar2)
# #主視窗加入主選單
# root.config(menu=menu)

#---------------------------------------------------------

root.geometry("350x100")
def open(event=None): print("Open")
def save(event=None): print("Save")
def exit(event=None):
    print("Exit")
    root.destroy()
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Open", command=open, accelerator="Command+O")
filemenu.add_command(label="Save", command=save, accelerator="Command+S")
filemenu.add_command(label="Exit", command=exit, accelerator="Command+E")
menubar.add_cascade(label="File", menu=filemenu)
root.bind_all("<Command-o>", open)
root.bind_all("<Command-s>", save)
root.bind_all("<Command-e>", exit)
root.config(menu=menubar)

#---------------------------------------------------------

#執行主程式
root.mainloop()

#---------------------------------------------------------

#筆記 (Grid常用參數)：
#Anchor 原件在容器中的錨定位置：E, W, S, N, CENTER (預設), NE, SE, SW, NW
#Row 列索引
#Column 行索引
#Sticky 元件於網格中的錨定位置：E, W, S, N, CENTER (預設)
