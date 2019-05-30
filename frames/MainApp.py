from tkinter import ttk
from tkinter import *
from frames.inicio.FrameDevoluciones import *
from frames.inicio.FrameHistorial import *
from frames.inicio.FrameMateriales import *
import time

class AppPrincipal(ttk.Frame):

    def __init__(self, window):
        super().__init__(window)
        window.title("Sistema de almacén")
        window.geometry("800x600+300+100")
        self.notebook=ttk.Notebook(self)

        self.materiales=Materiales(self.notebook)
        self.notebook.add(self.materiales, text="Lista de materiales", padding=10)

        self.historial=Historial(self.notebook)
        self.notebook.add(self.historial, text="Historial", padding=10)

        self.devoluciones=Devoluciones(self.notebook)
        self.notebook.add(self.devoluciones, text="Devoluciones pendientes", padding=10)

        self.notebook.pack(padx=10, pady=10, side=LEFT, fill=BOTH)
        self.pack(fill=BOTH)

win = Tk()
app = AppPrincipal(win)
try:
    while 1:
        app.update()
        time.sleep(0.1)

except TclError:
    print("Apagado exitoso")
