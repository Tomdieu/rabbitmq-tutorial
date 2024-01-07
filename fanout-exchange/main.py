from producer import publish


def main():
    for i in range(1001):
        publish(exchange='user_exchanges', body='Fanout Message : {}'.format(i))


if __name__ == "__main__":
    main()
