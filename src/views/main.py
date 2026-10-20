from fastapi import FastAPI, HTTPException, status
from src.models.model import TraineeModel, TraineeUpdateModel
from src.templates.controllers import (
    create_trainee,
    get_all_trainees,
    get_trainee_by_id,
    update_trainee,
    delete_trainee,
)
# uvicorn src.views.main:app --reload

app = FastAPI(
    title="Trainee API",
    description="API simple para gestionar datos de aprendices (trainees)",
    version="1.0.0",
)

# Mensaje de bienvenida
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de aprendices (trainees)"}

# Registrar aprendices
@app.post(
    "/trainees/", response_description="Registrar un nuevo aprendiz", status_code=status.HTTP_201_CREATED
)
def create_trainee_api(trainee: TraineeModel):
    return create_trainee(trainee)

# Obtener la lista de aprendices
@app.get("/trainees/", response_description="Obtener la lista de aprendices")
def get_all_trainees_api():
    return get_all_trainees()

# Obtener un aprendiz por su ID
@app.get("/trainees/{id}", response_description="Obtener un aprendiz por su ID")
def get_trainee_by_id_api(id: str):
    trainee = get_trainee_by_id(id)
    if not trainee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aprendiz no encontrado")
    return trainee

# Editar un aprendiz por su ID
@app.put("/trainees/{id}", response_description="Editar un aprendiz por su ID")
def update_trainee_api(id: str, trainee: TraineeUpdateModel):
    updated_trainee = update_trainee(id, trainee)
    if not updated_trainee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aprendiz no encontrarlo o sin datos a actualizar")
    return updated_trainee

#Eliminar un aprendiz
@app.delete(
    "/trainees/{id}", response_description="Eliminar datos de un aprendiz"
)
def delete_trainee_api(id: str):
    trainee = delete_trainee(id)
    if not trainee:
        raise HTTPException(
            status_code=404, detail="Aprendiz no encontrado"
        )
    return {"mnesaje": "Aprendiz eliminado"}