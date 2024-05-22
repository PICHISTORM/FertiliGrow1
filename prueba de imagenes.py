import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk





app = tk.Tk()
app.title("Image in Tkinter")
app.geometry("800x800")  # Dimensiones de la ventana
app.resizable(1, 1)  # Capacidad de ser reescalable

# Load the image file
# Replace 'your_logo.png' with the path to your image file
image_path = r'C:\Users\USER\Desktop\python\watermelon.jpg'
image = Image.open(image_path)

# Resize the image to 300x300 pixels (change the dimensions as needed)
new_size = (300, 300)
resized_image = image.resize(new_size, Image.LANCZOS)

# Convert the resized image to a format Tkinter can use
tk_image = ImageTk.PhotoImage(resized_image)
app.configure(background="grey18") 
# Create a label to display the image
image_label = tk.Label(app, image=tk_image)
image_label.place(x=80, y=40, width=300, height=300)

image_label.image = tk_image  # Keep a reference to the image to prevent garbage collection

lbl_A = Label(app, text="HOLA SOY WATERMELON TE AMO <3)", fg="red")
lbl_A.place(x=80, y=40, width=300, height=30)

# Start the Tkinter event loop
app.mainloop()
