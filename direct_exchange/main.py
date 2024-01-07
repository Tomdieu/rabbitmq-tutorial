from __future__ import  absolute_import

# from direct_exchange import publish
from producer import publish


def main():
    for i in range(0,100000):
        publish(exchange='logs', routing_key='log_service', body=f"Message {i}")


if __name__ == '__main__':
    main()
