#To read 'students.bin' and give 10 grace marks to 2 random students
import pickle
from random import randint

with open('./students.bin', mode = 'rb') as file:
	file_data = pickle.load(file)

for i in file_data:
	print('Name:', i['name'])
	print('Age:', i['age'])
	print('Marks:', i['marks'])
	print('Favourite Subject:', i['fav'])
	print()

rand_num = randint(1, len(file_data))-1
rand_num2 = randint(1, len(file_data))-1

file_data[rand_num]['marks'] += 10
file_data[rand_num2]['marks'] += 10

with open('./students.bin', mode = 'wb') as file:
	pickle.dump(file_data, file)