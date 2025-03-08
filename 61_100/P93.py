# To make a calculator

ch = 'a'

while (ch != 'x' and ch != 'X'):
    print('******* Calculator *******')
    print('1. Add ')
    print('2. Subtract ')
    print('3. Multiply ')
    print('4. Divide ')
    print('5. Remainder')
    choice = input('Enter your choice (1-5) : ')

    if choice == '1':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = num1 + num2
        print('Sum: ', result)
    elif choice == '2':
        num1 = int(input('Enter number to subtract from : '))
        num2 = int(input('Enter number to subtract : '))
        result = num1 - num2
        print('Result: ', result)
    elif choice == '3':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = num1 * num2
        print('Product: ', result)
    elif choice == '4':
        num1 = int(input('Enter dividend: '))
        num2 = int(input('Enter divisor: '))
        if num2 != 0:
            result = num1 / num2
            print('Result: ', result)
        else:
            print('Cannot divide by zero.')
    elif choice == '5':
        num1 = int(input('Enter dividend: '))
        num2 = int(input('Enter divisor: '))
        if num2 != 0:
            result = num1 % num2
            print('Remainder: ', result)
        else:
            print('Cannot calculate remainder when divisor is zero.')
    else:
        print('Invalid Input')

    ch = input('\n(Press Any Key to Continue)\n(x to exit)\n\n')
