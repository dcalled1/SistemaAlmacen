from tkinter import *
import RPi.GPIO as IO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def abrirHistorial():
    print("Historial")

def abrirLista():
    print("Lista de materiales")

def abrirDevoluciones():
    print("Devoluciones")

def abrirCarnet():
    print("Carnet abierto")

vPrincipal = Tk()
vPrincipal.geometry('150x230+200+200')
vPrincipal.title('Sistema de prestamos')
vPrincipal.config(bg = 'blue2')

botonHistorial = Button(vPrincipal,
                        text='Historial',
                        height=1,
                        width=10,
                        command=abrirHistorial).place(x = 20, y = 10)

botonMateriales = Button(vPrincipal,
                        text='Ver lista de \n materiales',
                        height=3,
                        width=10,
                        command=abrirLista).place(x = 20, y = 60)

botonDevoluciones = Button(vPrincipal,
                        text='Devoluciones \n pendientes',
                        height=3,
                        width=10,
                        command=abrirDevoluciones).place(x = 20, y = 140)


try:
    while 1:
        vPrincipal.update()
        id = reader.read_id_no_block()
        if not id:
            abrirCarnet()

except TclError:
    IO.cleanup()

except KeyboardInterrupt:
    IO.cleanup()