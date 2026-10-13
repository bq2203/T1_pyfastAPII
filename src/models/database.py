from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError


MONGO_URI = "mongodb+srv://braianquintero64_db_user:<Braian22>@cluster0.eeigrd2.mongodb.net/?appName=Cluster0"

#crear ujna instancia de; cliente en MongoDB y asignar un tiempo de espera de 3 segundos para la selección del servidor
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

#crear la bd y coleccion 
db = client.dataap
collection = db.trainee

try: 
    # intentar conectarse al servidor de MongoDB
    client.server_info()
    client.admin.command("ping")
    print("Conexión exitosa a MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print("Error de conexión a MongoDB:", e)
finally:
    #cerrar la conexion al cliente de MongoDB
    client.close()
