from tkinter import *
from tkinter import messagebox, simpledialog, filedialog
import tkinter as tk
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
import pandas as pd 
import numpy as np  
from PIL import Image, ImageTk
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


# Cantidad de errores
errores = 0
archivo_seleccionado = None  # Variable global para el archivo seleccionado


dataDict = {
    "ph" : [5.8,15,13.6,2.7,13.1,17.4,10.9,10.1,1.4,11,1.4,3.8],
    "ft" : [10.6,10.4,3.6,12.9,15.3,8.9,5.9,14.6,7.4,3.6,17.4,14.8],
    "co2" : [2.5,3.7,11.2,17,18.7,12.2,12.7,8.7,9.6,13.1,6.4,8.7],
    "ca" : [2.4,1.5,4.8,8.1,5.4,4.8,1.4,3.6,7.6,6,7.1,3.3],
    "fo" : [6.9,7,6,8.3,7.6,1.7,8.1,5.6,5.9,9.9,4.8,9],
    "hum" : [3.5,5.52,6.71,5.51,11.51,9.83,6.46,7.7,2.99,5.18,5.22,2.72]

}

monthDic = {
    'enero': 0,
    'febrero': 1,
    'marzo': 2,
    'abril': 3,
    'mayo': 4,
    'junio': 5,
    'julio': 6,
    'agosto': 7,
    'septiembre': 8,
    'octubre': 9,
    'noviembre': 10,
    'diciembre': 11
}

# Función para leer datos del archivo de texto
def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(data.columns)  # Para depuración
        return data
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        return pd.DataFrame()

def plot(month):
    idx = monthDic[month]
    a =  dataDict["fo"][idx] * dataDict["hum"][idx] 
    b =  dataDict["ph"][idx] * 1/dataDict["co2"][idx]
    c = 1/dataDict["ca"][idx] * 1/dataDict["fo"][idx]
    def dvdt(t,v):
        return a - b * v - c*v**2
    
    v0 = 0
    t = np.linspace(0,1,100)
    sol1 = odeint(dvdt, y0 = v0, t = t, tfirst = True)
    sol2 = solve_ivp(dvdt, t_span = (0,max(t)), y0= [v0], t_eval = t)

    ySol1 = sol1.T[0]
    ySol2 = sol2.y[0]
    plt.title("Crecimiento de la fertilidad en "+month)
    plt.plot(t,ySol1)
    plt.plot(t,ySol2)
    plt.ylabel('$P(t) / Fertilidad$', fontsize=22)
    plt.xlabel('$t$', fontsize=22)
    plt.show()
    return


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
    

    #all data ready
    for key in dataDict:
        if(len(dataDict[key]) != 12):
            messagebox.showerror("Error", "El formato de uno de los archivos es invalido. Deben ser 12 lineas *Una por mes*.")
            return
        
    print(dataDict)
    # Crear una nueva ventana usamos el (Toplevel)
    ventana_dos = Toplevel()
    ventana_dos.geometry("300x600")  # Dimensiones de la ventana
    app.resizable(1, 1)  # Capacidad de ser reescalable
    ventana_dos.title("***VISUALIZACION DEL MODELO***")
   

   

    # Agregar un label en la segunda ventana
    label = Label(ventana_dos, text="¡PANEL DE CONTROL!")
    label.pack(pady=6)

    # enero
    btn1 = Button(ventana_dos, text="[ENERO]", command= lambda: plot('enero'), fg="white", bg="dodger blue")
    btn1.place(x=100,y=40,width=100,height=30)

     # febrero
    btn2 = Button(ventana_dos, text="[FEBRERO]", command= lambda: plot('febrero'), fg="white", bg="dodger blue")
    btn2.place(x=100,y=80,width=100,height=30)

     # MARZO
    btn3 = Button(ventana_dos, text="[MARZO]", command= lambda: plot('marzo'), fg="white", bg="dodger blue")
    btn3.place(x=100,y=120,width=100,height=30)

     # ABRIL
    btn4 = Button(ventana_dos, text="[ABRIL]", command= lambda: plot('abril'), fg="white", bg="dodger blue")
    btn4.place(x=100,y=160,width=100,height=30)

     # MAYO
    btn5 = Button(ventana_dos, text="[MAYO]", command= lambda: plot('mayo'), bg="dodger blue")
    btn5.place(x=100,y=200,width=100,height=30)

     #JUNIO
    btn6 = Button(ventana_dos, text="[JUNIO]", command= lambda: plot('junio'), bg="dodger blue")
    btn6.place(x=100,y=240,width=100,height=30)

     #JULIO
    btn7 = Button(ventana_dos, text="[JULIO]", command= lambda: plot('julio'), bg="dodger blue")
    btn7.place(x=100,y=280,width=100,height=30)
    
     #AGOSTO
    btn8 = Button(ventana_dos, text="[AGOSTO]", command= lambda: plot('agosto'), bg="dodger blue")
    btn8.place(x=100,y=320,width=100,height=30)
    
     #SEPTIEMBRE
    btn9 = Button(ventana_dos, text="[SEPTIEMBRE]", command= lambda: plot('septiembre'), bg="dodger blue")
    btn9.place(x=100,y=360,width=100,height=30)

     #OCTUBRE
    btn10 = Button(ventana_dos, text="[OCTUBRE]", command= lambda: plot('octubre'), bg="dodger blue")
    btn10.place(x=100,y=400,width=100,height=30)

    #NOVIEMBRE
    btn11 = Button(ventana_dos, text="[NOVIEMBRE]", command= lambda: plot('noviembre'), bg="dodger blue")
    btn11.place(x=100,y=440,width=100,height=30)

    #DICIEMBRE
    btn12 = Button(ventana_dos, text="[DICIEMBRE]", command= lambda: plot('diciembre'), bg="dodger blue")
    btn12.place(x=100,y=480,width=100,height=30)


    # BOTON QUE CIERRA LA VENTANA
    cerrar_btn = Button(ventana_dos, text="Cerrar", command=ventana_dos.destroy)
    cerrar_btn.place(x=100,y=520,width=100,height=30)

# Función para seleccionar el archivo
def readData(args):
    global archivo_seleccionado
    global errores
    print(dataDict)
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
                numero = float(linea.strip())  # Convertir la línea a entero
                arreglo_numeros.append(numero)  # se pasa al arreglo
            
            messagebox.showinfo("Éxito", "Archivo agregado correctamente.")
            print(arreglo_numeros)
            dataDict[args] = arreglo_numeros
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



app.title("¡PROTOTIPO 2.3!")  # Establecer el título de la app

#ph
lbl_A=Label(app,text="pH//Unidades de pH", fg="white",bg="green2")
lbl_A.place(x=5,y=40,width=150,height=30)

btnA = Button(app, text="Select File", command= lambda: readData('ph'), fg="white", bg="black")
btnA.place(x=5,y=70,width=150,height=30)

#ft
lbl_B=Label(app,text="tasa de fotosíntesis//µg/m3",fg="white",bg="green2")
lbl_B.place(x=5,y=120,width=150,height=30)

btnB = Button(app, text="Select File", command= lambda: readData('ft'),fg="white", bg="black")
btnB.place(x=5,y=150,width=150,height=30)

#co2

lbl_C=Label(app,text="CO2//mol/m^2/s",fg="white",bg="green2")
lbl_C.place(x=5,y=200,width=150,height=30)

btnC = Button(app, text="Select File", command= lambda: readData('co2'), fg="white", bg="black")
btnC.place(x=5,y=230,width=150,height=30)

#ca
lbl_D=Label(app,text="calcio//mmol/L",fg="white",bg="green2")
lbl_D.place(x=5,y=280,width=150,height=30)

btnD = Button(app, text="Select File", command= lambda: readData('ca'), fg="white", bg="black")
btnD.place(x=5,y=310,width=150,height=30)

#fo
lbl_E=Label(app,text="fósforo//mmol/L", fg="white",bg="green2")
lbl_E.place(x=5,y=360,width=150,height=30)

btnE = Button(app, text="Select File", command= lambda: readData('fo'),fg="white", bg="black")
btnE.place(x=5,y=390,width=150,height=30)

#hum
lbl_F=Label(app,text="humedad//Porcentaje", fg="white",bg="green2")
lbl_F.place(x=5,y=440,width=150,height=30)

btnF = Button(app, text="Select File", command= lambda: readData('hum'),fg="white", bg="black")
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

Sobre los coeficientes de la ecuacion diferencial
a1 = Depende del producto del fosforo y humedad
a2 = Depende del ph y el inverso del Co2
a3 = Depende del inverso del producto del calcio y el fosforo
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