import pika
from typing import Any


def publish(exchange: str, routing_key: str, body: Any):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the direct exchange
    channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)

    # Declare the queue
    channel.queue_declare(queue='logs', durable=True)

    # Bind the queue to the exchange with the specified routing key
    channel.queue_bind(exchange=exchange, queue='logs', routing_key=routing_key)

    # Publish the message to the exchange with the specified routing key
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)

    print(" [x] Sent 'Direct Exchange Message' : ", body)

    connection.close()
