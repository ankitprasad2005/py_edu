# filter function

def fn1(x):
    return x%2 != 0

def fn2(x):
    return x*10

ls1 = [1,2,4,5,6,5,4,3,2,0]

ls2 = list(filter(fn1, ls1))

ls3 = list(map(fn2, filter(fn1, ls1)))

print(ls1, ls2, ls3)

# map and filter are data type on their own so need to convert to list