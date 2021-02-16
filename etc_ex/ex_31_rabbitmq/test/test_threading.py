import threading
import random
import time

def myRandomNumber(data):
    print('--- myRandomNumber start(' + str(data) +  ') ---')
    ranNum = random.randrange(1, 100)
    print('number('+str(data)+') : ' + str(ranNum))
    time.sleep(ranNum/10)    
    print('--- myRandomNumber end(' + str(data) +  ')   ---')

for i in range(10):
    # myRandomNumber(i)
    th = threading.Thread(target=myRandomNumber, args=[i]  )
    th.start()
    