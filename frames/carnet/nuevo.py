from tkinter import *
from tkinter import ttk

class NuevoCarnet(Toplevel):
    def __init__(self, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ##self.conexion=Conexion()

        self.id=id

        self.list=ttk.Treeview(self, columns=("nombre", "disponibilidad"))

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        self.list.heading("disponibilidad", text="Disponibilidad")

        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)

        #self.listar()

        self.list.pack(expand=True, fill=BOTH)

        self.aceptar=Button(self, text="Confirmar selección",
                            command=self.confirmar)
        self.aceptar.pack(side=RIGHT)

        self.cancel=Button(self, text="Cancelar",
                             command=self.cancelar)
        self.cancel.pack(side=RIGHT)



    def itemSeleccionado(self):
        pass

    def confirmar(self):
        pass

    def cancelar(self):
        pass