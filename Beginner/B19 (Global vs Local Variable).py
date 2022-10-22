print('Day 19')
print('Global and local variables')
print()

num = 7
inp = 'Hello'
def func1(x):
	num = 10
print (num)

def func2(y):
	num = 13
	print(num)	
func2(73)

print (num)

def func3(z):
	global num
	num = 23
func3(36)

print (num)
print(num)

print()
print('Day 20')