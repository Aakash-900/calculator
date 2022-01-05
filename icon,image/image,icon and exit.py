
from tkinter import *
from PIL import ImageTk, Image
from tkmacosx import Button

root = Tk()
 
root.title("Image Viewer")
root.iconbitmap("7 Small Medium.png")
 
root.geometry("500x500")

 
image_no_1 = PhotoImage(file="1 Medium.png")
image_no_2 = PhotoImage(file="2 Medium.png")
image_no_3 = PhotoImage(file="3 Small.png")
image_no_4 = PhotoImage(file="4 Medium.png")
image_no_5 = PhotoImage(file="5 Medium.png")
 

List_images = [image_no_1, image_no_2, image_no_3, image_no_4, image_no_5]
 
label = Label(image=image_no_1) 

label.grid(row=1, column=0, columnspan=3) 

button_exit = Button(root, text="Exit", command=root.quit)  
button_exit.grid(row=5, column=1) 



 
root.mainloop()