from tkinter import ttk
from tkinter import  *
import time

class AñadirNuevo(Toplevel):

    procesando=True
    cod=None
    nom=None
    cant=None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Añadir material")
        self.config()

        self.codLabel=Label(self, text="Código: ")
        self.codLabel.grid(column=0, row=0, padx=10, pady=10)

        self.codigo=ttk.Entry(self)
        self.codigo.grid(column=1, row=0, padx=10, pady=10)

        self.nomLabel = Label(self, text="Nombre: ")
        self.nomLabel.grid(column=0, row=1, padx=10, pady=10)

        self.nombre = ttk.Entry(self)
        self.nombre.grid(column=1, row=1, padx=10, pady=10)

        self.var=BooleanVar(self)

        self.verificar=Checkbutton(self,text="Registrar cantidad",
                                   variable=self.var, command=self.cambiar)
        self.verificar.grid(column=0, row=2, columnspan=2)

        self.cantLabel = Label(self, text="Cantidad: ")
        self.cantLabel.grid(column=0, row=3, padx=10, pady=10)

        self.cantidad = ttk.Spinbox(self, state="disabled")
        self.cantidad.grid(column=1, row=3, padx=10, pady=10)

        self.añadirBot=Button(self, text="Agregar", command=self.setData)
        self.añadirBot.grid(column=1, row=4, columnspan=2)


    def cambiar(self):
        st="normal" if self.var.get() else "disabled"
        self.cantidad.config(state=st)

    def setData(self):
        self.cod=self.codigo.get()
        self.nom=self.nombre.get()
        self.cant=self.cantidad.get()
        self.procesando=False

    def getData(self, list):
        while self.procesando:
            pass
        self.añadirLista(list,self.cod, self.nom, self.cant)

    def añadirLista(list, cod=None, nom=None, cant=None):
        item = list.insert("", END, text=cod,
                                values=(nom, cant.__str__()), tags=("t",))




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
        añadir=AñadirNuevo(self)
        time.sleep(5)
        data=añadir.getData(self.list)

    def eliminarMaterial(self):
        pass

    def editarMaterial(self):
        pass


