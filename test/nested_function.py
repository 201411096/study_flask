from datetime import datetime
def fn1(str1):
    print('start fn1 ...')
    def fn2(str2):
        print('start fn2 ...')
        print('end fn2 ...')
        return str1+str2
    print('end fn1 ...')
    return fn2

def fn3():
    print('start fn3 ...')
    datestr = fn1('abc')
    print(datestr)
    print('end fn3 ...')

fn3()