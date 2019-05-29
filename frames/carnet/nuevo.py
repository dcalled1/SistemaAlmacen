from tkinter import *
from tkinter import ttk
from data.modelos import *

class NuevoCarnet(Toplevel):
    def __init__(self, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Nuevo pedido')

        self.conexion=Conexion()

        self.id=id

        self.list=ttk.Treeview(self, columns=("nombre", "disponibilidad"))

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        self.list.heading("disponibilidad", text="Disponibilidad")

        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)

        self.listar()

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
        ids=self.list.selection()
        ls=[]
        for idmat in ids:
            data=self.list.item(idmat)
            dbobj=self.conexion.buscarMaterial(data.get('text'), data.get('values')[0])
            ls.append(dbobj.get('_id'))
        self.conexion.anadirPedido(self.id, ls)
        self.master.historial.listar()
        self.master.devoluciones.listar()
        self.destroy()

    def cancelar(self):
        self.destroy()
        
    def listar(self):
        docs=self.conexion.listarMateriales()
        self.list.delete(*self.list.get_children())
        for doc in docs:
            cantidad=int(doc.get('cantidad'))
            if cantidad != -1:
                if cantidad == 0:
                    self.list.insert('', END, text=doc.get('codigo'), values=(doc.get('nombre'), 'No disponible'))
                else:
                    self.list.insert('', END, text=doc.get('codigo'), values=(doc.get('nombre'), 'Disponible'))
            else:
                self.list.insert('', END, text=doc.get('codigo'), values=(doc.get('nombre'), 'Disponible'))


    def cancelar(self):
        self.destroy()
