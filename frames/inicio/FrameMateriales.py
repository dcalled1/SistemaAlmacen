from tkinter import ttk
from tkinter import  *
import time

class AñadirNuevo(Toplevel):

    procesando=True
    cod=None
    nom=None
    cant=None

    def __init__(self, lista, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Añadir material")
        self.config()

        self.lista=lista;

        self.codLabel=Label(self, text="Código: ")
        self.codLabel.grid(column=0, row=0, padx=10, pady=10)

        self.codigo=ttk.Entry(self)
        self.codigo.grid(column=1, row=0, padx=10, pady=10, sticky='ew')

        self.nomLabel = Label(self, text="Nombre: ")
        self.nomLabel.grid(column=0, row=1, padx=10, pady=10)

        self.nombre = ttk.Entry(self)
        self.nombre.grid(column=1, row=1, padx=10, pady=10, sticky='ew')

        self.var=BooleanVar(self)

        self.verificar=Checkbutton(self,text="Registrar cantidad",
                                   variable=self.var, command=self.cambiar)
        self.verificar.grid(column=0, row=2, columnspan=2)

        self.cantLabel = Label(self, text="Cantidad: ")
        self.cantLabel.grid(column=0, row=3, padx=10, pady=10)

        self.cantidad = ttk.Spinbox(self, state="disabled", increment=1)
        self.cantidad.grid(column=1, row=3, padx=10, pady=10)

        self.anadirBot=Button(self, text="Agregar", command=self.setData)
        self.anadirBot.grid(column=1, row=4, columnspan=2, sticky='w')

        self.cancelBot = Button(self, text="Cancelar", command=self.cancel)
        self.cancelBot.grid(column=1, row=4, columnspan=2, sticky='e')


    def cambiar(self):
        st="normal" if self.var.get() else "disabled"
        self.cantidad.config(state=st)

    def setData(self):
        self.cod=self.codigo.get()
        self.nom=self.nombre.get()
        self.cant=self.cantidad.get()

        if self.cod!='' and self.nom!='':
            self.lista.insert("", END, text=self.cod,
                        values=(self.nom, self.cant.__str__()), tags=("t",))
            self.destroy()

    def cancel(self):
        self.destroy()





class Materiales(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.list=ttk.Treeview(self, columns=("nombre", "cantidad"), selectmode=BROWSE)

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        self.list.heading("cantidad", text="Cantidad")

        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)

        item=self.list.insert("", END, text="1", values=("arduino", "20"), tags=("t",))

        self.list.pack(expand=True, fill=BOTH)

        self.agregar=Button(self, text="Agregar nuevo...",
                            command=self.nuevoMaterial)
        self.agregar.pack(side=RIGHT)

        self.eliminar=Button(self, text="Eliminar", state="disabled",
                             command=self.eliminarMaterial)
        self.eliminar.pack(side=RIGHT)

        self.editar = Button(self, text="Editar", state="disabled",
                               command=self.editarMaterial)
        self.editar.pack(side=RIGHT)

        self.pack(expand=True, fill=BOTH)


    def itemSeleccionado(self, event):
        print("item en seleccion")
        self.eliminar.config(state="normal")
        self.editar.config(state="normal")



    def nuevoMaterial(self):
        añadir=AñadirNuevo(self.list, self)

    def eliminarMaterial(self):
        self.list.selection_remove(self.list.selection())

    def editarMaterial(self):
        pass


