#To calculate mean, median and mode of all numbers entered by the user
from statistics import mean, median, mode
listnum = input("Enter a list of numbers:")
listnum = listnum.split(" ")

for i in range(len(listnum)):
	listnum[i] = int(listnum[i])

print('Mean : ', mean(listnum))
print('Median: ', median(listnum))
print('Mode : ', mode(listnum))