print('OOP 4')
print('Overloading python default methords. __str__, __eq__, etc.')
print()

class point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __add__(self, p):
		return point(self.x + p.x, self.y + p.y)
	def __sub__(self, p):
		return point(self.x - p.x, self.y - p.y)
	def __mul__(self, p):
		return point(self.x * p.x, self.y * p.y)
	
	def dis(self):
		import math
		return math.sqrt(self.x**2 + self.y**2)
	def __gt__(self, p):
		return self.dis() > p.dis()
	def __ge__(self, p):
		return self.dis() >= p.dis()
	def __lt__(self, p):
		return self.dis() < p.dis()
	def __le__(self, p):
		return self.dis() <= p.dis()
	def __eq__(self, p):
		return self.x == p.x and self.y == p.y
	
	def __str__(self):
		return '(' + str(self.x) + ',' + str(self.y) + ')'

pt1 = point(6, 9)
pt2 = point(7, 11)
pt3 = point(3, 8)
pt4 = point(5, 14)

print(pt1 + pt2)
print(pt2 - pt3)
print(pt3 * pt4)

print(pt1 <= pt2)
print(pt3 > pt4)
print(pt2 == pt3)

print()
print('OOP 5')
