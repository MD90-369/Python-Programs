# To create a arithmetic calculator using dictionary and hashing
print('ARITHMETIC CALCULATOR')

print('+:Addition')
print('*:Multiplication')
print('-:Subtraction')
print('/:Division')
print('%:Modulus')

choice = input('Enter your choice (+ - * / %) : ')
num1 = int(input('Enter Number 1:'))
num2 = int(input('Enter Number 2:'))

oper = {
	'+':num1+num2,
	'*':num1*num2,
	'-':num1-num2,
	'/':num1/num2,
	'%':num1%num2,
}

print(oper[choice])