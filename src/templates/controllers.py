from bson import ObjectId 
from src.models.database import collection
from src.models.model import TraineeModel, TraineeUpdateModel

def helper_trainee(trainee) -> dict:
    return {
        "id": str(trainee["_id"]),
        "document": trainee["document"],
        "name": trainee["name"],
        "lastname": trainee["lastname"],
        "email": trainee["email"],
        "age": trainee["age"],
        "program": trainee["program"],
        "record_number": trainee["record_number"]
    }
    
    
    # FUNCION DE CREAR DATOS DE UN APRENDIZ (TRAINEE)
    
def create_trainee(trainee: TraineeModel) -> dict:
    trainee_dict =trainee.model_dump() #el método model_dump() de Pydantic convierte el modelo en un diccionario de Python.
    result = collection.insert_one(trainee_dict) #aqui se inserta el diccionario en la colección de MongoDB y se obtiene un objeto de resultado que contiene información sobre la operación de inserción.
    new_trainee = collection.find_one({"_id": result.inserted_id}) #aqui se busca el documento recién insertado en la colección utilizando el ID generado por MongoDB.
    return helper_trainee(new_trainee) #aqui se llama a la función helper_trainee para convertir el documento de MongoDB en un diccionario de Python y se devuelve como resultado de la función create_trainee.


    # OBTENER TODOS LOS APRENDICES (TRAINEES)
def get_all_trainees(): 
    trainees = []
    for trainee in collection.find():
        trainees.append(helper_trainee(trainee))
    return trainees

    # OBTENER DATOS DEL APRENDIZ POR ID
def get_trainee_by_id(id: str):
    trainee = collection.find_one({"_id": ObjectId(id)})
    if trainee:
        return helper_trainee(trainee)
    return None

    # ACTUALIZAR DATOS DEL APRENDIZ POR ID
def update_trainee(id: str,data: TraineeUpdateModel):
    data_update = {
        k: v 
        for k, v in data.model_dump().items()
        if v is not None
    }
    if data_update:
        collection.update_one(
        {"_id": ObjectId(id)}, 
        {"$set": data_update}
        )
        trainee_updated = collection.find_one({"_id": ObjectId(id)})
        return helper_trainee(trainee_updated)
    return None

    # ELIMINAR DATOS DEL APRENDIZ POR ID
def delete_trainee(id: str):
    trainee = collection.find_one({"_id": ObjectId(id)})
    if trainee:
        collection.delete_one({"_id": ObjectId(id)})
        return True
    return False

    # OBTENER DATOS DEL APRENDIZ POR DOCUMENTO
    