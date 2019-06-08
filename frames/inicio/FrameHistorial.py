from tkinter import ttk
from tkinter import *
from data.modelos import *
import time

class Historial(ttk.Frame): 

    def __init__(self, *args, **kwargs):  
        self.conexion= Conexion() #Instancia de la clase conexión, que conecta con la base de datos en mongo.
        super().__init__(*args, **kwargs)

        self.list=ttk.Treeview(self, columns=("fecha"), selectmode=BROWSE) , # creando el TreeView para la ventana Historial
        self.list.heading("#0", text="Prestante")
        self.list.heading("fecha", text="Fecha")
        self.list.tag_bind("t", "<<TreeviewSelect>>",
                               self.itemSeleccionado)
        self.listar()  

        self.list.pack(expand=True, fill=BOTH)

        self.pack(expand=True, fill=BOTH)


    def itemSeleccionado(self, event): #Cuando se selecciona un item de historial, se abre una nueva ventana que contiene el nombre y la fecha en que se pidió
        idITEM=self.list.item(self.list.selection()) 
        y=int(idITEM.get('values')[0].split('-')[0])
        m=int(idITEM.get('values')[0].split('-')[1])
        d=int(idITEM.get('values')[0].split('-')[2])
        start=datetime.datetime(y,m,d, 0, 0, 0)
        end=datetime.datetime(y,m,d, 23, 59, 59)
        reg=self.conexion.buscarHistorial(idITEM.get('text'), {'$lt': end, '$gte': start}) #Obtener registro
        obtener = obtenerHis(reg.get("_id")) #Crear la nueva ventana en la clase obtenerHis con la información del registro.

    def listar(self):
        docs = self.conexion.listarHistorial() #Busca en la base de datos y muestra lo que encuentre de Historial
        self.list.delete(*self.list.get_children())
        for doc in docs:
            self.list.insert('', END, text=doc.get('prestante'),
                             values=(doc.get('fecha')), tags=("t",))



class obtenerHis(Toplevel): #Segundo treeView de historial
    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id=id
        self.conexion= Conexion()  #Conectando a la base de datos
        self.title("Historial")
        self.config()
        self.geometry("400x400+300+100")
        self.list=ttk.Treeview(self, columns=("nombre"))
        self.list.heading("#0", text="Codigo")
        self.list.heading("nombre", text="Nombre")

        self.listarMat() #Llama al método listar Materiales
        self.list.pack(expand=True, fill=BOTH)

    def listarMat(self):
        registro = self.conexion.buscarHistxID(self.id) #Buscamos los materiales con el id de la persona y la hora. Funciona como diccionario
        materiales=registro.get('materiales') 
        self.list.delete(*self.list.get_children())
        for i in materiales: #Para recorrer cuando se presten varios objetos a la vez
            mat=self.conexion.buscarMatxID(i)
            self.list.insert('', END, text= mat.get('codigo'), #Insertarlos a list, que es el Treeview de la interfaz gráfica obtenerHis
                             values=(mat.get('nombre')), tags=("t",))




