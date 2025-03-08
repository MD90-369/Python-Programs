#To read 'actors.txt' and add more actors that don't exist in the file.

with open('./actors.txt', mode = 'a+') as file:
	file.seek(0)
	file_data = file.readlines()
	print('File data of actors.txt:\n', ''.join(file_data))

	ans = 'Y'

	while (ans == 'Y'):
		ans = input('Do you want to add more actors?(Y/N):').upper()

		if ans == 'Y':
			act = input('Enter new actor :').lower()
			act += '\n'
			
			if (act in file_data):
				print('Actor already present in file.')
			else:
				file.write(act)
				file_data += [act]
				print('Ur data has been added to the file.')

		else:
			print('No actors added')
			break


