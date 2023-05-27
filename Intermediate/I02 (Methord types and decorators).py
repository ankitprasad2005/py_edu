# types of methord and decorator

class horce:
	ls_hr = []
	
	def __init__(self, name):
		self.name = name
		self.ls_hr.append(self.name)
	
	@classmethod
	# no object is required in classmethord so no self required
	# to access variable defined in the class use cls
	def num_horce(cls):
		return len(cls.ls_hr)
	
	@staticmethod
	# no need to access class variable or class object so no cls or self
	def spk_run(x):
		for x in range (0, x, 1):
			print('Running!!!!')
	
hr1 = horce('horce 1')
hr2 = horce('horce 2')
hr3 = horce('horce 3')
hr4 = horce('horce 4')

print('Here ls_hr is class variable.')
#can directly use class name 'horce' without creating object of that class.
print (horce.ls_hr)
print(len(horce.ls_hr))

print()
print (horce.num_horce())

print()
horce.spk_run(6)