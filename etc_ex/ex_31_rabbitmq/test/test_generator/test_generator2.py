# generator를 for문에..
def gen():
    for i in range(100):
        yield i

generator = gen()

for row in generator:
    print(row)