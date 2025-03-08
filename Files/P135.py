#To read 'students.bin' and add 2 more students to it

import pickle

with open('./students.bin', mode = 'rb') as file:
	file_data = pickle.load(file)

for i in file_data:
	print('Name:', i['name'])
	print('Age:', i['age'])
	print('Marks:', i['marks'])
	print('Favourite Subject:', i['fav'])
	print()

for i in range(2):
    student = {}
    student['name'] = input('Enter student name:')
    student['age'] = int(input('Enter student age:'))
    student['marks'] = int(input('Enter student marks:'))
    student['fav'] = input('Enter student Fav. Subject: ')
    file_data.append(student)

with open('./students.bin', mode = 'wb') as file:
	pickle.dump(file_data, file)