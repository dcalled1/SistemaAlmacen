from tkinter import *
import time

histAbierto=False
devAbierto=False
listAbierto=False

historial=None
lista=None
devoluciones=None

vPrincipal = Tk()
vPrincipal.geometry('150x230+200+200')
vPrincipal.title('Sistema de prestamos')
vPrincipal.config(bg = 'blue2')

def closeHist():
    global histAbierto, historial
    histAbierto=False
    historial.destroy()
    
def closeDev():
    global devAbierto, devoluciones
    devAbierto=False
    devoluciones.destroy()
    
def closeList():
    global listAbierto, lista
    listAbierto=False
    lista.destroy()

def abrirHistorial():
    global histAbierto, historial
    if not histAbierto:
        histAbierto=True
        historial=Toplevel()
        historial.geometry("800x800+500+100")
        historial.title("Historial de prestamos")
    historial.protocol("WM_DELETE_WINDOW", closeHist)

def abrirLista():
    global listAbierto, lista
    if not listAbierto:
        listAbierto=True
        lista=Toplevel()
        lista.geometry("800x800+500+100")
        lista.title("Lista de materiales")
    lista.protocol("WM_DELETE_WINDOW", closeList)

def abrirDevoluciones():
    global devAbierto, devoluciones
    if not devAbierto:
        devAbierto=True
        devoluciones=Toplevel()
        devoluciones.geometry("800x800+500+100")
        devoluciones.title("Devoluciones pendientes")
    devoluciones.protocol("WM_DELETE_WINDOW", closeDev)



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
        time.sleep(0.1)

except TclError:
    print("Apagado exitoso")

