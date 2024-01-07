from typing import Any,Optional

import pika


def publish(exchange: str, body: Any):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a fanout exchange

    channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)

    # Declare a queue
    channel.queue_declare(queue='user_exchanges', durable=True)

    # Bind the queue to the exchange
    channel.queue_bind(exchange=exchange, queue='user_exchanges')

    # Publish the message to the exchange
    # Here we don't specify a routing key as we are using a fanout exchange
    channel.basic_publish(exchange=exchange, routing_key='', body=body)
    print(" [x] Sent 'Direct Exchange Message'", body)
    connection.close()
