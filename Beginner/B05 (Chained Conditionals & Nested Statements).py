print ('Day 5')
print ('and, or, not')
print ()
num1 = int(input('type a number between 0 to 10 (even try again by taking any number below 0 and above 10): '))
if num1 < 0 or num1 > 10:
	print ('I told to take number between 0 to 10')
elif num1 > 0 and num1 <10:
		print ('Oh! you follow the instruction')
else:
	print ('I asked you to take number between 0 to 10, so 0 and 10 will not be included')
print ()
num2 = int(input('Take another number between 50 to 100 (even try taking 75):'))
if num2 == 75:
	print ('U took exactly middle number')
elif not(num2 > 50 and num2 < 100):
	print ('I told to take number between 0 to 10')
else:	
	print ('Oh! you follow the instruction')

print ()
num3 = int(input('Take no. smaller than 500'))
num4 = int(input('Take any other no. smaller than 1000'))
if num3 < 500:
	if num4 < 1000:
		print('U follow instruction')
	else:
		print('Strange, U took 1st no. correct but secound no. wrong.')
else:
	pint('U dint followed the instruction in 1st no.')
print ()
print ('Day 6')