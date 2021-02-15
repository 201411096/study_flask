import random
import time

# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)

def task1(channel, method, properties, body):
    # print('check arguemnts ...')
    # print(channel)
    # print(method)
    # print(properties)
    # print(body)
    num = random.randrange(1, 1000000)
    print(num)
    time.sleep(num/100000)
    return num

# for i in range(100):
#     task1()