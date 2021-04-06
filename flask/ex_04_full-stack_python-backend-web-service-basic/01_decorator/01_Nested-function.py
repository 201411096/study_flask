def outer_func():
    print('call outer_func function')

    def inner_func():
        return 'call inner_func function'
    
    print(inner_func())

def outer_func2(num):
    def inner_func():
        print(num)
        return 'inner_func value'
    return inner_func

outer_func()
print('====================')

fn = outer_func2(15)
print(fn())
