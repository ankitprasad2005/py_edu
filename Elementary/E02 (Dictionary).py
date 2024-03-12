# Dictionary 
# are mutable

dct1 = { 'k1': 5 , 'k2': 2 , 'k3': 4 , 'k4': 1 , (8, 'd') : 'h'}

print(dct1['k1'])

dct1['k2'] = 9
print(dct1)

dct1['k5'] = 8
print(dct1)

dct1.pop('k3')
print(dct1)
del dct1['k4']
print(dct1)

print(dct1.values())
print(dct1.items())

dct1.clear()
print(dct1)
