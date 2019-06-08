from tkinter import *
from tkinter import ttk
from data.modelos import *

class CarnetPendiente(Toplevel):
    def __init__(self, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.conexion=Conexion() #Instancia clase conexion

        self.id=id

        self.list=ttk.Treeview(self, columns=("nombre"))

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        #self.list.heading("disponibilidad", text="Disponibilidad")


        self.listar()

        self.list.pack(expand=True, fill=BOTH)

        self.devolver=Button(self, text="Devolver", #Botón devolver
                            command=self.devolvermaterial)
        self.devolver.pack(side=RIGHT)

        self.cancel=Button(self, text="Cancelar", #Botón cancelar
                             command=self.cancelar)
        self.cancel.pack(side=RIGHT)


    def devolvermaterial(self):
        self.conexion.devolverMaterial(self.id) #Conectar con la base de datos y quitar los materiales de devoluciones
        self.master.devoluciones.listar() #Actualizar devoluciones
        self.destroy() #Cerrar ventana.

    def cancelar(self):
        self.destroy()

    def listar(self):
        materiales=self.conexion.listarMatPrestante(self.id) #Buscar los materiales que debe devolver la persona
        for material in materiales:
            mat=self.conexion.buscarMatxID(material)
            if mat:
                self.list.insert('', END, text=mat.get('codigo'), #Mostrar los materiales que debe devolver la persona
                                values=(mat.get('nombre')), tags=("t",))
