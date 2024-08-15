from tkinter import *
from tkinter import ttk
import time
from datetime import datetime
import pytz

class RelojClass:
    def __init__(self):
        # Crear la ventana principal
        self.ventana = Tk()
        # Establecer el tamaño de la ventana
        self.ventana.geometry("500x250")
        
        # Crear un widget de etiqueta para mostrar la hora
        self.reloj = Label(self.ventana, font=("times", 50, "bold"))
        # Colocar la etiqueta en la ventana utilizando un grid
        self.reloj.grid(row=2, column=1, pady=65, padx=110)
        
        # Diccionario que asocia nombres de ciudades con sus zonas horarias
        self.localizaciones = { "Argentina":"America/Argentina/Buenos_Aires", "Brasil":"Etc/GMT+3", "Chile":"America/Santiago", "México":"America/Mexico_City", 
                               "Paraguay":"America/Asuncion", "Perú":"America/Lima", "Uruguay":"America/Montevideo", "Venezuela":"America/Caracas", "Canadá":"Etc/GMT+4",
                               "Estados Unidos":"Etc/GMT+4", "Alemania":"Europe/Berlin", "España":"Europe/Madrid", "Francia":"Europe/Paris","Italia":"Europe/Rome",
                               "Países Bajos":"Europe/Amsterdam", "Reino Unido":"Europe/London", "Qatar":"Asia/Qatar", "China":"Etc/GMT-8", "Japón":"Asia/Tokyo", 
                               "Rusia":"Europe/Moscow","Australia":"Australia/Canberra","Nueva Zelanda":"Etc/GMT-12"
                               }
        
        # Crear una etiqueta para mostrar el texto de la localización
        self.etiqueta_localizacion = Label(self.ventana, text="Hora Local", width=26, font="arial 24 bold", fg="green")
        # Colocar la etiqueta en la ventana
        self.etiqueta_localizacion.place(x=0, y=20)
        
        # Crear un combobox para seleccionar la ciudad
        self.entrada = ttk.Combobox(self.ventana, width=42)
        # Definir los valores del combobox
        self.entrada["values"] = ["Hora Local","Argentina","Brasil","Chile","México","Paraguay","Perú","Uruguay","Venezuela","Canadá","Estados Unidos",
                                  "Alemania","España","Francia","Italia","Países Bajos","Reino Unido","Qatar","China","Corea N", "Corea S", "Japón", "Rusia",
                                  "Australia","Nueva Zelanda"]
        # Establecer el valor inicial del combobox
        self.entrada.set("Hora Local")
        # Colocar el combobox en la ventana
        self.entrada.place(x=110, y=175)

        # Llamar al método para mostrar la hora
        self.mostrar_hora()

        # Ejecutar el bucle principal de la ventana
        self.ventana.mainloop()

    def mostrar_hora(self):
        # Verificar si se ha seleccionado una ciudad distinta a "Hora Local"
        if self.entrada.get() != "Hora Local":
            # Obtener la zona horaria de la ciudad seleccionada
            zona_tiempo = pytz.timezone(self.localizaciones[self.entrada.get()])
            # Obtener la hora actual en la zona horaria seleccionada
            hora_zona = datetime.now(zona_tiempo)
            # Formatear la hora como una cadena
            hora_actual = hora_zona.strftime("%H:%M:%S")
            # Actualizar el texto de la etiqueta de localización para mostrar la ciudad seleccionada
            self.etiqueta_localizacion.configure(text='Hora en {}'.format(self.entrada.get()))
        else:
            # Obtener la hora local del sistema
            hora_actual = time.strftime("%H:%M:%S")
            # Actualizar el texto de la etiqueta de localización para mostrar "Hora Local"
            self.etiqueta_localizacion.configure(text=self.entrada.get())
        
        # Actualizar el texto de la etiqueta del reloj con la hora actual
        self.reloj.config(text=hora_actual, bg="black", fg="green", font="Arial 50 bold")
        # Llamar al método mostrar_hora nuevamente después de 200 milisegundos
        self.reloj.after(200, self.mostrar_hora)

# Ejecutar la aplicación si este archivo es el principal
if __name__ == "__main__":
    RelojClass()
