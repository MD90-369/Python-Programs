# To accept name, age, marks & fav. subject of 10 student and write it to a file “students.bin”

import pickle

student_list = [ ]

for i in range(10):
    student = {}
    student['name'] = input('Enter student name:')
    student['age'] = int(input('Enter student age:'))
    student['marks'] = int(input('Enter student marks:'))
    student['fav'] = input('Enter student Fav. Subject: ')
    student_list.append(student)

with open('./students.bin', mode="wb") as file:
    pickle.dump(student_list, file)