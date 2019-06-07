from tkinter import ttk
from tkinter import *
from data.modelos import *


class Devoluciones(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conexion = Conexion()
        self.list=ttk.Treeview(self, columns=("Fecha"), selectmode=BROWSE)
        self.list.heading("#0", text="Prestante")
        self.list.heading("Fecha", text="Fecha")
        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)
        item=self.list.insert("", END, text="1", values=("arduino", "obtenerdelabd"), tags=("t",))
        self.listar()
        self.list.pack(expand=True, fill=BOTH)

        self.pack(expand=True, fill=BOTH)

    def itemSeleccionado(self, event):
        idITEM=self.list.item(self.list.selection())
        y = int(idITEM.get('values')[0].split('-')[0])
        m = int(idITEM.get('values')[0].split('-')[1])
        d = int(idITEM.get('values')[0].split('-')[2])
        start = datetime.datetime(y, m, d, 0, 0, 0)
        end = datetime.datetime(y, m, d, 23, 59, 59)
        reg=self.conexion.buscarDevoluciones(idITEM.get('text'), {'$lt': end, '$gte': start})

        if reg:
            obtener = obtenerDev(reg.get("_id"))

    def listar(self):
        docs = self.conexion.listarDevoluciones()
        self.list.delete(*self.list.get_children())
        for doc in docs:
            self.list.insert('', END, text=doc.get('prestante'),
                             values=(doc.get('fecha')), tags=("t",))

class obtenerDev(Toplevel):
    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.conexion=Conexion()
        self.title("Pendientes")
        self.config()
        self.geometry("400x400+300+100");
        self.list=ttk.Treeview(self, columns=("nombre"))
        self.list.heading("#0", text="Codigo")
        self.list.heading("nombre", text="Nombre")
        self.listarMat()
        self.list.pack(expand=True, fill=BOTH)

    def listarMat(self):
        registro = self.conexion.buscarDevxID(self.id)
        materiales = registro.get('materiales')
        self.list.delete(*self.list.get_children())
        for i in materiales:
            mat=self.conexion.buscarMatxID(i)
            self.list.insert('', END, text=mat.get('codigo'),
                             values=(mat.get('nombre')), tags=("t",))