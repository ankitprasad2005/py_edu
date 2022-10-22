print('Day 11')
print('[start:stop:step]')
print()
print('Enter 4 words (Clock enter after each)')
inp1 = input('1st: ')
inp2 = input('2nd: ')
inp3 = input('3rd: ')
inp4 = input('4th: ')
lis1 = [inp1, inp2, inp3, inp4]
num1 = int(input('Enter position of a word:')) - 1
print('The word is: ', lis1[num1])
inp10 = input('Type one more item: ')
print('Enter the position in the list where you want to add', inp10, ': ')
num10 = int(input()) - 1
lis1[num10:num10] = inp10
print(lis1)

print()
print('Enter any sentence:')
inp5 = input()
num2 = int(input('Enter a number which is less than the total letters in the line including space:')) - 1
print('Letter at that position is: ', inp5[num2])
print('Enter position of 2 letters to get the letrers between the words (Click enter after each letter): ')
num3 = int(input()) - 1
num4 = int(input()) 
print('The sentence between the 2 letters are: ')
print(inp5[num3:num4:1])
print('The sentence before is: ', inp5[:num3])
print('The sentence after is: ', inp5[num4:])
print()
num5 = int(input('Enter a number by which u want to skip letters of the part of sentence: ')) + 1
print('The part of sentence after skipping', num5, 'letters: ')
print(inp5[num3:num4:num5])
print('The whole sentence after skippinh', num5, 'letters: ')
print(inp5[::num5])
print()
print('Day 12')