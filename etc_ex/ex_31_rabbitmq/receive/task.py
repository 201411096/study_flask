import random
import time

# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)

def task1(ch, method, properties, body):
    # print('check arguemnts ...')
    # print(ch)
    # print(method)
    # print(properties)
    # 단순 메시지 테스트
    # print(body)
    # dictionary 테스트
    import json
    body = json.loads(body)
    print('body : ', body)
    # print(body['a'])
    
    num = random.randrange(1, 1000000)
    print(num)
    time.sleep(num/100000)
    return num

# for i in range(100):
#     task1()