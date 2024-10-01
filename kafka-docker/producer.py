from kafka import KafkaProducer
import json

# Kafka configuration
KAFKA_TOPIC = 'json-topic'
KAFKA_BOOTSTRAP_SERVERS = ['192.168.29.170:9092']  # Change this to your Kafka broker's address

# Sample JSON data
data = {
    "id": "001",
    "name": "Sample Product",
    "price": 99.99,
    "in_stock": True,
    "tags": ["sample", "product", "json"],
}

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serialize JSON to a byte array
    retries=5,  # Retry sending messages on failure
    acks='all',  # Wait for all in-sync replicas to acknowledge
    linger_ms=10,  # Wait for 10 ms before sending (for batching)
)

# Send the JSON data to the Kafka topic
future = producer.send(KAFKA_TOPIC, value=data)

# Wait for the message to be sent
try:
    record_metadata = future.get(timeout=10)
    print(f"Message sent successfully. Topic: {record_metadata.topic}, Partition: {record_metadata.partition}, Offset: {record_metadata.offset}")
except Exception as e:
    print(f"Error sending message: {e}")

# Ensure all messages are sent before exiting
producer.flush()
producer.close()
