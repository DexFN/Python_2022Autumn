#---------------------------------------------------------

#引入tkiner module
from tkinter import *
root=Tk()
root.title("Class7")
root.geometry("350x100")

#---------------------------------------------------------

# #加入Frame框架
# frame=Frame(root)
# frame.pack()
# #將Label放在制定的Frame裡
# label=Label(frame, text="Sussy Baka")
# label.pack()

#---------------------------------------------------------

# #Frame元件
# frame1=Frame(root, pady=5, padx=20, bg="lightblue")
# frame2=Frame(root, pady=20, padx=10, bg="pink")

# #放到frame1裡的label
# label1=Label(frame1, text="hello", width=10)
# label1.pack()
# #放到frame2裡的label
# label2=Label(frame2, text="world", width=20)
# label2.pack()

# #先放frame2
# frame2.pack()
# #先放frame1
# frame1.pack()

#---------------------------------------------------------

# #Frame元件
# frame1=Frame(root, pady=5, padx=10, bg="lightgreen")
# frame2=Frame(root, pady=10, padx=2, bg="lightblue")

# #放到frame1裡的label
# label1=Label(frame1, text="First", width=5)
# label1.pack()
# #放到frame2裡的label
# label2=Label(frame2, text="Second", width=10)
# label2.pack()

# #先放frame2
# frame2.pack(side="right")
# #先放frame1
# frame1.pack(side="left")

#---------------------------------------------------------

# #更改Label文字
#     #方法一
# counter=0
# def clicked():
#         global counter
#         counter+=1
#         mylabel["text"]="click "+str(counter)
# myButton = Button(root, text = "Button", command = clicked)
# myButton.pack(pady = 20)
# mylabel=Label(root, text="click 0")
# mylabel.pack()
# root.mainloop()

#---------------------------------------------------------

# #更改Label文字
#     #方法二
# counter=0
# def clicked():
#         global counter
#         counter+=1
#         mystringvar.set("click "+str(counter))
# myButton = Button(root, text = "Button", command = clicked)
# myButton.pack(pady = 20)
# mystringvar=StringVar()
# mystringvar.set("click 0")
# mylabel=Label(root, textvariable=mystringvar)
# mylabel.pack()
# root.mainloop()

#---------------------------------------------------------

# #獲取label文字內容
#     #方法一
# mylabel=Label(root, text="Hello World")
# mylabel.pack()
# Label(root, text=mylabel["text"]).pack()

#---------------------------------------------------------

# #獲取label文字內容
#     #方法二
# mystringvar=StringVar()
# mystringvar.set("Hello World!")
# mylabel=Label(root, textvariable=mystringvar)
# mylabel.pack()
# Label(root, text=mystringvar.get()).pack()

#---------------------------------------------------------

mylabel=Label(root, text="Hello World!")
mylabel.pack()
def clicked():
    Label(root, text=mylabel["text"]).pack()
myButton = Button(root, text = "Get Label Text", command = clicked)
myButton.pack()

#---------------------------------------------------------

#執行主程式
root.mainloop()

#---------------------------------------------------------