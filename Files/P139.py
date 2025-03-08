#To perform  CRUD operations on 'pokemon.csv'

from menu import menu
import csv


def read_data():
	with open('./pokemon.csv', mode= 'r', newline = '') as file:
		file_data = list(csv.DictReader(file))
	return file_data


def write_data(data_to_write):
	with open('./pokemon.csv', mode= 'w', newline = '') as file:
		if(data_to_write):
			fieldnames = data_to_write[0].keys()
		else:
			fieldnames = []

		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(data_to_write)


def create_element():
	pokemon = {}
	pokemon['name'] = input('Enter pokemon\'s name : ')
	pokemon['type-1'] = input('Enter pokemon\'s type-1 : ')
	pokemon['type-2'] = input('Enter pokemon\'s type-2 : ')
	pokemon['hp'] = int(input('Enter pokemon\'s hp : '))
	pokemon['attack'] = int(input('Enter pokemon\'s attack : '))
	pokemon['defense'] = int(input('Enter pokemon\'s defense : '))
	pokemon['sp-att'] = int(input('Enter pokemon\'s special attack : '))
	pokemon['sp-def'] = int(input('Enter pokemon\'s special defense: '))
	pokemon['speed'] = int(input('Enter pokemon\'s speed : '))
	pokemon['bst'] = pokemon['hp'] + pokemon['attack'] + pokemon['defense'] + pokemon['sp-att'] + pokemon['sp-def'] + pokemon['speed'] 
	data = read_data()
	data.append(pokemon)
	write_data(data)
	print('Added new pokemon :', pokemon['name'])


def view_element_num():

	num = int(input('Which pokemon number to display? : '))
	data = read_data()
	if num > len(data):
		print('NOTE : Write number between 1 to', len(data))
	else:
		pokemon = data[num]
		print()
		print('Name:', pokemon['name'])
		print('Type-1:', pokemon['type-1'])
		print('Type-2:', pokemon['type-2'])
		print('Hp:', pokemon['hp'])
		print('Attack:', pokemon['attack'])
		print('Defense:', pokemon['defense'])
		print('Special Attack:', pokemon['sp-att'])
		print('Special Defense:', pokemon['sp-def'])
		print('Speed:', pokemon['speed'])
		print('Total(bst):', pokemon['bst'])


def view_element_name():

	name = input('Which pokemon to display? : ').lower()
	data = read_data()

	found = False

	for pokemon in data:
		if name == pokemon['name'].lower():
			print()
			print('Name:', pokemon['name'])
			print('Type-1:', pokemon['type-1'])
			print('Type-2:', pokemon['type-2'])
			print('Hp:', pokemon['hp'])
			print('Attack:', pokemon['attack'])
			print('Defense:', pokemon['defense'])
			print('Special Attack:', pokemon['sp-att'])
			print('Special Defense:', pokemon['sp-def'])
			print('Speed:', pokemon['speed'])
			print('Total(bst):', pokemon['bst'])

			found = True
			break

	if not found:
		print('Pokemon Not Found')


def update_element():
	name = input('Which pokemon to update? : ').lower()
	data = read_data()

	keys = ['type-1', 'type-2', 'hp', 'attack', 'defense', 'sp-att', 'sp-def', 'speed']
	menu(keys, '\nWhat should we update')
	choice = int(input('Enter your choice(1-8) : '))

	if (choice < 1 or choice > 8 ):
		print('Invalid Choice, choose 1-8 ONLY')
	else:
		prop = keys[choice-1]

		found = False

		for pokemon in data:
			if name == pokemon['name'].lower():
				new_value = input('Enter new value :')
				pokemon[prop] = new_value

				found = True
				break

		if not found:
			print('Pokemon Not Found')
		else:
			write_data(data)
			print('Updated pokemon :', name)


def delete_element():
	name = input('Which pokemon to delete? : ').lower()
	data = read_data()
	new_data = []

	for pokemon in data:
		if name != pokemon['name'].lower():
			new_data.append(pokemon)

	write_data(new_data)
	print('Deleted pokemon :', name)



options = ['Create', 'View by number', 'View by name', 'Update', 'Delete', 'Exit']
choice = '0'

while choice != '6':

	menu(options, '\n::::::::::: Pokedex :::::::::::')
	choice = input('Enter your choice(1-6) : ')
	
	if choice == '1':
		create_element()
	elif choice == '2':
		view_element_num()
	elif choice == '3':
		view_element_name()
	elif choice == '4':
		update_element()
	elif choice == '5':
		delete_element()
	elif choice != '6':
		print('Enter your choice 1-6 ONLY ')
