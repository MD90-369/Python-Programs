#To read 'file.txt' and replace the first line if user wants.

with open('./file.txt', mode = 'r+') as file:
	file_data = file.read()
	print('File data of file.txt:\n', file_data)

	ans = input('Do you want to replace the first line?(Y/N): ').upper()
	if ans == 'Y':
		l1 = input('Enter new line: ')
		file.seek(0)
		file.write(l1+'\n')
	elif ans == 'N':
		print('OK')
	else:
		print('Error : Invalid Input, Restart the program')