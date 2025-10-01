from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from kafka import KafkaProducer
import json
import time

# --- Configuração do Kafka Producer ---
try:
    # Damos um tempo para o Kafka iniciar completamente
    time.sleep(5)
    producer = KafkaProducer(
        bootstrap_servers="kafka:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    print("Successfully connected to Kafka!")
except Exception as e:
    print(f"Could not connect to Kafka: {e}")
    producer = None

# --- Configuração do FastAPI ---
app = FastAPI(
    title="VibraCore - Product Service",
    description="Microsserviço responsável por gerenciar produtos.",
    version="0.1.0",
)

db: List[Dict[str, Any]] = [
    {"id": 1, "name": "Smartphone G-Model", "price": 1500.00},
    {"id": 2, "name": "Laptop ProMax", "price": 7500.00},
]


@app.get("/")
def read_root():
    return {"status": "Product Service is running!"}


@app.get("/products", response_model=List[Dict[str, Any]])
def get_products():
    return db


@app.post("/products", status_code=201)
def create_product(product: Dict[str, Any]):
    new_id = max(p["id"] for p in db) + 1 if db else 1
    new_product = {"id": new_id, "name": product["name"], "price": product["price"]}
    db.append(new_product)

    # Envia o evento para o Kafka
    if producer:
        try:
            producer.send("product_created", new_product)
            producer.flush()  # Garante que a mensagem seja enviada
            print(f"Event 'product_created' sent for product ID {new_id}")
        except Exception as e:
            print(f"Failed to send message to Kafka: {e}")

    return new_product
