from tkinter import *

############## Window ###########
root = Tk()
root.title("Test Window")
root.resizable(False, False)
root.geometry("700x500")
root.iconbitmap("icon.ico")
root.config(bg="green")


############## Frame ############
# simplificación:
# myFrame = myFrame(root, width=500, height = 400)
# myFriend.pack() para inicializar? frame
myFrame = Frame()
# side: left, top, right, bottom
# anchor: n (north), s (south), e (east), w (west)
# myFrame.pack(side="left", anchor="w")
# fill: x, y, both, none
# myFrame.pack(fill="none", expand="True")
myFrame.pack()
myFrame.config(bg="white")
myFrame.config(width="400", height="200")
# bd = border
# myFrame.config(bd=10)
# myFrame.config(relief="sunken")

########## Labels ###########
myLabel = Label(myFrame, text="Hello world", fg="green", font=("Century Gothic", 18));
myLabel.place(x="50px", y="50px")
# Label(myFrame, text="Hello world").place(x="50px", y="50px")
# myImage = PhotoImage(file="icon.png")
# Label(myFrame, image=myImage).place(x=10, y=20)

########### Text input ##########
square = Frame(root, width=200, height=200)
square.pack()
textInput = Entry(square)
# Using place() with the same coordinates x and y will have a similar result
textInput.grid(row=0, column=1)
nameLabel = Label(square, text="Log in")
nameLabel.grid(row=0, column=0)

########### Grids #############


root.mainloop()