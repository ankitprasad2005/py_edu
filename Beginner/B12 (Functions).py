print('Day 12')
print('def, return')
print()
def speed(distance, time):
	sp = distance / time	
	return print('Speed of the object is= ',sp)
def volt(current, resistance):
	vol = current * resistance
	return print('Volt between the resistor= ', vol)
print('To calculate speed enter the following info:')
num1 = int(input('Enter distance: '))
num2 = int(input('Enter time: '))
speed(num1,num2)
print('To calculate voltage between resistor enter the following info:')
num3 = int(input('Enter current: '))
num4 = int(input('Enter resistance: '))
volt(num3,num4)
print()
print('Day 13')