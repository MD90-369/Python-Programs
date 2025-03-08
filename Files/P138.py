#To read 'pokemon.csv' and then create a file 'strong-pokemon.csv' having the pokemon with bst greater than 500

import csv

with open('./pokemon.csv', mode = 'r') as inputfile, open('./strong-pokemon.csv', mode = 'w', newline='') as outputfile:
	file_data = list(csv.reader(inputfile))
	writer = csv.writer(outputfile)

	for row in file_data[1: ]:
		*rest, bst = row
		bst = int(bst)

		if bst >= 500 :
			writer.writerow(row)
