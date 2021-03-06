import pika, sys, os
from task import *

def main():
    credentials = pika.PlainCredentials(username='abc', password='abc')
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.51', credentials=credentials))
    channel = connection.channel()

    queue_name = 'queue_name_01'
    channel.queue_declare(queue=queue_name)

    # channel.basic_consume(queue=queue_name, on_message_callback=task1, auto_ack=True)
    channel.basic_consume(queue=queue_name, on_message_callback=task1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)