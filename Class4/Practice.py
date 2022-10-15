# from tkinter import *

# root = Tk()

# root.title("Practice")

# root.geometry("600x400+150+200") 

# myLabel = Label(root, text="2022/10/02", fg = "Blue", bg = "Pink", font = ("Arial",16, "bold"))
# myLabel.pack()

# myLabel1 = Label(root, text="Sunday", fg = "Blue", bg = "Pink", font = ("Pilgi",20, "italic"))
# myLabel1.pack(pady = 50)

# def clicked():
#     label1 = Label(root, text = "Louie", font = ["Garamond", 16])
#     label1.pack()
# myButton = Button(root, text = "Please Click it", command = clicked, font = ("Garamond", 16))
# myButton.pack(pady = 20)

# root.mainloop()

# 引入 tkinter module
from tkinter import *

# 建立主視窗 Frame
root = Tk()

# 設定視窗標題
root.title("Hello World!")

# 設定視窗大小為 300x275，視窗（左上腳）在螢幕上的座標位置為（500, 150)
root.geometry("300x275+500+150") 

# 建立 Label 標籤
myLabel = Label(root, text="Please enter you name:", fg = "#f4b41a", bg = "#143d59", font = ("Garamond",25, "bold"))
# 加入視窗中
myLabel.pack(pady = 20)

# 點擊按鈕函式Function
def clicked():
    label1 = Label(root, text = "Hello "+e.get()+", Welcome!", font = ("Garamond", 16))
    label1.pack()
# 建立 Input Entry Boxes
e = Entry(root, width = 25, font = ["Garamond", 16])
# 加入視窗中
e.pack()
# 建立 Button 按鈕
myButton = Button(root, text = "Enter", command = clicked, font = ("Garamond", 16))
# 加入視窗中
myButton.pack(pady = 20)

# 執行主程式
# Mainloop一定要打在最後
root.mainloop()