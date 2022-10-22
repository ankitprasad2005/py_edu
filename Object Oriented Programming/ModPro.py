class _pri:
	def __init__(self, name):
		self.name = name
	def display(self):
		print (self.name, 'is display of private class')

class pub:
	def __init__(self, name):
		self.name = name
	def display(self):
		print(self.name, 'is public display of public class')
	def _display(self):
		print(self.name, 'is private display of public class')