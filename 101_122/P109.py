#To accept a title and a list for a menu

def menu(items, title= 'MENU'):
	print(title)
	for i in range(len(items)):
		print(i+1,'.', items[i])

if __name__ == '__main__':
	title = input("Enter menu title:")
	list1 = input("Enter a list of items:").split(' ')

	menu(list1, title)