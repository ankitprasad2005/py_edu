print('Day 13')
print('Reeding .txt file')
print()
txt1 = open('Reeding file.txt', 'r')
list1 = txt1.readlines()
print(list1)
print()

list2 = []
for ln1 in list1:
	if ln1[-1] == '\n':
		list2.append(ln1.strip('\n'))
		print(ln1)
	else:
		list2.append(ln1)
		print(ln1)
print(list2)
print()

list6 = []
for ln1 in list1:
	if ln1[-1] == '\n':
		list6.append(ln1.strip())
		print(ln1)
	else:
		list6.append(ln1)
		print(ln1)
print(list6)
print()

list4 = []
for ln1 in list1:
	if ln1[-1] == '\n':
		list4.append(ln1[:-1])
		print(ln1)
	else:
		list4.append(ln1[:-1])
		print(ln1)
print(list4)
print()


list3 = []
for ln2 in list1:
	list3.append(ln2.strip('\n'))
	print(ln2)
print(list3)

list5 = []
for ln2 in list1:
	list5.append(ln2.strip())
	print(ln2)
print(list5)



txt1.close()
print()
print('Day 14')