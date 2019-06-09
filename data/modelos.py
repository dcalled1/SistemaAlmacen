from pymongo import *
import datetime


class Conexion:
    uri = 'mongodb+srv://almacen:almacenPass@pandoracluster-mibdw.azure.mongodb.net/AlmacenDB?retryWrites=true' #link Conexion
    dbname = 'AlmacenDB' 

    def __init__(self):

        self.client = MongoClient() #Inicializando mongo

        self.db = self.client[self.dbname] 

        self.material = self.db['Material']       # tabla material
        self.historial = self.db['Historial']     # tabla historial
        self.devolucion = self.db['Devolucion']   # tabla devolucion

    def cerrar(self):
        self.client.close()

    def anadirMaterial(self, codigo, nombre, cantidad=-1):
        post = {
            'codigo': codigo,
            'nombre': nombre,
            'cantidad': cantidad
        } #Diccionario con la información del material
        self.material.insert(post) #Agregar a la tabla material

    def listarMateriales(self):
        return self.material.find() #Buscar en la BD
        
    def quitarMaterial(self, codigo, nombre):
        ids=self.material.remove({'codigo': codigo, 'nombre': nombre}) #Quitarlo de la BD

    def agregarHistorial(self,codigo,cantidad,nombre):
        post = {
            'codigo':codigo,
            'cantidad':cantidad,
            'nombre':nombre
        }
        self.material.find_one(post) #Buscar para mostrar en el historial
        #Ese nombre se pondrá en el otro frame
        #obtener la fecha

    def listarHistorial(self):
        return self.historial.find() #Retorna el historial

    def buscarHistorial(self, prestante, fecha):
        return self.historial.find_one({'prestante': int(prestante), 'fecha': fecha}) #Retorna el diccionario específico en historial con el id y la fecha

    def buscarMatxID(self, id):
        return self.material.find_one({'_id': id}) #Retorna el diccionario con el id

    def buscarHistxID(self, id):
        return self.historial.find_one({'_id': id}) #Retorna el diccionario con el ID

    def buscarDevxID(self, id):
        return self.devolucion.find_one({'_id': id}) #Retorna el diccionario con el ID

    def listarDevoluciones(self):
        return self.devolucion.find() #Busca en devoluciones

    def buscarDevoluciones(self, prestante, fecha):
        return self.devolucion.find_one({'prestante': int(prestante), 'fecha': fecha}) #Retorna el diccionario específico en devoluciones con el id y la fecha
        
    def anadirPedido(self, prestante, materiales):
        print(materiales)
        post={'prestante': prestante, 'materiales': materiales, 'fecha': datetime.datetime.now()} #Añade la fecha actual al pedido
        self.historial.insert(post) #Agrega a historial
        self.devolucion.insert(post) #Agrega a devolucion
		
    def buscarMaterial(self, codigo, nombre):
        return self.material.find_one({'codigo': codigo , 'nombre': nombre}) #Retorna el diccionario de material específico

    def checarDevolucion(self, id):
        if self.devolucion.find({'prestante': id}).count() == 0: #Mirar si existe la devolución
            return False
        else:
            return True

    def listarMatPrestante(self, prest):
        docs = self.devolucion.find({'prestante': prest}) #Materiales del prestante
        materiales=[]
        for doc in docs:
            materiales.extend(doc.get('materiales'))
        return materiales

    def devolverMaterial(self, prest):
        ids=self.devolucion.remove({'prestante': prest})
