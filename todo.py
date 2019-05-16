from tkinter import *
import RPi.GPIO as IO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

vPrincipal = Tk()
vPrincipal.geometry('150x230+200+200')
vPrincipal.title('Sistema de prestamos')
vPrincipal.config(bg = 'blue2')

botonHistorial = Button(vPrincipal,
                        text = 'Historial',
                        height = 1,
                        width = 10).place(x = 20, y = 10)

botonMateriales = Button(vPrincipal,
                        text = 'Ver lista de \n materiales',
                        height = 3,
                        width = 10).place(x = 20, y = 60)

botonDevoluciones = Button(vPrincipal,
                        text = 'Devoluciones \n pendientes',
                        height = 3,
                        width = 10).place(x = 20, y = 140)

id, _ = reader.read()
print(id)

vPrincipal.mainloop()

IO.cleanup()