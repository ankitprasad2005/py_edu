# map and list comprihention

ls1 = [1,2,4,5,6,5,4,3,2,0]

def fn1(x):
    return x**x

ls2 = list(map(fn1, ls1))

ls3 = [fn1(x) for x in ls1]

ls4 = [fn1(x) for x in ls1 if x%2 != 0]

print(ls1 ,ls2, ls3, ls4)

# to copy list 
ls5 = ls1[:]
