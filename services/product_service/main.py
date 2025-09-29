from fastapi import FastAPI
from typing import List, Dict

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="Product Service",
    description="Service for managing products",
    version="0.1.0",
)

# Um banco de dados em memória para simular nosso catálogo de produtos
products_db: List[Dict] = [
    {"id": 1, "name": "Smartphone G-Model", "price": 1500.00},
    {"id": 2, "name": "Laptop ProMax", "price": 7500.00},
    {"id": 3, "name": "Fone de Ouvido Blast", "price": 450.50},
]


@app.get("/")
def read_root():
    """Endpoint de boas-vindas para verificar se o serviço está no ar."""
    return {"status": "Product Service is running!"}


@app.get("/products")
def get_products():
    """Endpoint para listar todos os produtos disponíveis."""
    return products_db
