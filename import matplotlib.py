from tkinter import *
from tkinter import messagebox, simpledialog, filedialog
import tkinter as tk
import matplotlib.pyplot as plt  # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # type: ignore
import pandas as pd  # type: ignore

# Cantidad de errores
errores = 0
archivo_seleccionado = None  # Variable global para el archivo seleccionado

# Función para leer datos del archivo de texto
def read_data(file_path):
    return pd.read_csv(file_path)

# Función para graficar los datos
def plot():
    global archivo_seleccionado
    if archivo_seleccionado:
        data = read_data(archivo_seleccionado)  # Leer los datos del archivo seleccionado
        ax.clear()  # type: ignore
        # Graficar P_i a través del tiempo (asegúrate de que el archivo tiene la columna 'time')
        if 'time' in data.columns and 'P_i' in data.columns:
            ax.plot(data['time'], data['P_i'], label='Fertility (P_i) over Time')  # type: ignore
            ax.set_xlabel('Time')  # type: ignore
            ax.set_ylabel('Fertility (P_i)')  # type: ignore
            ax.legend()  # type: ignore
            canvas.draw()  # type: ignore
        else:
            messagebox.showerror("Error", "El archivo seleccionado no tiene las columnas necesarias ('time' y 'P_i').")
    else:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")

# Función para seleccionar el archivo
def miFuncion():
    global archivo_seleccionado
    global errores
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        print("Archivo seleccionado:", archivo)
        if not archivo.endswith(".txt"):
            errores += 1  # Incrementamos la variable errores en 1
            messagebox.showerror("Error", "Debes seleccionar un archivo de texto.")
        else:
            archivo_seleccionado = archivo
            messagebox.showinfo("Éxito", "Archivo agregado correctamente.")

# Muestra la cuenta de errores hasta el momento
def miFuncion2():
    messagebox.showerror("Cantidad de errores", "Errores: " + str(errores))

# Función que muestra más información
def miFuncion3():
    messagebox.showinfo("ACERCA DE", "Este programa fue creado sin fines de lucro xD")

app = Tk()
app.geometry("800x800")  # Dimensiones de la ventana
app.resizable(1, 1)  # Capacidad de ser reescalable
app.configure(background="grey18")  # Color del fondo de la app
app.iconbitmap("conciente.ico")
app.title("¡PROTOTIPO!")  # Establecer el título de la app

lbl_titulo = Label(app, text="FertiliGrow", font=("comic sans", 26))
lbl_titulo.pack()  # Etiqueta del título principal

# Variable A
btnA = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnA.place(x=5, y=70, width=100, height=30)

lbl_A = Label(app, text="INPUT A", fg="red")
lbl_A.place(x=5, y=40, width=100, height=30)

# Variable B
btnB = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnB.place(x=5, y=150, width=100, height=30)

lbl_B = Label(app, text="INPUT B", fg="red")
lbl_B.place(x=5, y=120, width=100, height=30)

# Variable C
btnC = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnC.place(x=5, y=230, width=100, height=30)

lbl_C = Label(app, text="INPUT C", fg="red")
lbl_C.place(x=5, y=200, width=100, height=30)

# Variable D
btnD = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnD.place(x=5, y=310, width=100, height=30)

lbl_D = Label(app, text="INPUT D", fg="red")
lbl_D.place(x=5, y=280, width=100, height=30)

# Variable E
btnE = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnE.place(x=5, y=390, width=100, height=30)

lbl_E = Label(app, text="INPUT E", fg="red")
lbl_E.place(x=5, y=360, width=100, height=30)

# Label de las instrucciones
texto_instrucciones = """
Rellena los campos de las variables A, B, C, D y E 
con información sobre las propiedades de la tierra en la que se va a trabajar.
Procura que tu archivo sea de tipo txt para evitar errores.
A continuación se detalla el modo de uso:

Paso 1. Rellena cada campo con un archivo de texto.
Paso 2. Aprieta el botón 'Cargar Modelo' para ver con más detalle la ecuación diferencial.

Paso extra. Si quieres ver más sobre el programa, oprime 'MORE INFO'. 
"""
lbl_inst = Label(app, text=texto_instrucciones, fg="red", bg="blue")
lbl_inst.pack(pady=120)

# Indicador de errores
btnError = Button(app, text="Indicador de errores", command=miFuncion2, fg="white", bg="green")
btnError.place(x=330, y=350, width=120, height=30)

# Cargar modelo y graficar
btnModel = Button(app, text="Cargar modelo", command=plot, fg="white", bg="orange")
btnModel.place(x=330, y=380, width=120, height=30)

# Más información
btnInfo = Button(app, text="MORE INFO", command=miFuncion3, fg="red", bg="white")
btnInfo.place(x=700, y=10, width=120, height=30)

# Configuración de la gráfica
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.draw()
canvas.get_tk_widget().place(x=450, y=70, width=300, height=300)

toolbar = NavigationToolbar2Tk(canvas, app)
toolbar.update()
canvas.get_tk_widget().pack()
toolbar.pack()

app.mainloop()  # Refresh de la app
