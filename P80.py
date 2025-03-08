#To print the table till user wishes
tnum = int(input('Enter number to print table :'))
num = int(input('Table Till where ? :'))
for i in range(1, num + 1):
	print(tnum, 'x', i, '=',tnum*i)