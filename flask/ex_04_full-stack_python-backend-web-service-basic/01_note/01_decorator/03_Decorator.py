import datetime
import inspect
import functools

print('==============================')
def print_decorator(func):
    def wrapper(*args, **kwars):
        print('time ... : ' + str(datetime.datetime.now()))
        func(*args, **kwars)
        print('... time : ' + str(datetime.datetime.now()))
    return wrapper

@print_decorator
def myPrinter(msg):
    print(msg)

tempFunc = myPrinter
myPrinter('bbb')
tempFunc('abc')
print('==============================')
def decorator1(function):
    print('call decorator1')
    def wrapper():
        print('before decorator1 wrapper')
        function()
        print('after decorator1 wrapper')
    return wrapper
 
def decorator2(function):
    print('call decorator2')
    def wrapper():
        print('before decorator2 wrapper')
        function()
        print('after decorator2 wrapper')
    return wrapper

@decorator1
@decorator2
def myPrinter2():
    print('myPrinter2-content ...')
print('after declaration ...')
myPrinter2()
print('==============================')
def content_wrapper1(function):
    def wrapper(*args, **kwargs):
        return '***' + function(*args, **kwargs) + '***'
    return wrapper

def content_wrapper2(function):
    def wrapper(*args, **kwargs):
        return '---' + function(*args, **kwargs) + '---'
    return wrapper

@content_wrapper1
@content_wrapper2
def myPrinter3(string):
    return string

print (myPrinter3('myMessage'))
print('==============================')

def functools_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('before inner function')
        func(*args, **kwargs)
        print('after inner function')
        return None
    return wrapper

@functools_decorator
def functools_printer(msg):
    print(msg)

functools_printer('abc')

print('==============================')

def functools_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('before inner function')
        result = func(*args, **kwargs)
        print('after inner function')
        return result
    return wrapper

@functools_decorator2
def functools_printer(msg):
    print(msg)

functools_printer('bbb')