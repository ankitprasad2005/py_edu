print('Day 15')
print('.find(), .count()')
print()
print('Enter random letters or caracter: ')
inp1 = input()
print('Enter any letter or carrecter to know if there is any of the letter or caracter:')
inp2 = input()
num1 = inp1.count(inp2)
num2 = inp1.find(inp2) + 1
if  num1 != 0:
	print('There are', num1 , inp2, 'in the statement and first', inp2 , 'in the statement is at', num2 ,'position.')
else:
	print('There are no', inp2 ,'in the statement.')
print()
print('Day 16')