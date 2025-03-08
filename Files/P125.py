#To read password.txt and tell the user the website's password they need.
from menu import menu 

file = open('./password.txt')

file_data = file.readlines()

wl = []
for line in file_data[1: ]:
	website_name = line.split(': ')[0]
	wl.append(website_name)

menu(wl)
choice = int(input(f'Enter the website number (1 - {len(wl)}): '))
print('Password of ', file_data[choice])

file.close()
