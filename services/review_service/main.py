import time
import json
from kafka import KafkaConsumer

print("Review Service Starting...")

# Dando um tempo para o Kafka subir completamente
time.sleep(10)

try:
    consumer = KafkaConsumer(
        "product_created",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        group_id="review-group",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )
    print("Successfully connected to Kafka!")

    for message in consumer:
        product_data = message.value
        print(f"EVENT RECEIVED! Review system processing product: {product_data}")

except Exception as e:
    print(f"Failed to connect to Kafka: {e}")
