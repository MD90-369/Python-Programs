# To create a smiley using strings and loops

char = '\u2588'
fill = '\u1F7E8'

image = [
    '0000001111000000',
    '0000112222110000',
    '0001222222221000',
    '0012222222222100',
    '0122222222222210',
    '0122112222112210',
    '1221221221221221',
    '1222222222222221',
    '1222222222222221',
    '1222111111112221',
    '0122122222212210',
    '0122212222122210',
    '0012221111222100',
    '0001222222221000',
    '0000112222110000',
    '0000001111000000',
]

for row in image:
    for pixel in row:
        if (pixel == '0'):
            print('  ', end='')
        elif (pixel == '2'):
            print(fill)
        else:
            print(char * 2, end='')
    print()