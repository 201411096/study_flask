import pika
import json
# username과 password는 미리 설정했어야 함
credentials = pika.PlainCredentials(username='abc', password='abc')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.51', credentials=credentials))
channel = connection.channel()

queue_name = 'queue_name_01'
channel.queue_declare(queue=queue_name)

# myMessage = 'abcabc ... ...'
# channel.basic_publish(exchange='', routing_key=queue_name, body=myMessage)

myMessage = {"a":"aa", "b":"bb"}
myMessage = json.dumps(myMessage)
channel.basic_publish(exchange='', routing_key=queue_name, body=myMessage)

connection.close()