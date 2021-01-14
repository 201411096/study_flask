def decorator1(func):
    def wrapper(*args, **kwargs):
        print('before innerFunc ...')
        func(*args, **kwargs)
        print('after innerFunc ...')
    return wrapper

@decorator1
def printa(var1):
    print(var1)

printa('abc')