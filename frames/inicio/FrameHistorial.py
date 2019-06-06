from tkinter import ttk
from tkinter import *
from data.modelos import *
import time

class Historial(ttk.Frame):

    def __init__(self, *args, **kwargs):
        self.conexion= Conexion()
        super().__init__(*args, **kwargs)

        self.list=ttk.Treeview(self, columns=("fecha"), selectmode=BROWSE)
        self.list.heading("#0", text="Prestante")
        self.list.heading("fecha", text="Fecha")
        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)

        item=self.list.insert("", END, text="1", values=(time.strftime("%d/%m/%y")), tags=("t",))
        self.listar()

        self.list.pack(expand=True, fill=BOTH)

        self.pack(expand=True, fill=BOTH)


    def itemSeleccionado(self, event):
        print("item en seleccion")
        idITEM=self.list.item(self.list.selection())

        reg=self.conexion.buscarHistorial(idITEM.get('text'), idITEM.get('values')[0])

        if reg:
            obtener = obtenerHis(reg.get("_id"))

    def listar(self):
        docs = self.conexion.listarHistorial()
        self.list.delete(*self.list.get_children())
        for doc in docs:
            self.list.insert('', END, text=doc.get('prestante'),
                             values=(doc.get('fecha')), tags=("t",))



class obtenerHis(Toplevel):
    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id=id
        self.conexion= Conexion()
        self.title("Historial")
        self.config()
        self.geometry("400x400+300+100")
        self.list=ttk.Treeview(self, columns=("Cantidad"), selectmode=BROWSE)
        self.list.heading("#0", text="Nombre")
        self.list.heading("Cantidad", text="Cantidad")
        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)
        self.list.pack(expand=True, fill=BOTH)
        arr=self.list.item(self.list.selection())


    def itemSeleccionado(self):
        pass


    def listarMat(self):
        materiales = self.conexion.buscarHistxID(self.id)
        self.list.delete(*self.list.get_children())
        for i in materiales:
            mat=self.conexion.buscarMatxID(i)
            self.list.insert('', END, text= mat.get('_id'),
                             values=(i.get('cantidad')), tags=("t",))



