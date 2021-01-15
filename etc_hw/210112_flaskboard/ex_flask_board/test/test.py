data = {'a':"aa", 'b':'bb'}
data2 = {'c':'cc', 'd':'dd', 'a':'a'}
data3 = {}
data.update(data2)

print(data)
data.update(data3)
print(data)