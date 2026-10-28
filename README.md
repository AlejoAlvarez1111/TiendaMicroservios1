
# Tienda Virtual - Arquitectura de Microservicios

## Descripcion

Proyecto academico desarrollado con Python y FastAPI.
Separa la gestion de productos, clientes y pedidos en
tres servicios independientes que exponen API REST.

## Tecnologias

- Python
- FastAPI
- Uvicorn
- HTTP / REST

## Requisitos

Python instalado y acceso a una terminal.

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Ejecucion

Abrir tres terminales en la carpeta del proyecto.

Terminal 1:

```powershell
.\.venv\Scripts\python.exe -m uvicorn productos:app --reload --port 8001
```

Terminal 2:

```powershell
.\.venv\Scripts\python.exe -m uvicorn clientes:app --reload --port 8002
```

Terminal 3:

```powershell
.\.venv\Scripts\python.exe -m uvicorn pedidos:app --reload --port 8003
```

## Documentacion de las API

- Productos: http://127.0.0.1:8001/docs
- Clientes: http://127.0.0.1:8002/docs
- Pedidos: http://127.0.0.1:8003/docs

## Limitaciones

Los datos se almacenan en memoria y se pueden perder
cuando se reinician los servicios.

El servicio de pedidos recibe los datos del producto
desde la solicitud y no verifica el inventario real.
