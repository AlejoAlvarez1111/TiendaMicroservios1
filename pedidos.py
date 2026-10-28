
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Microservicio de Pedidos",
    description="API para registrar y consultar pedidos",
    version="1.0.0"
)

# Datos de prueba almacenados en memoria
pedidos = []


class PedidoNuevo(BaseModel):
    cliente_id: int = Field(gt=0)
    producto_id: int = Field(gt=0)
    nombre_producto: str
    cantidad: int = Field(gt=0)
    precio_unitario: float = Field(ge=0)


@app.get("/health")
def health():
    return {"servicio": "pedidos", "estado": "activo"}


@app.get("/pedidos")
def listar_pedidos():
    return pedidos


@app.get("/pedidos/{pedido_id}")
def consultar_pedido(pedido_id: int):
    for pedido in pedidos:
        if pedido["id"] == pedido_id:
            return pedido

    raise HTTPException(
        status_code=404,
        detail="Pedido no encontrado"
    )


@app.post("/pedidos", status_code=201)
def registrar_pedido(nuevo: PedidoNuevo):
    siguiente_id = max(
        (p["id"] for p in pedidos),
        default=0
    ) + 1

    total = nuevo.cantidad * nuevo.precio_unitario

    pedido = {
        "id": siguiente_id,
        "cliente_id": nuevo.cliente_id,
        "producto_id": nuevo.producto_id,
        "nombre_producto": nuevo.nombre_producto,
        "cantidad": nuevo.cantidad,
        "precio_unitario": nuevo.precio_unitario,
        "total": total,
        "estado": "registrado"
    }

    pedidos.append(pedido)
    return pedido
