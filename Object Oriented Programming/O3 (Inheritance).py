print ('OOP 3')
print ('super class, .super(), overwriting')
print()

class dumy(object):
	def __init__(self, name, size, colour):
		self.name = name
		self.size = size
		self.colour = colour
	def describe(self):
		print('The size of', self.name, 'is', self.size, 'which is', self.colour, 'in colour.')
	def dis_size(self):
		if self.size >= 10:
			print('Big statue :)')
		else:
			print('Small statue :(')


class idol(dumy):
	def __init__(self, name, size, colour, prize):
		super().__init__(name, size, colour)
		self.prize = prize
	def describe(self):
		print('Prize of', self.name, 'is', self.prize, 'which is', self.size, 'in size of', self.colour, 'colour.')


class statue(dumy):
	def __init__(self, name, size, colour, material):
		super().__init__(name, size, colour)
		self.material = material
	def describe(self):
		print(self.name, 'is made up of', self.material, 'which is', self.size, 'in size and of', self.colour, 'colour.')


class monument(statue):
	def __init__(self, name, size, colour, material, area):
		super().__init__(name, size, colour, material)
		self.area = area
	def describe(self):
		print(self.name, 'is made in area of', self.area, 'made up of', self.material, 'which is', self.size, 'in size and of', self.colour, 'colour.')


obj1 = dumy('obj1', 10, 'white')
obj2 = statue('obj2', 7, 'blue', 'Marble')
obj3 = idol('obj3', 9, 'green', 2500)
obj4 = monument('obj4', 13, 'red', 'sandstone', '1500sq.ft.')
obj1.describe()
obj2.describe()
obj3.describe()
obj4.describe()

print()
print('OOP 4')