# lambda, ITS NOT lamda
# can also use optional parameter with lambda

def fn1(x, y=1):
    return x**y

fn2 = lambda x, y=1: x**y

print(fn1(3,5) == fn2(3,5))