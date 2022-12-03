from tkinter import *
root=Tk()
root.title("Class7")
root.geometry("250x150")


counter=0
def clicked():
    global counter
    counter+=1
    mylabel4["text"]=str(counter)
    label1["text"]="總額：$"+str(int(mylabel4["text"])*1200)+"元"

def clicked1():
    global counter
    if counter!=0: 
        counter-=1
    mylabel4["text"]=str(counter)
    label1["text"]="總額：$"+str(int(mylabel4["text"])*1200)+"元"


mylabel1 = Label(root, text = "Kube Shop").grid(row=0, column=1, columnspan=2, sticky=W+E)
mylabel2 = Label(root, text = "戶外餐桌椅組").grid(row=1, column=0, columnspan=3, sticky=W)
mylabel3 = Label(root, text = "$1200").grid(row=2, column=0, sticky=W)
mybutton2 = Button(root, text = "-", command=clicked1).grid(row=3, column=0, sticky=W)

mylabel4 = Label(root, text="0")
mylabel4.grid(row=3, column=1, sticky=W)

mybutton1 = Button(root, text = "+", command=clicked).grid(row=3, column=2, sticky=W)

label1 = Label(root, text = "總額：$ 0元")
label1.grid(row=4, column=1, sticky=W)



root.mainloop()