#To read 'students.csv' and display it nicely

import csv

with open('./students.csv', mode = 'r') as file:
	file_data = list(csv.reader(file))
	
	for row in file_data[1:]:
		# List Unpacking
		name, age, fav, marks = row
		print(' Name : ', name)
		print( ' Age : ', age)
		print(' Favourite Subject : ', fav)
		print(' Marks : ', marks)
		print()