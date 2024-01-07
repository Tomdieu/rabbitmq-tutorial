import pika


def consume():
    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body))
        # acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the direct exchange and queue
    channel.exchange_declare(exchange='logs', exchange_type='direct', durable=True)
    # result = channel.queue_declare(queue='', exclusive=False,durable=True)
    queue_name = "logs" # result.method.queue

    # Specify the routing key ('log_service') to bind the queue to the exchange
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key='log_service')

    print(' [*] Waiting for logs. To exit press CTRL+C')

    # Set up the callback function for incoming messages
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

    # Start consuming messages
    channel.start_consuming()


if __name__ == '__main__':
    consume()
