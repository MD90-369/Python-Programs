# To find all factors of a number

def find_factors(number):
    # Iterate from 1 to the number
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors


while True:
    try:
        num = int(input("Enter a number : "))
        result_factors = find_factors(num)
    except ValueError:
        print('Please enter a valid number')
    else:
        print(f"The factors of {num} are: {result_factors}")
        break