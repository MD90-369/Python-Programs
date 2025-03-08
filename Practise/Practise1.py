#To print squares and cubes of numbers from 1 to 20
print(" ")
print("[NORMAL VERSION]")
print(" ")
print('"SQUARES OF NUMBERS FROM 1 TO 20 :"')
for i in range(1,21):
	print(f"Square of {i}:{i*i}")
print(" ")
print('"CUBES OF NUMBERS FROM 1 TO 20 :"')
for i in range(1,21):
	print(f"Cube of {i}:{i*i*i}")
print(' ')
# Advanced version(print till user wishes)

num = int(input("Enter a number : "))
print("{ADVANCED VERSION}")
for i in range(1, num):
	print(f"Square of {i}:{i*i}")
	print(f"Cube of {i}:{i*i*i}")