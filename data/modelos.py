from pymongo import MongoClient


class Conexion:
    uri = 'mongodb+srv://almacen:almacenPass@pandoracluster-mibdw.azure.mongodb.net/AlmacenDB?retryWrites=true'
    dbname = 'AlmacenDB'

    def __init__(self):

        self.client = MongoClient()

        self.db = self.client[self.dbname]

        self.material = self.db['Material']
        self.historial = self.db['Historial']
        self.devolucion = self.db['Devolucion']

    def anadirMaterial(self, codigo, nombre, cantidad='NA'):
        post = {
            'codigo': codigo,
            'nombre': nombre,
            'cantidad': cantidad
        }
        print(post)
        self.material.insert_one(post)

    def listarMateriales(self):
        return self.material.find()

    def agregarHistorial(self,codigo,cantidad,nombre):
        post = {
            'codigo':codigo,
            'cantidad':cantidad,
            'nombre':nombre
        }
        self.material.find_one(post)
        #Ese nombre se pondrá en el otro frame
        #obtener la fecha

    def agregarDevolucionesPendientes(self, codigo, cantidad, nombre):
        post = {
            'codigo': codigo,
            'cantidad': cantidad,
            'nombre': nombre
        }
        self.material.find_one(post)

    def listarHistorial(self):
        return self.historial.find()

    def buscarHistorial(self, prestante, fecha):
        return self.historial.find_one({'prestante': prestante , 'fecha': fecha})

    def buscarMatxID(self, id):
        return self.material.find_one({'_id': id})

    def buscarHistxID(self, id):
        return self.historial.find_one({'_id': id})

    def listarDevoluciones(self):
        return self.devolucion.find()

    def buscarDevoluciones(self, prestante, fecha):
        return self.devolucion.find_one({'prestante': prestante, 'fecha': fecha})


