import pika
import os
import json

RABBITMQ_URL = os.environ.get("RABBITMQ_URL")

def send_user_created_message(user):
    try:
        connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        channel = connection.channel()
        channel.queue_declare(queue="users_queue", durable=True)
        
        message = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

        channel.basic_publish(
            exchange='',
            routing_key='users_queue',
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()
    except Exception as e:
        print("No se pudo enviar el mensaje a RabbitMQ:", e)
