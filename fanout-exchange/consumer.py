import pika


def consume():
    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body))
        # acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue="x_queue",durable=True)
    # Declare the fanout exchange and queue
    channel.exchange_declare(exchange='user_exchanges', exchange_type='fanout', durable=True)

    queue_name = "x_queue"  # result.method.queue

    # Bind the queue to the exchange
    channel.queue_bind(exchange='user_exchanges', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    # Set up the callback function for incoming messages
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

    # Start consuming messages
    channel.start_consuming()


if __name__ == '__main__':
    consume()
