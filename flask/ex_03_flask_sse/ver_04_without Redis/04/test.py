################################################################################
# class abc:
#     def __init__(self):
#         self.listeners = {}
    
#     def listen(self, id, content):
#         if id in self.listeners:
#             pass
#         else:
#             self.listeners[id]=content

# aa = abc()

# aa.listen('aa', 'aa')
# print(aa.listeners)
# aa.listen('bb', 'bb')
# print(aa.listeners)
# aa.listen('cc', 'cc')
# print(aa.listeners)
# aa.listen('aa', 'ee')
# print(aa.listeners)
################################################################################


################################################################################
# def func_flow(id):
#     num = 1
#     if id > 0 :
#         num = 5
#         pass
#     else:
#         num = -5
#         pass
#     return num

# print(func_flow(-3))
################################################################################


################################################################################
# listeners = [1,2,3,4,5,6,7,8]

# for i in reversed(range(len(listeners))):
#     print(listeners[i])
################################################################################


################################################################################
# setA = set()
# setA.add('a')
# setA.add('a')
# setA.add('a')
# setA.add('b')
# try:
#     setA.remove('c')
# except:
#     print('keyerror..')
# print(setA)
################################################################################


################################################################################
# aset = set()
# print(len(aset))
# aset.add('a')
# print(len(aset))
# aset.add('a')
# print(len(aset))
# aset.add('b')
# print(len(aset))
################################################################################


################################################################################
aDict = {"a":'aa', 'b':'bb'}
print(aDict)
aDict.pop('a')
print(aDict)
aDict.pop('a')
################################################################################