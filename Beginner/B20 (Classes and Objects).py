print('Day 20')
print('Creating Classes and Objects')
print()

obj1 = 'Hello'
obj2 = 7
obj3 = True
print(type(obj1))
print(type(obj2))
print(type(obj3))
print()

class myClass():
	def __init__(self, x):
		self.num = x
	def display(self, y):
		print (y)

print('Here in 1st def of the class we put "self." to make that variable global in the class.')

num1 = myClass(27)
print(type(num1))
print(num1)

num1.display(num1.num)

print()
print('Day 21')