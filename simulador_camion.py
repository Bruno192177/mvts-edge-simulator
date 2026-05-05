import pika
import json
import time
import random
from datetime import datetime

RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'telemetry.gps'
VEHICLE_ID = "CAMION_001"

lat_actual = 27.9150
lon_actual = -110.9000

def iniciar_simulacion():
    print("Conectando a RabbitMQ...")

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST)
        )
        channel = connection.channel()
    except Exception as e:
        print("Error:", e)
        return

    channel.queue_declare(queue=QUEUE_NAME)

    print("Simulador iniciado...\n")

    global lat_actual, lon_actual

    try:
        while True:
            lat_actual += random.uniform(-0.0005, 0.0005)
            lon_actual += random.uniform(-0.0005, 0.0005)

            payload = {
                "vehicle_id": VEHICLE_ID,
                "latitude": round(lat_actual, 6),
                "longitude": round(lon_actual, 6),
                "status": "en_ruta",
                "timestamp": datetime.now().isoformat()
            }

            mensaje = json.dumps(payload)

            channel.basic_publish(
                exchange='',
                routing_key=QUEUE_NAME,
                body=mensaje
            )

            print("Enviado:", mensaje)

            time.sleep(3)

    except KeyboardInterrupt:
        print("Detenido")
        connection.close()

if __name__ == '__main__':
    iniciar_simulacion()