from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#---------------------------------------------------------

# root=Tk()
# root.title("Class7")
# root.geometry("100x100")

#---------------------------------------------------------

# counter=0
# def clicked():
#         global counter
#         counter+=1
#         myButton["text"]="click "+str(counter)
# myButton = Button(root, text = "click 0", command = clicked)
# myButton.pack(pady = 20)

#---------------------------------------------------------

# counter=0
# def clicked():
#         global counter
#         counter+=1
#         mystringvar.set("click "+str(counter))
# mystringvar=StringVar()
# mystringvar.set("click 0")
# myButton = Button(root, text = "click 0", command = clicked, textvariable=mystringvar)
# myButton.pack()

#---------------------------------------------------------

# mybutton=Button(root, text="Hello World")
# mybutton.pack()
# Label(root, text=mybutton["text"]).pack()

#---------------------------------------------------------

# mystringvar=StringVar()
# mystringvar.set("Hello World!")
# mybutton=Button(root, textvariable=mystringvar)
# mybutton.pack()
# Label(root, text=mystringvar.get()).pack()

#---------------------------------------------------------

# img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class8/corgi1.jpg")
# resized_image=img.resize((100,100))
# tk_img=ImageTk.PhotoImage(resized_image)

#---------------------------------------------------------

# label=Label(root, image=tk_img)
# label.pack()

#---------------------------------------------------------

# mybutton=Button(root, image=tk_img)
# mybutton.pack()

#---------------------------------------------------------

# messagebox.showinfo("showinfo", "message test")

#---------------------------------------------------------

result = messagebox.askquestion("askquestion", "Is Forza Horizon 5 fun?")
print("User click"+result)

#---------------------------------------------------------

# root.mainloop()

#---------------------------------------------------------