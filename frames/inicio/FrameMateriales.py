from tkinter import ttk
from tkinter import  *
from data.modelos import Conexion

class AñadirNuevo(Toplevel):

    procesando=True
    cod=None
    nom=None
    cant=None

    def __init__(self, list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Añadir material")
        self.config()

        self.lista=list

        self.conexion=Conexion()

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

        self.cantidad = Entry(self, state="disabled")
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
            #self.lista.insert("", END, text=self.cod,
                        #values=(self.nom, self.cant.__str__()), tags=("t",))
            if self.cant=='':
                self.conexion.anadirMaterial(self.cod, self.nom)
            else:
                self.conexion.anadirMaterial(self.cod, self.nom, int(self.cant))
            self.master.listar()
            self.destroy()

    def cancel(self):
        self.destroy()





class Materiales(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.conexion=Conexion()

        self.list=ttk.Treeview(self, columns=("nombre", "cantidad"), selectmode=BROWSE)

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        self.list.heading("cantidad", text="Cantidad")

        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)

        self.listar()

        self.list.pack(expand=True, fill=BOTH)

        self.agregar=Button(self, text="Agregar nuevo...",
                            command=self.nuevoMaterial)
        self.agregar.pack(side=RIGHT)

        self.eliminar=Button(self, text="Eliminar", state="disabled",
                             command=self.eliminarMaterial)
        self.eliminar.pack(side=RIGHT)

        #self.editar = Button(self, text="Editar", state="disabled",
         #                      command=self.editarMaterial)
        #self.editar.pack(side=RIGHT)

        self.pack(expand=True, fill=BOTH)


    def itemSeleccionado(self, event):
        self.eliminar.config(state="normal")
        self.editar.config(state="normal")


    def nuevoMaterial(self):
        añadir=AñadirNuevo(self.list, master=self)

    def eliminarMaterial(self):
        item=self.list.item(self.list.selection())
        self.conexion.quitarMaterial(item.get('text'), item.get('values')[0])
        self.listar()

    def editarMaterial(self):
        pass

    def listar(self):
        docs=self.conexion.listarMateriales()
        self.list.delete(*self.list.get_children())
        for doc in docs:
            if doc.get('cantidad')==-1:
                self.list.insert('', END, text=doc.get('codigo'),
                             values=(doc.get('nombre')), tags=('t'))
            else:
                self.list.insert('', END, text=doc.get('codigo'),
                             values=(doc.get('nombre'), str(doc.get('cantidad'))), tags=('t'))



