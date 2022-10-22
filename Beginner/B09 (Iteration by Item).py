print ('Day 9')
print ()
print ('type 5 names (click enter after each):')
inp1 = input('1st: ')
inp2 = input('2nd: ')
inp3 = input('3rd: ')
inp4 = input('4th: ')
inp5 = input('5th: ')
list1 = [inp1, inp2, inp3, inp4, inp5]
print ()
print ('the list which you created is:')
for x in list1:
	print (x)
for x in list1:
	if x == 'ankit' or x == 'Ankit' or x == 'ANKIT' :
		print ('Oo you chose my name too :) ')
	else:
		print ('U didnt chose my name :( ')
print ()
print ()
print ('Day 10')