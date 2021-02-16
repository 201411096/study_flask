# 1. while 이용
# def gen():
#     count = 0
#     while True:
#         yield count
#         count+=1

# 1. for문 이용
def gen():
    for i in range(10000):
        yield i

# test1
# generator = gen()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# test2
generator = gen()
def makeListFromGenerator(gen):
    resultList = []    
    try:
        while True:
            element = next(gen)
            resultList.append(element)
    except:
        return resultList

myList = makeListFromGenerator(generator)
print(myList)