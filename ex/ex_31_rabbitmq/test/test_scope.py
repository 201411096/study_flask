aa = 'aaa'
bb = 55
def abc():
    print(aa)
    print(bb+54)
abc()

myList = []

def bbb():
    myList.append('a')
    myList.append('a')
    myList.append('a')

# bbb()
# print(myList)

from threading import Thread

th = Thread(target=bbb)
th.start()

th.join()

print(myList)

