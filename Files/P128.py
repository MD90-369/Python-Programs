#To ask user their name, age and address then write it into 'user.txt'

name = input('Enter your name : ')
age = int(input('Enter your age : '))
address = input('Enter your address : ')

with open('./user.txt', mode='w') as file:
	file.write(f'...Your Details...\n Your Name:{name}\n Your Age:{age}\n Your address:{address}')
	print('File created : user.txt')