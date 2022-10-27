import tkinter
ventana= tkinter.Tk()
ventana.title("BIENVENIDO A LA PANTALLA 1")
ventana.geometry("500x500")
ventana.config(bg="thistle3")

def ventana2():
    ventana2=tkinter.Toplevel()
    ventana2.geometry("500x500")
    ventana2.config(bg="orange")
    ventana2.title("BIENVENIDO PANTALLA 2")

boton=tkinter.Button (ventana,command=ventana2,text="INICIAR")
boton.pack()
ventana.mainloop()