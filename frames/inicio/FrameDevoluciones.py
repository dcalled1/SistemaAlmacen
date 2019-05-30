from tkinter import ttk
from tkinter import *

class Devoluciones(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list=ttk.Treeview(self, columns=("Cantidad","Fecha"), selectmode=BROWSE)
        self.list.heading("#0", text="Prestante")
        self.list.heading("Cantidad", text="Cantidad")
        self.list.heading("Fecha", text="Fecha")
        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)
        item=self.list.insert("", END, text="1", values=("arduino", "obtenerdelabd"), tags=("t",))

        self.list.pack(expand=True, fill=BOTH)

        self.pack(expand=True, fill=BOTH)

    def itemSeleccionado(self, event):
        print("item en seleccion")

        obtener = obtenerDev()
class obtenerDev(Toplevel):
    def __init__(self, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Pendientes")
        self.config()
        self.geometry("400x400+300+100");
        self.list=ttk.Treeview(self, columns=("Cantidad"), selectmode=BROWSE)
        self.list.heading("#0", text="Nombre")
        self.list.heading("Cantidad", text="Cantidad")
        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)
        self.list.pack(expand=True, fill=BOTH)

    def itemSeleccionado(self):
        pass
