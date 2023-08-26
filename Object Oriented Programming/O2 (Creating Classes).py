print ('OOP 2')
print ('__init__, self')
print()

class dumy(object):
	def __init__(self, name, size, colour):
		self.name = name
		self.size = size
		self.colour = colour
	
	def describe(self):
		print('The size of', self.name, 'is', self.size, 'which is', self.colour, 'in colour.')
	
	def change_size(self, size):
		self.size = size
	
	def add_mass(self, mass):
		self.mass = mass
	
	def describe_mass(self):
		print('Weight of', self.name, 'is', self.mass, '.')

dum1 = dumy('Dum1', 7, 'green')
dum2 = dumy('Dum2', 23, 'blue')

print(dum1)

dum1.describe()
dum2.describe()
dum1.change_size(9)
dum1.describe()
dum2.add_mass(50)
dum2.describe_mass()
print(dum1.size)
print(dum2.mass)

print()
print('OOP 3')