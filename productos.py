
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Microservicio de Productos",
    description="API para administrar el catalogo de la tienda",
    version="1.0.0"
)

# Datos de prueba almacenados en memoria
productos = [
    {
        "id": 1,
        "nombre": "Teclado",
        "precio": 80000,
        "stock": 15
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 45000,
        "stock": 20
    }
]


class ProductoNuevo(BaseModel):
    nombre: str
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)


@app.get("/health")
def health():
    return {"servicio": "productos", "estado": "activo"}


@app.get("/productos")
def listar_productos():
    return productos


@app.get("/productos/{producto_id}")
def consultar_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


@app.post("/productos", status_code=201)
def registrar_producto(nuevo: ProductoNuevo):
    siguiente_id = max(
        (p["id"] for p in productos),
        default=0
    ) + 1

    producto = {
        "id": siguiente_id,
        "nombre": nuevo.nombre,
        "precio": nuevo.precio,
        "stock": nuevo.stock
    }

    productos.append(producto)
    return producto
