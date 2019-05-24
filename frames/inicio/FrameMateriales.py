from tkinter import ttk
from tkinter import  *

class Materiales(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.list=ttk.Treeview(self, columns=("nombre", "cantidad"))

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        self.list.heading("cantidad", text="Cantidad")

        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)

        item=self.list.insert("", END, text="1", values=("arduino", "20"), tags=("t",))

        self.list.pack(expand=True, fill=BOTH)

        self.agregar=Button(self, text="Agregar nuevo...")
        self.agregar.pack(side=RIGHT)

        self.eliminar=Button(self, text="Eliminar", state="disabled")
        self.eliminar.pack(side=RIGHT)

        self.pack(expand=True, fill=BOTH)


    def itemSeleccionado(self, event):
        print("item en seleccion")
        self.eliminar.config(state="normal")
