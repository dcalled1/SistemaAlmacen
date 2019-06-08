from tkinter import *
from tkinter import ttk
from data.modelos import *

class NuevoCarnet(Toplevel):
    def __init__(self, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Nuevo pedido')

        self.conexion=Conexion() #Instancia clase conexión

        self.id=id

        self.list=ttk.Treeview(self, columns=("nombre", "disponibilidad")) #Crear treeview

        self.list.heading("#0", text="Código")
        self.list.heading("nombre", text="Nombre")
        self.list.heading("disponibilidad", text="Disponibilidad")

        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)

        self.listar()

        self.list.pack(expand=True, fill=BOTH)

        self.aceptar=Button(self, text="Confirmar selección", #Botón confirmar
                            command=self.confirmar)
        self.aceptar.pack(side=RIGHT)

        self.cancel=Button(self, text="Cancelar", #Botón cancelar acción
                             command=self.cancelar)
        self.cancel.pack(side=RIGHT)



    def itemSeleccionado(self):
        pass

    def confirmar(self):
        ids=self.list.selection() #Obtener los materiales seleccionados
        ls=[]
        for idmat in ids:
            data=self.list.item(idmat)
            dbobj=self.conexion.buscarMaterial(data.get('text'), data.get('values')[0]) #Buscar en la base de datos los materiales.
            ls.append(dbobj.get('_id')) #Agregar el id al arreglo
        self.conexion.anadirPedido(self.id, ls) #Añadir nuevo material prestado a la base de datos.
        self.master.historial.listar() #Actualizar historial
        self.master.devoluciones.listar() #Actualizar devoluciones
        self.destroy()

    def cancelar(self):
        self.destroy()
        
    def listar(self):
        docs=self.conexion.listarMateriales() #Mostrar los materiales que hay en la base de datos.
        self.list.delete(*self.list.get_children())
        for doc in docs:
            cantidad=int(doc.get('cantidad'))
            if cantidad != -1:
                if cantidad == 0:
                    self.list.insert('', END, text=doc.get('codigo'), values=(doc.get('nombre'), 'No disponible')) #Mostrar en el treeview si la cantidad no aplica
                else:
                    self.list.insert('', END, text=doc.get('codigo'), values=(doc.get('nombre'), 'Disponible')) #Mostrar en el treeview si existe
            else:
                self.list.insert('', END, text=doc.get('codigo'), values=(doc.get('nombre'), 'Disponible'))


    def cancelar(self):
        self.destroy()
