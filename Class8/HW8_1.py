from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title("Class7")
root.geometry("300x200")

img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class8/sofa.jpg")
resized_image=img.resize((150,100))
tk_img=ImageTk.PhotoImage(resized_image)
label=Label(root, image=tk_img)
label.grid(row=1, column=1, columnspan=2, sticky=W+E)

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
    else:
        messagebox.showinfo("showinfo", "The number of products can't be below 0")
    mylabel4["text"]=str(counter)
    label1["text"]="總額：$"+str(int(mylabel4["text"])*1200)+"元"


mylabel1 = Label(root, text = "Kube Shop")
mylabel1.grid(row=0, column=1, columnspan=2, sticky=W+E)
mylabel2 = Label(root, text = "Sofa")
mylabel2.grid(row=2, column=0, columnspan=3, sticky=W)
mylabel3 = Label(root, text = "$1200")
mylabel3.grid(row=2, column=1, sticky=W)
mybutton2 = Button(root, text = "-", command=clicked1)
mybutton2.grid(row=3, column=0, sticky=W)

mylabel4 = Label(root, text="0")
mylabel4.grid(row=3, column=1, sticky=W)

mybutton1 = Button(root, text = "+", command=clicked)
mybutton1.grid(row=3, column=2, sticky=W)

label1 = Label(root, text = "總額：$ 0元")
label1.grid(row=4, column=1, sticky=W)



root.mainloop()