#To read computer.txt and print the no. of lines and words in it.
file = open('./computer.txt')

file_data = file.read() # Read the entire file and returns list of lines(string)
print('Number of Lines : ', len(file_data.split('\n')))
print('Number of Words : ', len(file_data.split(' ')))
file.close()