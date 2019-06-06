from pymongo import MongoClient


class Conexion:
    uri = 'mongodb+srv://almacen:almacenPass@pandoracluster-mibdw.azure.mongodb.net/AlmacenDB?retryWrites=true'
    dbname = 'AlmacenDB'

    def __init__(self):

        self.client = MongoClient(self.uri)

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
