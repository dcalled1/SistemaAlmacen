from tkinter import *
from tkinter import ttk
from data.modelos import *

class CarnetPendiente(Toplevel):
    def __init__(self, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.conexion=Conexion()

        self.id=id

        self.list=ttk.Treeview(self, columns=("nombre"))

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        #self.list.heading("disponibilidad", text="Disponibilidad")


        self.listar()

        self.list.pack(expand=True, fill=BOTH)

        self.devolver=Button(self, text="Devolver",
                            command=self.devolvermaterial)
        self.devolver.pack(side=RIGHT)

        self.cancel=Button(self, text="Cancelar",
                             command=self.cancelar)
        self.cancel.pack(side=RIGHT)


    def devolvermaterial(self):
        self.conexion.devolverMaterial(self.id)
        self.master.devoluciones.listar()
        self.destroy()

    def cancelar(self):
        self.destroy()

    def listar(self):
        materiales=self.conexion.listarMatPrestante(self.id)
        for material in materiales:
            mat=self.conexion.buscarMatxID(material)
            if mat:
                self.list.insert('', END, text=mat.get('codigo'),
                                values=(mat.get('nombre')), tags=("t",))
