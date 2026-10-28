
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Microservicio de Clientes",
    description="API para administrar los clientes",
    version="1.0.0"
)

# Datos de prueba almacenados en memoria
clientes = [
    {
        "id": 1,
        "nombre": "Carlos Perez",
        "correo": "carlos@example.com"
    }
]


class ClienteNuevo(BaseModel):
    nombre: str
    correo: str = Field(min_length=5)


@app.get("/health")
def health():
    return {"servicio": "clientes", "estado": "activo"}


@app.get("/clientes")
def listar_clientes():
    return clientes


@app.get("/clientes/{cliente_id}")
def consultar_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )


@app.post("/clientes", status_code=201)
def registrar_cliente(nuevo: ClienteNuevo):
    siguiente_id = max(
        (c["id"] for c in clientes),
        default=0
    ) + 1

    cliente = {
        "id": siguiente_id,
        "nombre": nuevo.nombre,
        "correo": nuevo.correo
    }

    clientes.append(cliente)
    return cliente
