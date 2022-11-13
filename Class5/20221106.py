from tkinter import *
root = Tk()
root.title("Class5")
root.geometry("500x500")

#---------------------------------------------------------

# #建立 Label 標籤
# mybutton1 = Button(root, text = "West")
# mybutton2 = Button(root, text = "East")
# mybutton3 = Button(root, text = "East2")

# #加入視窗中
# mybutton1.pack(side = "left")
# mybutton2.pack(side = "right")
# mybutton3.pack(side = "right")

#---------------------------------------------------------

# #建立 Label 標籤
# mybutton1 = Button(root, text = "fill x")
# mybutton2 = Button(root, text = "fill y")

# #加入視窗中
# mybutton1.pack(fill = "x")
# mybutton2.pack(side = "right", fill = "y")

#---------------------------------------------------------

# #建立 Label 標籤
# mybutton1 = Button(root, text = "expand=0")
# mybutton2 = Button(root, text = "expand=1")

# #加入視窗中
# mybutton1.pack(fill = "both", expand = 0)
# mybutton2.pack(fill = "both", expand = 1)

#---------------------------------------------------------

# #建立 Label 標籤
# mybutton1 = Button(root, text = "West")
# mybutton2 = Button(root, text = "East")

# #加入視窗中
# mybutton1.pack(side = "left", padx = 10)
# mybutton2.pack(side = "right", padx = 90)

#--------------------------------------------------------- 

# #建立 Label 標籤
# mybutton1 = Button(root, text = "West")
# mybutton2 = Button(root, text = "East")

# #加入視窗中
# mybutton1.pack(side = "left", ipadx = 30)
# mybutton2.pack(side = "right", ipady = 30)

#---------------------------------------------------------

#建立 Label 標籤
mybutton1 = Button(root, text = "button1")
mybutton2 = Button(root, text = "button2")
mybutton3 = Button(root, text = "button3")
mybutton4 = Button(root, text = "button4")
mybutton5 = Button(root, text = "button5")

#加入視窗中
mybutton1.pack(side = "top", fill = "x")
mybutton2.pack(side = "left", fill = "y")
mybutton3.pack(side = "left")
mybutton4.pack(side = 'right')
mybutton5.pack(side = "top")


#---------------------------------------------------------

root.mainloop()

#---------------------------------------------------------

#筆記：
#Side 排列方向：TOP(預設), BOTTOM, LEFT, RIGHT
#Fill 填滿所分配空間之方向：NONE (預設), X, Y, BOTH
#Expand 填滿容器：True/False (預設)
#Padx/Pady 元件邊框與容器之距離 (px, 預設=0)
#Ipadx/Ipady 元件內容 (文字/圖像) 與其邊框之距離 (px, 預設=0)