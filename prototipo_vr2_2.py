from tkinter import *
from tkinter import messagebox, simpledialog, filedialog
import tkinter as tk
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
import pandas as pd 
import numpy as np  
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
    
def imprimirhola():
 print("hola!OwO")
    
#funcion que abre una seg ventana al oprimir el boton cargar modelo xd
def ventana2():
    # Crear una nueva ventana usamos el (Toplevel)
    ventana_dos = Toplevel()
    ventana_dos.geometry("300x600")  # Dimensiones de la ventana
    app.resizable(1, 1)  # Capacidad de ser reescalable
    ventana_dos.title("***VISUALIZACION DEL MODELO***")
   

   

    # Agregar un label en la segunda ventana
    label = Label(ventana_dos, text="¡PANEL DE CONTROL!")
    label.pack(pady=6)

    # enero
    btn1 = Button(ventana_dos, text="[ENERO]", command=imprimirhola, fg="white", bg="dodger blue")
    btn1.place(x=100,y=40,width=100,height=30)

     # febrero
    btn2 = Button(ventana_dos, text="[FEBRERO]", command=imprimirhola, fg="white", bg="dodger blue")
    btn2.place(x=100,y=80,width=100,height=30)

     # MARZO
    btn3 = Button(ventana_dos, text="[MARZO]", command=imprimirhola, fg="white", bg="dodger blue")
    btn3.place(x=100,y=120,width=100,height=30)

     # ABRIL
    btn4 = Button(ventana_dos, text="[ABRIL]", command=imprimirhola, fg="white", bg="dodger blue")
    btn4.place(x=100,y=160,width=100,height=30)

     # MAYO
    btn5 = Button(ventana_dos, text="[MAYO]", command=imprimirhola, fg="white", bg="dodger blue")
    btn5.place(x=100,y=200,width=100,height=30)

     #JUNIO
    btn6 = Button(ventana_dos, text="[JUNIO]", command=imprimirhola, fg="white", bg="dodger blue")
    btn6.place(x=100,y=240,width=100,height=30)

     #JULIO
    btn7 = Button(ventana_dos, text="[JULIO]", command=imprimirhola, fg="white", bg="dodger blue")
    btn7.place(x=100,y=280,width=100,height=30)
    
     #AGOSTO
    btn8 = Button(ventana_dos, text="[AGOSTO]", command=imprimirhola, fg="white", bg="dodger blue")
    btn8.place(x=100,y=320,width=100,height=30)
    
     #SEPTIEMBRE
    btn9 = Button(ventana_dos, text="[SEPTIEMBRE]", command=imprimirhola, fg="white", bg="dodger blue")
    btn9.place(x=100,y=360,width=100,height=30)

     #OCTUBRE
    btn10 = Button(ventana_dos, text="[OCTUBRE]", command=imprimirhola, fg="white", bg="dodger blue")
    btn10.place(x=100,y=400,width=100,height=30)

    #NOVIEMBRE
    btn11 = Button(ventana_dos, text="[NOVIEMBRE]", command=imprimirhola, fg="white", bg="dodger blue")
    btn11.place(x=100,y=440,width=100,height=30)

    #DICIEMBRE
    btn12 = Button(ventana_dos, text="[DICIEMBRE]", command=imprimirhola, fg="white", bg="dodger blue")
    btn12.place(x=100,y=480,width=100,height=30)


    # BOTON QUE CIERRA LA VENTANA
    cerrar_btn = Button(ventana_dos, text="Cerrar", command=ventana_dos.destroy)
    cerrar_btn.place(x=100,y=520,width=100,height=30)

# Función para seleccionar el archivo
def miFuncion():
    global archivo_seleccionado
    global errores
    arreglo_numeros = []
    try:
        # Abrir el cuadro de diálogo para seleccionar el archivo
        archivo = filedialog.askopenfile(filetypes=[("Archivos de texto", "*.txt")])
        
        if archivo:
            print("Archivo seleccionado:", archivo.name)

            lineas = archivo.readlines() #lee todas las lineas
            # Cerrar el archivo después de leerlo
            archivo.close()

            for linea in lineas:
                numero = int(linea.strip())  # Convertir la línea a entero
                arreglo_numeros.append(numero)  # se pasa al arreglo
            
            messagebox.showinfo("Éxito", "Archivo agregado correctamente.")
            print(arreglo_numeros)
            return arreglo_numeros
            
            
        
        
        else:
            messagebox.showerror("Error", "Debes seleccionar un archivo de texto.")
            return None
    
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo: {e}")
        return None

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

#TEXTO DE LAS MEDIDAS
textoinfo2= """- pH // Unidades de pH
- tasa de fotosíntesis //  µg/m3..---microgramos por metro cúbico 
- difusión del CO2 // mol/m^2/s (moles por metro cuadrado por segundo)
- calcio // mmol/L (milimoles por litro) o ppm (partes por millón)
- fósforo // mmol/L (milimoles por litro) o ppm (partes por millón)
- humedad del suelo // Medida como fracción de volumen o porcentaje """

# Función que muestra más información
def miFuncion3():
    messagebox.showinfo("ACERCA DE LA ECUACION", textoinfo)

def miFuncion4():
     messagebox.showinfo("UNIDADES DE MEDIDA", textoinfo2)




app = Tk()
app.geometry("800x800")  # Dimensiones de la ventana
app.resizable(1, 1)  # Capacidad de ser reescalable

#IMAGEN DE LA FORMULA
image_path = 'formula.png'
image = Image.open(image_path)
#tamaño de la imagen
new_size = (300, 63)
resized_image = image.resize(new_size, Image.LANCZOS)
#transformar para que tkinter pueda usarla
formula = ImageTk.PhotoImage(resized_image)
#crear una etiqueta para posicionar la imagen y poder manipularla
image_label = tk.Label(app, image=formula)
image_label.place(x=270, y=295, width=300, height=63)


app.configure(background="grey18")  # Color del fondo de la app
app.iconbitmap("conciente.ico")
app.title("¡PROTOTIPO 2.3!")  # Establecer el título de la app

# Variable A
lbl_A=Label(app,text="pH//Unidades de pH", fg="white",bg="green2")
lbl_A.place(x=5,y=40,width=150,height=30)

btnA = Button(app, text="Select File", command=miFuncion, fg="white", bg="black")
btnA.place(x=5,y=70,width=150,height=30)

#variable B
lbl_B=Label(app,text="tasa de fotosíntesis//µg/m3",fg="white",bg="green2")
lbl_B.place(x=5,y=120,width=150,height=30)

btnB = Button(app, text="Select File", command=miFuncion,fg="white", bg="black")
btnB.place(x=5,y=150,width=150,height=30)

#variable C

lbl_C=Label(app,text="CO2//mol/m^2/s",fg="white",bg="green2")
lbl_C.place(x=5,y=200,width=150,height=30)

btnC = Button(app, text="Select File", command=miFuncion, fg="white", bg="black")
btnC.place(x=5,y=230,width=150,height=30)

#variable D
lbl_D=Label(app,text="calcio//mmol/L",fg="white",bg="green2")
lbl_D.place(x=5,y=280,width=150,height=30)

btnD = Button(app, text="Select File", command=miFuncion, fg="white", bg="black")
btnD.place(x=5,y=310,width=150,height=30)

#variable E
lbl_E=Label(app,text="fósforo//mmol/L", fg="white",bg="green2")
lbl_E.place(x=5,y=360,width=150,height=30)

btnE = Button(app, text="Select File", command=miFuncion,fg="white", bg="black")
btnE.place(x=5,y=390,width=150,height=30)

#Variable F
lbl_F=Label(app,text="humedad//Porcentaje", fg="white",bg="green2")
lbl_F.place(x=5,y=440,width=150,height=30)

btnF = Button(app, text="Select File", command=miFuncion,fg="white", bg="black")
btnF.place(x=5,y=470,width=150,height=30)

# Label de las instrucciones
texto_instrucciones = """
Rellena los campos de las variables
con información sobre las propiedades de la tierra en la que se va a trabajar.
Procura que tu archivo sea de tipo txt para evitar errores.
A continuación se detalla el modo de uso:

Paso 1. Rellena cada espacio vacio (input) con un archivo de texto.
Paso 2. Al finalizar el llenado,aprieta el botón 'Cargar Modelo' 
para ver con más detalle la ecuación diferencial.
**Paso extra**. Si quieres ver más sobre el programa o la ec.dif, oprime 'MORE INFO'. 
"""
lbl_inst = Label(app, text=texto_instrucciones, fg="white", bg="green")
lbl_inst.place(x=200,y=70)

# Indicador de errores
btnError = Button(app, text="Indicador de errores", command=miFuncion2, fg="white", bg="green")
btnError.place(x=350, y=470, width=120, height=30)

# Cargar modelo y graficar
btnModel = Button(app, text="Cargar modelo", command=ventana2, fg="white", bg="orange")
btnModel.place(x=350, y=500, width=120, height=30)

# Más información
btnInfo = Button(app, text="MORE INFO", command=miFuncion3, fg="red", bg="white",)
btnInfo.place(x=700, y=5, width=120, height=30,)

# MEDIDAS
btnInfo = Button(app, text="MEDIDAS", command=miFuncion4, fg="red", bg="white",)
btnInfo.place(x=5, y=520, width=150, height=30,)




app.mainloop()  # Refresh de la app