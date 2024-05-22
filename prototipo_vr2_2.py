from tkinter import *
from tkinter import messagebox, simpledialog, filedialog
import tkinter as tk
import matplotlib.pyplot as plt  # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import customtkinter as ctk # type: ignore
from random import choice
from PIL import Image, ImageTk


# Cantidad de errores
errores = 0
archivo_seleccionado = None  # Variable global para el archivo seleccionado

# Función para leer datos del archivo de texto
def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(data.columns)  # Para depuración
        return data
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        return pd.DataFrame()

def plot():
    global archivo_seleccionado
    if archivo_seleccionado:
        data = read_data(archivo_seleccionado)
        #print 1
        print("el archivo fue detectado con exito")
        if not data.empty:
            if 'time' in data.columns and 'P_i' in data.columns and 'a1' in data.columns and 'a2' in data.columns and 'a3' in data.columns:
                # Leer parámetros a1, a2, a3 y tiempo
                a1 = data['a1'][0]
                a2 = data['a2'][0]
                a3 = data['a3'][0]
                t_final = max(data['time'])

                print(t_final)
                dt = 0.1
                n_steps = int(t_final / dt)
                time = np.linspace(0, t_final, n_steps)

                # Definir la ecuación diferencial
                def modelo(P, a1, a2, a3):
                    dPdt = a1 - a2 * P - a3 * P**2
                    return dPdt
                #print 2
                print("se retorna Ddpdt")

                # Condición inicial
                P0 = 0

                P_values = np.zeros(n_steps)
               # n_steps= int(100)
                P_values[0] = P0
               #print 3
                print("se establecen los valores iniciales")
            
                # Resolver la ecuación diferencial usando el método de Euler
                for i in range(1, n_steps):
                    P_values[i] = P_values[i-1] + modelo(P_values[i-1], a1, a2, a3) * dt
                  #print 4
                    print("se usa el metodo de euler")

                # Graficar la solución
                plt.plot(time, P_values, label='Fertilidad (P_i) sobre tiempo')
                plt.xlabel('Tiempo')
                plt.ylabel('Fertililidad (Pi)')
                plt.legend()
                plt.show()
                    #print 5
                print("se grafico la solucion")
                # Interpretar la fertilidad
                 #print 6
                print("se mando a llamar la funcion interpretar fertility")
                interpretation = interpretar_fertility(P_values)
                print(interpretation)
                messagebox.showinfo("Interpretación de la Fertilidad", interpretation)
            else:
                messagebox.showerror("Error", "El archivo seleccionado no tiene las columnas necesarias ('time', 'P_i', 'a1', 'a2', 'a3').")
        else:
            messagebox.showerror("Error", "El archivo seleccionado no contiene datos.")
    else:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")



def interpretar_fertility(P_i_values):
    if P_i_values[-1] > 10:
        return "La fertilidad es alta."
    elif P_i_values[-1] > 5:
        return "La fertilidad es moderada."
    else:
        return "La fertilidad es baja."
    
#quitar prueba

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

textoinfo= """la ecuacion diferencial puede clasificarse de la siguiente manera:

1. **Ecuación Diferencial Ordinaria (EDO)**:
  - La ecuación involucra una sola variable dependiente \( P \) y una sola variable independiente \( t \). No hay derivadas parciales con respecto a más de una variable independiente, por lo que es una ecuación diferencial ordinaria.

2. **Ecuación Diferencial de Primer Orden**:
   - La más alta derivada que aparece en la ecuación es la primera derivada por lo que es una ecuación de primer orden.

3. **Ecuación Diferencial No Lineal**:
   - La ecuación es no lineal. Una ecuación diferencial es no lineal si la variable dependiente \( P \) o sus derivadas aparecen con potencias distintas de uno o en productos entre ellas.

En resumen, la ecuación:
es una ecuación diferencial ordinaria, de primer orden, no lineal """

# Función que muestra más información
def miFuncion3():
    messagebox.showinfo("ACERCA DE LA ECUACION", textoinfo)





app = Tk()
app.geometry("800x800")  # Dimensiones de la ventana
app.resizable(1, 1)  # Capacidad de ser reescalable

#IMAGEN DE LA FORMULA
image_path = r'C:\Users\USER\Desktop\python\formula.png'
image = Image.open(image_path)
#tamaño de la imagen
new_size = (300, 63)
resized_image = image.resize(new_size, Image.LANCZOS)
#transformar para que tkinter pueda usarla
formula = ImageTk.PhotoImage(resized_image)
#crear una etiqueta para posicionar la imagen y poder manipularla
image_label = tk.Label(app, image=formula)
image_label.place(x=250, y=295, width=300, height=63)




app.configure(background="grey18")  # Color del fondo de la app
app.iconbitmap("conciente.ico")
app.title("¡PROTOTIPO 2.3!")  # Establecer el título de la app



# Variable datos
btnA = Button(app, text="Select File", command=miFuncion, fg="red", bg="blue")
btnA.place(x=5, y=70, width=100, height=30)

lbl_A = Label(app, text="INPUT(DATOS.TXT)", fg="red")
lbl_A.place(x=5, y=40, width=100, height=30)

# Label de las instrucciones
texto_instrucciones = """
Rellena los campos de las variables
con información sobre las propiedades de la tierra en la que se va a trabajar.
Procura que tu archivo sea de tipo txt para evitar errores.
A continuación se detalla el modo de uso:

Paso 1. Rellena el input con un archivo de texto.
Paso 2. Aprieta el botón 'Cargar Modelo' para ver con más detalle la ecuación diferencial.

Paso extra. Si quieres ver más sobre el programa, oprime 'MORE INFO'. 
"""
lbl_inst = Label(app, text=texto_instrucciones, fg="red", bg="blue")
lbl_inst.pack(pady=120)

# Indicador de errores
btnError = Button(app, text="Indicador de errores", command=miFuncion2, fg="white", bg="green")
btnError.place(x=340, y=470, width=120, height=30)

# Cargar modelo y graficar
btnModel = Button(app, text="Cargar modelo", command=plot, fg="white", bg="orange")
btnModel.place(x=340, y=500, width=120, height=30)

# Más información
btnInfo = Button(app, text="MORE INFO", command=miFuncion3, fg="red", bg="white")
btnInfo.place(x=700, y=10, width=120, height=30)

app.mainloop()  # Refresh de la app