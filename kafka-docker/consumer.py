from kafka import KafkaConsumer
import json

# Kafka configuration
KAFKA_TOPIC = 'json-topic'
KAFKA_BOOTSTRAP_SERVERS = ['192.168.29.170:9092']  # Change to your Kafka broker's address

# Initialize Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',  # Start reading at the earliest available message
    enable_auto_commit=True,        # Commit the offset of messages consumed
    group_id='json-consumer-group', # Consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize the JSON data
)

# Consume messages from Kafka
print("Listening for messages...")
for message in consumer:
    # message.value contains the JSON data
    print(f"Consumed message: {message.value}")

