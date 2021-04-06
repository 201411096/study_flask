"""
First-class function

1. 함수를 식별자에 바인딩할 수 있는지
2. 함수를 데이터 구조에 저장할 수 있는지
3. 함수 호출에서 함수를 인수로 전달할 수 있는지
4. 함수 호출에서 함수를 반환할 수 있는지
"""
print('==============================')
def my_func(arg_num):
    return arg_num *2

print(my_func(4))

tempFunc = my_func
print(tempFunc(4))
print('==============================')

def my_func_list(arg_list, arg_func):
    for i in arg_list:
        print(arg_func(i))

my_func_list([1,2,3,4,5], my_func)
print('==============================')

def myPrintFunc(arg_sender):
    def inner_func(msg):
        print(arg_sender + " : " + msg)
    return inner_func

tempFunc2 = myPrintFunc('sender1')
tempFunc2('abc')
