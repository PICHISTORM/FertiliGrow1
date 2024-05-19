from tkinter import *
from tkinter import messagebox,simpledialog,filedialog
#cantidad de errores
errores = 0

#FUNCION QUE SE MANDA A LLAMAR AL APRETAR LOS BOTONES INPUT (PERMITE INGRESAR UN ARCHIVO Y ABRE UN POP-UP SI SE AGREGO DE FORMA CORRECTA)

def miFuncion():
    global errores 
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        print("Archivo seleccionado:", archivo)
        if not archivo.endswith(".txt"):
            errores += 1  # Incrementamos la variable errores en 1
            messagebox.showerror("Error", "Debes seleccionar un archivo de texto.")
        else:
            messagebox.showinfo("Éxito", "Archivo agregado correctamente.")

       

#muestra la cuenta de errores hasta el momento 
def miFuncion2():
    messagebox.showerror("cantidad de errores", "Errores: " + str(errores))

#funcion que muestra más informacion
def miFuncion3():
     messagebox.showinfo("ACERCA DE","este programa fue creado sin fines de lucro xD")




app = Tk()
app.geometry("800x600")  # dimensiones x,
app.resizable(1,1)  #capacidad de ser reescalable//redimensionar //true/false
app.configure(background="grey18")  # color del fondo de la app
app.iconbitmap("conciente.ico") #CUANDO TENGAMOS LA IMAGEN SOLO PONER LA RUTA
app.title("¡PROTOTIPO!")  # Establecer el título de la app

lbl_titulo=Label(app,text="FERTILINADOR VERSION 1.0",font=("comic sans",26))

lbl_titulo.pack() #etiqueta del titulo principal


#variable A
btnA = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnA.place(x=5,y=70,width=100,height=30)

lbl_A=Label(app,text="INPUT A", fg="red")
lbl_A.place(x=5,y=40,width=100,height=30)

#variable B
btnB = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnB.place(x=5,y=150,width=100,height=30)

lbl_B=Label(app,text="INPUT B", fg="red")
lbl_B.place(x=5,y=120,width=100,height=30)

#variable C
btnC = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnC.place(x=5,y=230,width=100,height=30)

lbl_C=Label(app,text="INPUT C", fg="red")
lbl_C.place(x=5,y=200,width=100,height=30)

#variable D
btnD = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnD.place(x=5,y=310,width=100,height=30)

lbl_D=Label(app,text="INPUT D", fg="red")
lbl_D.place(x=5,y=280,width=100,height=30)

#variable E
btnE = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnE.place(x=5,y=390,width=100,height=30)

lbl_E=Label(app,text="INPUT E", fg="red")
lbl_E.place(x=5,y=360,width=100,height=30)

#label de las instrucciones

texto_instrucciones = """
Rellena los campos de las variables A, B, C, D y E 
con información sobre las propiedades de la tierra en la que se va a trabajar.
Procura que tu archivo sea de tipo txt para evitar errores.
 A continuación se detalla el modo de uso:

Paso 1. Rellena cada campo con un archivo de texto.
Paso 2. Aprieta el botón 'Cargar Modelo' para ver con más detalle la ecuación diferencial.

Paso extra. Si quieres ver más sobre el programa, oprime 'MORE INFO'. 
"""
lbl_inst=Label(app,text=texto_instrucciones, fg="red",bg="blue")

lbl_inst.pack(pady=120)

#indicador de errores
btnError = Button(app, text="indicador de errores", command=miFuncion2, fg="white", bg="green")
btnError.place(x=330,y=350,width=120,height=30)

#cargar modelo
btnmodel = Button(app, text="Cargar modelo", fg="white", bg="orange")
btnmodel.place(x=330,y=380,width=120,height=30)


#MAS INFO
btninfo = Button(app, text="MORE INFO", command=miFuncion3,fg="red", bg="white")
btninfo.place(x=700,y=10,width=120,height=30)

#XD LOL LMAO ROFLMAO SIGMA SKIBIDI GYATT RIZZLER TOILET


app.mainloop()  # refresh de la app
