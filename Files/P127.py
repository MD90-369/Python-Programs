#To read computer.txt and calculate the word frequency

with open('./computer.txt') as file:
	file_data = file.readlines()
	countdict = {}
	for line in file_data:
		words = line.split(' ')
		for word in words:
			word = word.lower()
			countdict[word] = countdict.get(word, 0) + 1

	item_list = list(countdict.items())	

	for item in item_list:
		key, value = item

		print(key, ':', value)
	# print('The word frequency is', countdict.items())