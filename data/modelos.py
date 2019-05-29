from pymongo import *
import datetime


class Conexion:
    uri = 'mongodb+srv://almacen:almacenPass@pandoracluster-mibdw.azure.mongodb.net/AlmacenDB?retryWrites=true'
    dbname = 'AlmacenDB'

    def __init__(self):

        self.client = MongoClient()

        self.db = self.client[self.dbname]

        self.material = self.db['Material']
        self.historial = self.db['Historial']
        self.devolucion = self.db['Devolucion']

    def cerrar(self):
        self.client.close()

    def anadirMaterial(self, codigo, nombre, cantidad=-1):
        post = {
            'codigo': codigo,
            'nombre': nombre,
            'cantidad': cantidad
        }
        print(post)
        self.material.insert(post)

    def listarMateriales(self):
        return self.material.find()
        
    def quitarMaterial(self, codigo, nombre):
        ids=self.material.remove({'codigo': codigo, 'nombre': nombre})

    def agregarHistorial(self,codigo,cantidad,nombre):
        post = {
            'codigo':codigo,
            'cantidad':cantidad,
            'nombre':nombre
        }
        self.material.find_one(post)
        #Ese nombre se pondrá en el otro frame
        #obtener la fecha

    def listarHistorial(self):
        return self.historial.find()

    def buscarHistorial(self, prestante, fecha):
        return self.historial.find_one({'prestante': int(prestante), 'fecha': fecha})

    def buscarMatxID(self, id):
        return self.material.find_one({'_id': id})

    def buscarHistxID(self, id):
        return self.historial.find_one({'_id': id})

    def buscarDevxID(self, id):
        return self.devolucion.find_one({'_id': id})

    def listarDevoluciones(self):
        return self.devolucion.find()

    def buscarDevoluciones(self, prestante, fecha):
        return self.devolucion.find_one({'prestante': prestante, 'fecha': fecha})
        
    def anadirPedido(self, prestante, materiales):
        print(materiales)
        post={'prestante': prestante, 'materiales': materiales, 'fecha': datetime.datetime.now()}
        self.historial.insert(post)
        self.devolucion.insert(post)
		
    def buscarMaterial(self, codigo, nombre):
        return self.material.find_one({'codigo': codigo , 'nombre': nombre})

    def checarDevolucion(self, id):
        if self.devolucion.find({'prestante': id}).count() == 0:
            return False
        else:
            return True

    def listarMatPrestante(self, prest):
        docs = self.devolucion.find({'prestante': prest})
        materiales=[]
        for doc in docs:
            materiales.extend(doc.get('materiales'))
        return materiales

    def devolverMaterial(self, prest):
        ids=self.devolucion.remove({'prestante': prest})





