#To create a calculator using functions

from menu import menu

def add(x, y):
	return x + y

def sub(x, y):
	return x-y

def mul(x, y):
	return x*y

def div(x, y):
	if y == 0:
		print("Cannot be divided by 0")
	else:
		return x/y

def mod(x, y):
	if y == 0:
		print("Cannot be divided by 0")
	else:
		return x%y
 
ch = 'a'

while (ch != 'x' and ch != 'X'):

	title = "******* Calculator *******"
	options = ["Addition", "Subtraction", "Multiplication", "Division", "Remainder"]

	menu(options, title)

	choice = input('Enter your choice (1-5) : ')

	while True:
		try:
			if choice == '1':
				x = int(input("Enter the first number:"))
				y = int(input("Enter the second number:"))
				answer = add(x, y)
				print("Answer :", answer)
			elif choice == '2':
				x = int(input("Enter the first number:"))
				y = int(input("Enter the second number:"))
				answer = sub(x, y)
				print("Answer :", answer)
			elif choice == '3':
				x = int(input("Enter the first number:"))
				y = int(input("Enter the second number:"))
				answer = mul(x, y)
				print("Answer :", answer)
			elif choice == '4':
				x = int(input("Enter the first number:"))
				y = int(input("Enter the second number:"))
				answer = div(x, y)
				print("Answer :", answer)
			elif choice == '5':
				x = int(input("Enter the first number:"))
				y = int(input("Enter the second number:"))
				answer = mod(x, y)
				print("Answer :", answer)
			else:
				print("Invalid choice")
		except ValueError:
			print('Enter valid number only.')
		else :
			break

	ch = input('\n(Press Any Key to Continue)\n(x to exit)\n\n')