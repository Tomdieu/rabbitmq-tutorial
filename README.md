# RabbitMq Tutorial

RabbitMQ is a robust message-queuing software, often referred to as a message broker or queue manager. This repository provides a comprehensive guide on leveraging RabbitMQ for effective communication in distributed systems.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Python](https://www.python.org/downloads/)
- [RabbitMQ](https://www.rabbitmq.com/download.html)

## RabbitMq Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/Tomdieu/rabbitmq-tutorial.git
    ```

2. **Run rabbitmq image**

    ```sh
    docker compose up
    ```

## Run each example

Navigate to the example directory of your choice:

```sh
cd direct-exchange
```

### Running Producer

Execute the following command to run the producer:

```sh
python main.py
```

### Running Consumer

Execute the following command to run the consumer:
Run `consumer`

```sh
python consumer.py
```

Feel free to explore other examples in the repository for a deeper understanding of RabbitMQ and its features.

By following this tutorial, you'll gain hands-on experience with RabbitMQ, enabling you to enhance communication and messaging in your applications. If you encounter any issues or have questions, please refer to the documentation or create an issue in this repository.

Happy coding!
