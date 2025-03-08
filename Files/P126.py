#To read 'votes.txt' and find the favourite superhero

with open('./votes.txt') as file:
	file_data = file.readlines()
	votedict = {}
	for i in file_data:
		votedict[i] = votedict.get(i, 0) + 1
	print('The favourite superhero is', votedict)
